import time
from datetime import datetime, date
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import psycopg2
import pymysql
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer

from db_connect import dbConnect
from data_preprocess import DataCleaning, DataQualityCheck

def generate_QC(self, df, figure_output=0):
        """ 
        Input:  y: time series with sorted time index

        Output: time series data quality metrics
            start, end, timeliness, data_length, completeness, duplicates, mode_D

            start: start of time series
            end: end of time seires
            timeliness: gap between the end of time seires and today, days. 0 means sampling is up to today, 30 means the most recent data was sampled 30 days ago.
            data_length: length of available data in terms of days
            completeness: not NaN/total data in a complete day-by-day time frame, 0 means all data are not valid, 1 means data is completed on 
            duplicates: number of data sampled on same date, 0: no duplicates, 10: 10 data were sampled on a same date
            mode_D: the most frequent sampling interval in time series, days, this is important for determing forecast resolution
        """
        y = df.copy()
        y1 = self.remove_duplicates(y)
        y2 = self.remove_outliers(y)

        if y2.empty:
            # e.g., special case of two datapoint, all data will be considered outlier
            y = y1
        else:
            y = y2
            # construct time frame and create augumented time series
        START, END = y.index.min(), y.index.max()
        TIMELINESS = (datetime.now()-END).days
        
        # this is time series framed in the complete day-by-day timeframe
        y_t = self.day_by_day(y) 
        
        # completeness
        L = len(y_t)
        L_nan = y_t.isnull().sum()
        COMPLETENESS = (1-L_nan/L)[0]
        COMPLETENESS = round(COMPLETENESS, 3)
        DATA_LEN = L

        if COMPLETENESS == 0 | DATA_LEN == 1:
            # no data or 1 datum
            DUPLICATES = np.nan
            MODE_D = np.nan

        else:
            # some data exist
            timediff = pd.DataFrame(np.diff(y.index.values), columns=['D'])
            x = timediff['D'].value_counts()
            x.index = x.index.astype(str)
            # x is value counts of differences between all adjecent sampling dates for one time series

            if x.empty:
                # only one data available, keep row for future data addition
                DUPLICATES = 0
                MODE_D = 0

            elif any(x.index == '0 days') | len(x) == 1:
                # duplicates exists, and all data occur on the same date
                DUPLICATES = x[0]
                MODE_D = 0

            elif any(x.index == '0 days') | len(x) > 1:
                # duplicates exists and data not equally spaced
                DUPLICATES = x[0]
                MODE_D = x[~(x.index == '0 days')].index[0]

            else:  # elif ('0 days' not in x.index):
                # no duplication
                DUPLICATES = 0
                MODE_D = x.index[0]

        START = str(START.date())
        END = str(END.date())
        QC_i = [START, END, TIMELINESS,
                DATA_LEN, COMPLETENESS, DUPLICATES, MODE_D]

        if figure_output == 1:
            # a small plot indicating sampling scheme
            sns.heatmap(y_t.isnull(), cbar=False)
            plt.show()

        return QC_i


