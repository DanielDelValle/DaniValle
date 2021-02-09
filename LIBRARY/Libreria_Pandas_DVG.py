    
import pandas as pd
import numpy as np


def date_fixer(x):

    """   fixes the usual error on dates   """
    
    import datetime
    if x.year > 1989:
        year = x.year - 100
    else:
        year = x.year
    return datetime.date(year,x.month,x.day)

def csv_info(df):
    """reads and gives main info about a csv file"""
    import pandas as pd
    import numpy as np
    x = pd.read_csv(df)
    print(x.dtypes, "\n\n", "Rows, Columns: ", x.shape,"\n\n", x.columns, "\n\n", x.head())


def list_dif(a, b):

    """ This function returns the items in a(list) that are not present in b(list)"""
    for x in a:
        if x in a and x in b:
            a.remove(x)
        else: x = x
    for y in b:
        if y in a and y in b:
            a.remove(y)
        else: y = y
    return a

def column_lower(df):

    """ Lowers all strings in columns of a dataframe """

    df.columns = [x.lower() for x in df.columns]
    return df     


def intersector(df1, df2, col1, col2):
    """Returns 2 dataframes reduced to common values according specified columns.
        Col1 & Col2 must be string"""

    df1list = set(df1[col1].unique())
    df2list = set(df2[col2].unique())
    countrylist = list(set(df1list).intersection(df2list))

    df1 = df1.loc[df1[col1].isin(countrylist)]
    df2 = df2.loc[df2[col2].isin(countrylist)]

    return df1, df2

def only_desired(df, col1, desired):
    """Returns dataframe slice with only desired values on column.
    Col1 & desired must be string"""

    df2 = df.loc[df[col1] == desired]
    return df2

def str_discarder(df, col1, unwanted):
    """Returns dataframe slice discarding unwanted values on column
    Col1 & unwanted must be string"""

    df2 = df[~df[col1].str.contains(unwanted, na=False)]
    return df2         

def column_lower(df):
    """Returns lowercase for all column names"""

    df.columns = [x.lower() for x in df.columns]


def column_renamer(df, old, new):
    """Renames columns. old is the column to be changed, new the name to be given. 
    Both must be LISTS"""

    changer = dict(zip(old, new))
    df = df.rename(columns = changer)
    return df

def value_renamer(df, col1, old, new):
    """Renames values on column, given their current name and the new name.
    Both in string"""

    df.loc[df[col1] == old, col1] = new


def value_discarder(df, col1, unwanted):
    """Returns dataframe with unwanted values on col1 discarded. 
    Col1 & unwanted must be string""" 

    df.drop(df[df[col1] == unwanted].index, inplace=True)

def str_replacer(df, col1, old, new):
    """Replaces strings on values, given what to remove and what to replace with.
    Both in string"""

    df[col1] = df[col1].str.replace(old , new)

def str_cleaner(df, col1, unwanted):
    """Removes unwanted strings from values on col1"""

    df[col1] = df[col1].str.rstrip(unwanted)


def add_ratio(df, new_col, num, den, mult, round):
    """Adds a column featuring the division between 2 columns (num, den) and multiplicating by "mult", rounding decimals by "round"""

    df[new_col] = ((df[num]/df[den])*mult).round(round)


def gr_meaner(df, col, val):
    """ Groups a dataframe by a column and gives the MEAN of the value (val), rounded on 2 decimals"""

    aggregation_functions = {val: 'mean'}
    df2 = df.groupby(col).aggregate(aggregation_functions).sort_values(val, ascending=False).round(2)
    return df2

def gr_sum(df, col, val):
    """ Groups a dataframe by a column and gives the SUM of the value (val), rounded on 2 decimals"""

    aggregation_functions = {val: 'sum'}
    df2 = df.groupby(col).aggregate(aggregation_functions).sort_values(val, ascending=False).round(2)
    return df2

def most_least(df, col, val, quant):
    """Does the same than gr_meaner but returns just the "quant" (amount) of top and bottom values."""

    aggregation_functions = {val: 'mean'}
    df2 = df.groupby(col).aggregate(aggregation_functions).sort_values(val, ascending=False).round(2).head(quant)
    df3 = df.groupby(col).aggregate(aggregation_functions).sort_values(val).round(2).head(quant)
    return df2, df3



def corrFilter(x: pd.DataFrame, bound: float):
    """Finds most correlated columns in a df, below corr. factr (bound) and discarding duplicates"""
    
    xCorr = x.corr()
    xFiltered = xCorr[((xCorr >= bound) | (xCorr <= -bound)) & (xCorr !=1.000)]
    xFlattened = xFiltered.unstack().sort_values().drop_duplicates()
    return xFlattened


def corr_comparer(df, col):
    """Returns the correlations of a column respect the rest of df columns"""
    return df[df.columns[:]].corr()[col][:].sort_values()



def outlayers_df(df):
    """Removes outlayers in whole df given quantiles"""
    Q1=df.quantile(0.05)
    Q3=df.quantile(0.95)
    IQR=Q3-Q1
    lowqe_bound=Q1 - 1.5 * IQR
    upper_bound=Q3 + 1.5 * IQR
    df = df[~((df < lowqe_bound) | (df > upper_bound)).any(axis=1)]
    print(lowqe_bound,upper_bound)

def outlayers_col(df, outlay_ratio, col):
    """Removes outlayers on ratio, on specified column"""
    df = df[(np.abs(stats.zscore(df[col])) < ratio)]


def nan_replacer(df, col, operator):
    """Replaces NaN values in specific column by a given val(mean, median, 0...)"""
    if isinstance (val, [int, float]):
        df[col] = df[col].fillna(operator)
    else:
        df[col] = df[col].fillna(df[col].operator())

def nan_out_cols(df, ratio):
    """Given a nan ratio (0.9, f.example), drops all columns with it."""
    df=df.dropna(axis=1,thresh=len(df)*ratio)

def nan_out_rows(df, hows):
    """Given a nan ratio (0.9, f.example), drops all rows with it."""
    df=df.dropna(axis=0,how=hows)