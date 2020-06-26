

countries_dict = {'Uganda': {'country_code': 'UGA', 'country_name':'Republic of Uganda'},
            'Kenya': {'country_code': 'KEN', 'country_name':'Republic of Kenya'},
            'Congo': {'country_code': 'DRC', 'country_name':'Democratic Republic of the Congo'},
            'Burundi': {'country_code': 'BDI', 'country_name':'Republic of Burundi'},
            'Tanzania': {'country_code': 'TZA', 'country_name':'United Republic of Tanzania'},
            'South Sudan': {'country_code': 'SSD', 'country_name':'Republic of South Sudan'},
            'Rwanda': {'country_code': 'RWA', 'country_name':'Republic of Rwanda'},
            'Malawi': {'country_code': 'MWI', 'country_name':'Republic of Malawi'}}



markets_country = {'UGA': ['Kiboga',
            'Masindi',
            'Tororo',
            'Kampala',
            'Owino',
            'Busia',
            'Kabale',
            'Lira',
            'Kasese',
            'Soroti',
            'Mbale',
            'Gulu',
            'Iganga',
            'Bugiri',
            'Nakasero',
            'Nakawa',
            'Mubende',
            'Arua',
            'Kisenyi',
            'Mbarara',
            'Masaka',
            'Kapchorwa',
            'Kalerwe',
            'Luwero',
            'Isingiro',
            'Kyankwanzi',
            'Kamwenge',
            'Kyenjonjo',
            'Kabarole',
            'Kyegegwa',
            'Rukiga'],
        'KEN': ['Eldoret',
            'Nakuru',
            'Machakos',
            'Makueni',
            'Meru',
            'Mombasa',
            'Kisumu',
            'Nairobi',
            'Kitale',
            'Isiolo',
            'Garissa',
            'Kisii',
            'Busia',
            'Embu',
            'Malindi',
            'Kajiado',
            'Bungoma',
            'Kitui',
            'Wajir',
            'Loitkt',
            'Loitoktok',
            'Kakamega',
            'Taveta'],
        'DRC': ['Kolwezi',
            'Bukavu',
            'Lubumbashi',
            'Uvira',
            'Goma',
            'Likasi',
            'Kasumbalesa'],
        'BDI': ['Bujumbura', 'Gitega', 'Ngozi', 'Kobero'],
        'TZA': ['Iringa',
            'Tunduma',
            'Dar Es Salaam',
            'Arusha',
            'Dodoma',
            'Mbeya',
            'Mwanza',
            'Majengo',
            'Kibaigwa',
            'Tanga/Mgandini',
            'Tabora',
            'Shinyanga',
            'Singida',
            'Songea',
            'Sumbawanga',
            'Njombe',
            'Mtwara Dc',
            'Morogoro urban',
            'Mwanyelwa',
            'Babati',
            'Musoma',
            'Lindi',
            'Mwanga',
            'Moshi',
            'Bukoba',
            'Geita',
            'Temeke',
            'Ilala (Buguruni)',
            'Kinondoni (Tandale)',
            'Kigoma'],
        'SSD': ['Juba', 'Yei'],
        'RWA': ['Rubavu',
            'Mulindi',
            'Kimironko',
            'Kamembe',
            'Ruhengeri',
            'Kimisagara',
            'Ruhuha',
            'Matimba',
            'Kibirizi',
            'Gicumbi',
            'Kigali',
            'Kiramuruzi',
            'Gacurabwenge',
            'Kirambo',
            'Kabaya',
            'Ziniya',
            'Nyabugogo',
            'Byumba',
            'Nyagatare',
            'Rukomo',
            'Gikongoro',
            'Busasamana',
            'Gahoromani',
            'Ndago',
            'Gahanga',
            'Nyamirambo',
            'Nyamata',
            'Base',
            'Gisenyi',
            'Ngororero',
            'Kibuye',
            'Muhanga',
            'Butare',
            'Mahoko',
            'Nkora',
            'Kibungo',
            'Kizi',
            'Ruhango',
            'Buhanda',
            'Mubyangabo',
            'Mukarange',
            'Congonil',
            'Kayenzi',
            'Gaseke',
            'Karenge',
            'Intunga',
            'Mugina',
            'Musanze',
            'Rushashi',
            'Mukamira',
            'Nyakarambi',
            'Muhondo',
            'Rwamagana',
            'Shyorongi',
            'Nyagahinga',
            'Musha',
            'Gasarenda',
            'Gashyushya',
            'Kabarondo',
            'Karambi',
            'Birambo',
            'Gakenke',
            'Bugarama'],
        'MWI': ['Namwera',
            'Ntcheu',
            'Mitundu',
            'Salima',
            'Nkhotakota',
            'Mponela',
            'Mvera',
            'Balaka',
            'Ntchisi',
            'Nkhamenya',
            'Kasungu',
            'Liwonde',
            'Mchinji',
            'Phalombe',
            'Chimbiya',
            'Limbe',
            'Mzuzu',
            'Mzimba',
            'Mwanza',
            'Mkando',
            'Lilongwe',
            'Madisi',
            'Ace Blantyre',
            'Ace Lilongwe',
            'Kamwendo']}

