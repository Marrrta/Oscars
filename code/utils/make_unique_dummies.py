'''A function which takes in a dataframe and a column which holds unique values in comma-separated sets for each observation, and creates binary variables representing each separate value
'''
def make_unique_dummies(df, column, separator):
    all_unique = list_uniques(df, column, separator)
    for unique in all_unique:
        df[unique] = df[column].apply(lambda x: 1 if unique in x else 0)

make_unique_dummies.__doc__ = '''
                        A function which takes in a dataframe and a column which holds unique values in comma-separated sets for each observation, and creates binary variables representing each separate value
                        '''
