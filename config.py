data_path = 'data/'
train_data_path = 'data/adult.data'
test_data_path = 'data/adult.test'

COLUMN_NAMES = ['AGE', 'WORK_CLASS', 'FNLWGT', 'EDUCATION', 'EDUCATIONAL_NUM',
                'MARITAL_STATUS', 'OCCUPATION', 'RELATIONSHIP', 'RACE',
                'GENDER', 'CAPITAL_GAIN', 'CAPITAL_LOSS', 'HOURS_PER_WEEK',
                'NATIVE_COUNTRY', 'INCOME']
X_COLUMNS_VARS = ['AGE', 'WORK_CLASS', 'FNLWGT', 'EDUCATION', 'EDUCATIONAL_NUM',
                  'MARITAL_STATUS', 'OCCUPATION', 'RELATIONSHIP', 'RACE',
                  'GENDER', 'CAPITAL_GAIN', 'CAPITAL_LOSS', 'HOURS_PER_WEEK',
                  'NATIVE_COUNTRY']
Y_COLUMN_VAR = 'INCOME'

COLUMN_TYPES = {'AGE': 'int',
                'WORK_CLASS': 'str',
                'FNLWGT': 'int',
                'EDUCATION': 'str',
                'EDUCATIONAL_NUM': 'int',
                'MARITAL_STATUS': 'str',
                'OCCUPATION': 'str',
                'RELATIONSHIP': 'str',
                'RACE': 'str',
                'GENDER': 'str',
                'CAPITAL_GAIN': 'int',
                'CAPITAL_LOSS': 'int',
                'HOURS_PER_WEEK': 'int',
                'NATIVE_COUNTRY': 'str',
                'INCOME': 'str'
                }


INCOME_VAR_CONVERSION = {'<=50K': 0, '>50K': 1}

CATEGORICAL_COLUMNS = ['WORK_CLASS', 'EDUCATION','MARITAL_STATUS',
                       'OCCUPATION', 'RELATIONSHIP', 'RACE',
                       'GENDER',  'NATIVE_COUNTRY'
                       ]

DROP_COLUMNS = ['EDUCATION', 'NATIVE_COUNTRY']