currencies_country = {'UGX': ['UGA', 'KEN', 'BDI', 'RWA', 'DRC', 'TZA', 'SSD'],
        'RWF': ['RWA'],
        'TZS': ['TZA'],
        'MWK': ['MWI'],
        'KES': ['KEN', 'UGA', 'DRC', 'BDI', 'TZA', 'SSD', 'RWA']}

sources_country = {'EAGC-RATIN': ['KEN', 'UGA', 'DRC', 'BDI', 'TZA', 'SSD', 'RWA'],
           'Farmgain': ['UGA'],
           'MIT (Tanzania)': ['TZA'],
           'InfoTrade': ['UGA'],
           'MinAgri(RW) ESOKO': ['RWA'],
           'ACE Malawi/RATIN': ['MWI'],
           'MOA-NAFIS': ['KEN'],
           'RATIN': ['RWA']}

categories_list = ['Cereals - Maize',
                 'Beans',
                 'Animal Products',
                 'Cereals - Other',
                 'Cereals - Rice',
                 'Seeds & Nuts',
                 'Peas',
                 'Fruits',
                 'Roots & Tubers',
                 'Other',
                 'Vegetables',
                 'Farm Inputs',
                 'Fuel']

cat_broken_down = {'Cereals - Maize': ['Dry Maize',
                                'Maize Flour',
                                'Maize Bran',
                                'Green Maize',
                                'Maize',
                                'Imported Maize',
                                'Maize Meal',
                                'Maize Grain'],
                    'Beans': ['Yellow Bean',
                                        'Green Gram',
                                        'White Bean',
                                        'Old Bean',
                                        'Soya Bean',
                                        'Mixed Beans',
                                        'Red Bean',
                                        'Black Bean (Dolichos)',
                                        'Kidney Bean',
                                        'Nambale Bean',
                                        'Agwedde Bean',
                                        'Bean Rosecoco',
                                        'Bean (K132)',
                                        'Mwezi Moja',
                                        'Bean Mwitemania',
                                        'Bean Canadian',
                                        'Bean',
                                        'French Bean',
                                        'Dolicho (Njahi)',
                                        'Green Bean'],
                    'Animal Products': ['Tilapia',
                                        'Pork',
                                        'Goat Meat',
                                        'Nile Perch',
                                        'Milk',
                                        'Turkey',
                                        'Processed Honey',
                                        'Local Egg',
                                        'Local Chicken',
                                        'Exotic Egg',
                                        'Exotic Chicken',
                                        'Beef',
                                        'Unprocessed Honey',
                                        'Egg',
                                        'Sheep',
                                        'Goat',
                                        'Goat Hide and Skin',
                                        'Cow Hide',
                                        'Sheep Hide and Skin',
                                        'Mutton',
                                        'Cow',
                                        'Bull',
                                        'Fresh Milk'],
                    'Cereals - Other': ['Sorghum Grain',
                                        'Sorghum Flour',
                                        'Millet Grain',
                                        'Red Sorghum',
                                        'Wheat',
                                        'Wheat Flour',
                                        'White Sorghum',
                                        'White Millet',
                                        'Pearl Millet',
                                        'Barley',
                                        'Millet Flour',
                                        'Finger Millet',
                                        'Wheat Bran',
                                        'Bulrush Millet',
                                        'Sorghum',
                                        'Millet'],
                    'Cereals - Rice': ['Imported Rice',
                                        'Rice',
                                        'Morogoro Rice',
                                        'Unprocessed/Husked Rice',
                                        'Kilombero Rice',
                                        'Mbeya Rice',
                                        'Upland Rice',
                                        'Kahama Rice',
                                        'Super Rice',
                                        'Kayiso Rice',
                                        'Rice Bran',
                                        'Paddy Rice',
                                        'Tanzanian  Rice',
                                        'Rwandan Rice',
                                        'Asian Rice'],
                    'Seeds & Nuts': ['Sunflower Seed',
                                        'Groundnut',
                                        'Simsim',
                                        'Sunflower Seed Cake',
                                        'Sunflower Seed Meal'],
                    'Peas': ['Green Pea',
                                        'Pigeon Pea',
                                        'Dry Pea',
                                        'Cowpea',
                                        'Chic Pea',
                                        'Fresh Pea',
                                        'Pea'],
                    'Roots & Tubers': ['Cassava Fresh',
                                        'Sun Dried Cassava',
                                        'Red Irish Potato',
                                        'Cassava Flour',
                                        'White Fleshed Sweet Potato',
                                        'White Irish Potato',
                                        'Dry Fermented Cassava',
                                        'Cassava Chips',
                                        'Sweet Potato',
                                        'Irish Potato',
                                        'Round Potato',
                                        'Beet Root'],
                    'Fruits': ['Cooking Banana',
                                        'Pineapple',
                                        'Cavendish (Bogoya)',
                                        'Apple Banana',
                                        'Avocado',
                                        'Pawpaw',
                                        'Lime',
                                        'Mango Ngowe',
                                        'Mango Local',
                                        'Lemon',
                                        'Orange',
                                        'Passion Fruit',
                                        'Ripe Banana',
                                        'Apple',
                                        'Banana Bunch',
                                        'Sweet Banana',
                                        'Mandarine',
                                        'Guava',
                                        'Strawberry',
                                        'Matooke'],
                    'Other': ['Tobacco',
                                        'Coffee (Robusta)',
                                        'Coffee (Arabica)',
                                        'Unprocessed Vanilla',
                                        'Unprocessed Tea',
                                        'Unprocessed Cotton'],
                    'Vegetables': ['Ginger',
                                        'Kale',
                                        'Lettuce',
                                        'Cauliflower',
                                        'Capsicum',
                                        'Cucumber',
                                        'Chilli',
                                        'Spring Onion',
                                        'Onions Dry',
                                        'Tomato',
                                        'Carrot',
                                        'Cabbage',
                                        'Pepper',
                                        'Garlic',
                                        'Red Onion',
                                        'Green Pepper',
                                        'Leek',
                                        'Pounded Cassava Leave',
                                        'White Onion',
                                        'Eggplant',
                                        'Celery',
                                        'Pumpkin',
                                        'Spinach',
                                        'Amaranth',
                                        'Parsley'],
                    'Farm Inputs': ['Ditane',
                                    'NPK Fertilizer',
                                    'Chemical Fertilizer',
                                    'Urea Fertilizer'],
                    'Fuel': ['Wood Charcoal']}

