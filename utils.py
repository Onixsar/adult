import pandas as pd
import config
import os
import io


def load_data_file_names(data_path=config.data_path):
    return os.listdir(data_path)


def operate_remove_spaces_from_string_type_columns(df):
    str_cols = [x[0] for x in config.COLUMN_TYPES.items() if x[1] == 'str']
    for x in str_cols:
        df[x] = df[x].apply(lambda x: x.replace(' ', '').replace('.', ''))
    return df


def load_train_data(path = config.train_data_path):

    df = pd.read_csv(path, header=None)

    df.columns = config.COLUMN_NAMES
    df = df.astype(config.COLUMN_TYPES)
    df = operate_remove_spaces_from_string_type_columns(df)
    df[config.Y_COLUMN_VAR] = df[config.Y_COLUMN_VAR]\
        .apply(lambda x: config.INCOME_VAR_CONVERSION[x])
    #x, y =
    return df


def load_test_data(path = config.test_data_path):

    with open(path, 'r') as fp:
        x = fp.read()
    data = io.StringIO(x[21:])
    df = pd.read_csv(data, sep=",", header=None)

    df.columns = config.COLUMN_NAMES
    df = df.astype(config.COLUMN_TYPES)
    df = operate_remove_spaces_from_string_type_columns(df)
    df[config.Y_COLUMN_VAR] = df[config.Y_COLUMN_VAR] \
        .apply(lambda x: config.INCOME_VAR_CONVERSION[x])
    return df


def print_categorical_columns_unique_values(df,col_list=config.CATEGORICAL_COLUMNS):

    for i in col_list:
        print(f"{i} : {df[i].nunique()} unique values")
        print((df[i].value_counts() * 100 / len(df)).round(decimals=2))
        print("****************************************************************")