def create_qc_tables(sale_type):
    """
    create data quality check table for time series
    User input: sale type 
    """
    sale_type = sale_type

    ## read data from stakeholder's database
    # instantiate db class
    db_c = dbConnect()
    raw_data = db_c.read_stakeholder_db()
    print('data retrieved for local analysis')

    ## Clean data
    dc = DataCleaning()
    df = raw_data.copy()
    df = dc.read_data(df)
    df = dc.remove_zeros(df)
    df = dc.convert_dtypes(df)
    print('data cleaned')

    # All product list
    PRODUCT_LIST = df['product'].unique().tolist()
    # All market list
    MARKET_LIST = df['market'].unique().tolist()
    # All source list
    SOURCE_LIST = df['source'].unique().tolist()

    # prepare table for data quality dimension
    col_names = ['market', 'product', 'source', 'start', 'end', 'timeliness', 'data_length', 'completeness', 'duplicates', 'mode_D']

    m = len(MARKET_LIST)*len(PRODUCT_LIST)*len(SOURCE_LIST)
    # n = len(col_names)
    # print(f'Anticipate qc talbe size is {m*n} entries')

    
    ## Generate quality table with specified data quality dimensions

    # instantiate qc class
    qc = DataQualityCheck()

    # initialize QC table
    QC = [[] for _ in range(m)] 
    i = 0
    for MARKET in MARKET_LIST:
        for PRODUCT in PRODUCT_LIST:
            for SOURCE in SOURCE_LIST:
                print(MARKET, PRODUCT, SOURCE)
                # apply filters
                cond1 = (df['product']==PRODUCT)
                cond2 = (df['source']==SOURCE)
                cond3 = (df['market']==MARKET)
                            
                subset = df[cond1 & cond2 & cond3].sort_values(by='date', ascending=True).set_index('date')
                
                # this is the sale time series
                sale = subset[[sale_type]] 
                
                if sale.empty:
                    break
                
                if len(sale)==sale.isnull().sum().values[0]:
                    break
                    
                else:
                    QC_i = generate_QC(sale, figure_output=0)
                    QC[i] = [MARKET, PRODUCT, SOURCE] + QC_i
                    i = i+1

    # write to DQ dataframe
    QC_df = pd.DataFrame(columns=col_names, data = QC)

    # remove valid data rows but containing NaN in mode_D and duplicates
    QC_df = QC_df[~(QC_df['duplicates'].isnull() | QC_df['mode_D'].isnull())]

    # add id column
    QC_df['qc_id'] = QC_df.index
    cols = QC_df.columns.tolist()
    # move id to first column location
    cols = [cols[-1]] + cols[:-1]
    QC_df = QC_df[cols]

    # populate database with new qc table
    tablename = 'qc_' + sale_type
    db_c.populate_analytical_db(QC_df, tablename)

    

def create_DQI(sale_type):
    """ Design a composite quality index based on 
    data quality dimensions to determine time series quality for forecasting
    """
    # get qc table
    db_c = dbConnect()
    tablename = 'qc_'+ sale_type

    df = db_c.read_analytical_db(tablename=tablename)

    # add an other col to get valid datapoint
    df['data_points']=round(df['data_length']*df['completeness']-df['duplicates'], 0)

    # convert mode_D to float
    df['mode_D'] = df['mode_D'].astype(str).str.rstrip(' days').astype(float)

    # transfer num columns to minmax scale
    cat_cols = ['market', 'product', 'source']
    num_cols = ['timeliness', 'data_length', 'completeness', 'duplicates', 'mode_D','data_points']

    cat_vars = df[cat_cols]
    num_vars = df[num_cols]

    column_trans = ColumnTransformer(
        [('scaled_numeric', MinMaxScaler(), num_cols), 
        ],
        remainder="drop",
    )

    X = column_trans.fit_transform(num_vars)

    # tdf: transformed df 
    tdf = df.copy()
    tdf[num_cols]=X

    # Rank the data for ML candidate using data quality index (DQI)
    # Higher DQI, better data quality
    # DQI based on six data quality dimensions:
    D1, W1 = tdf['data_length'], 0.6
    D2, W2 = tdf['completeness'], 0.3
    D3, W3 = 1-tdf['mode_D'], 0.9
    D4, W4 = 1-tdf['timeliness'], 0.9
    D5, W5 = 1-tdf['duplicates'], 0.3
    D6, W6 = tdf['data_points'], 0.9

    df['DQI'] = D1*W1 + D2*W2 + D3*W3 + D4*W4 + D5*W5 + D6*W6

    df['DQI_cat']=pd.qcut(df['DQI'], [0, .25, .5, .75, 0.9, 1.], labels = [ "poor", "medium", "fair", "good", "great"])

    candidate = df[(df['DQI_cat']=='great') ]
    print(f'len(candidate) time series fall into "great" DQI category' )
    print(candidate)

    # upload dataframe to DB table
    db_c.populate_analytical_db(df, tablename=tablename)
    print('AWS could database updated: added DQI in QC table. ')

    # plt.subplots(figsize=(10, 7))
    # sns.scatterplot('data_points', 'timeliness', hue='DQI_cat', data=df)
    # plt.show()

if __name__ == "__main__":
    start_time = time.time() 
    for item in ['retail', 'wholesale']:
        create_qc_tables(item)
        create_DQI(item)
    elapsed_time = time.time()-start_time
    print(f"--- QC table generated for {sale_type}  and successfually initiated in AWS db. Elapsed time ={elapsed_time/60} minutes! ---" )