correct_markets_dict = {'Garisa': 'Garissa',
                        'Gichumbi': 'Gicumbi',
                        'Kamwendo Market': 'Kamwendo',
                        'Luwero Market': 'Luwero',
                        'Kakmega': 'Kakamega',
                        'Oloitoktok': 'Loitoktok',
                        'Limbe Market': 'Limbe',
                        'Kinondoni (Tandale )': 'Kinondoni (Tandale)',
                        'Kitale ' : 'Kitale'
}



correct_prod_dict = {'Agwedde Beans': 'Agwedde Bean',
                      'Apple Bananas': 'Apple Banana',
                      'Apples': 'Apple',
                      'Beans': 'Bean',
                      'Beans (K132)': 'Bean (K132)',
                      'Beans Canadian': 'Bean Canadian',
                      'Beans Mwitemania': 'Bean Mwitemania',
                      'Beans Rosecoco': 'Bean Rosecoco',
                      'Beet Roots': 'Beet Root',
                      'Black Beans (Dolichos)': 'Black Bean (Dolichos)' ,
                      'Brinjal/Eggplant': 'Eggplant',
                      'Cabbages': 'Cabbage',
                      'Capsicums': 'Capsicum',
                      'Carrots': 'Carrot', 
                      'Chillies': 'Chilli',
                      'Cooking Bananas':'Cooking Banana',
                      'Cow Peas': 'Cowpea',
                      'Cowpeas': 'Cowpea', 
                      'Dry Peas': 'Dry Pea',
                      'Eggs': 'Egg',
                      'Exotic Eggs': 'Exotic Egg',
                      'French Beans': 'French Bean',
                      'Fresh Peas': 'Fresh Pea', 
                      'Goat Skin And Hide': 'Goat Hide and Skin',
                      'Goats': 'Goat',
                      'Green Beans': 'Green Bean',
                      'Green Peas': 'Green Pea',
                      'Ground Nuts': 'Groundnut',
                      'Groundnuts': 'Groundnut',
                      'Guavas': 'Guava',
                      'Irish Potatoes': 'Irish Potato',
                      'Kales': 'Kale',
                      'Kidney Beans': 'Kidney Bean',
                      'Lemons': 'Lemon',
                      'Limes': 'Lime',
                      'Local Eggs': 'Local Egg',
                      'Mangoes Local': 'Mango Local',
                      'Mangoes Ngowe': 'Mango Ngowe',
                      'Matooke (kg)': 'Matooke',
                      'Matooke (Kg)': 'Matooke',
                      'Matoke': 'Matooke',
                      'Nambale Beans': 'Nambale Bean',
                      'Npk Fertilizer ': 'NPK Fertilizer',
                      'Npk Fertilizer': 'NPK Fertilizer',
                      'Old Beans': 'Old Bean',
                      'Oranges': 'Orange',
                      'Passion Fruits': 'Passion Fruit',
                      'Peas': 'Pea',
                      'Pigeon Peas': 'Pigeon Pea',
                      'Pineapples': 'Pineapple',
                      'Pounded Cassava Leaves': 'Pounded Cassava Leave',
                      'Pumpkins': 'Pumpkin',
                      'Red Beans': 'Red Bean',
                      'Red Irish Potatoes': 'Red Irish Potato',
                      'Red Onions': 'Red Onion',
                      'Ripe Bananas': 'Ripe Banana',
                      'Round Potatoes': 'Round Potato',
                      'Soya Beans': 'Soya Bean',
                      'Spring Onions': 'Spring Onion',
                      'Sunflower': 'Sunflower Seed',
                      'Sun Flower': 'Sungflower Seed',
                      'Sweet Bananas': 'Sweet Banana',
                      'Sweet Potatoes': 'Sweet Potato',
                      'Tomatoes': 'Tomato',
                      'Urea Fertilizer' : 'Urea Fertilizer',
                      'Urea Fertilisers': 'Urea Fertilizer',
                      "Urea Fertilisersâ": 'Urea Fertilizer',
                      'White Beans': 'White Bean',
                      'White Fleshed Sweet Potatoes': 'White Fleshed Sweet Potato',
                      'White Irish Potatoes': 'White Irish Potato',
                      'White Onions' : 'White Onion',
                      'Yellow Beans':'Yellow Bean'}

correct_scale_dict = {'1kg': 'kg',
                    ' (kg)': 'kg',
                    'dozen (13Kg)': 'dozen',
                    'dozen (Kg)': 'dozen',
                    'litre': 'lt'
}