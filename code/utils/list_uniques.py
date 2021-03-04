'''A function which takes in a dataframe and an object column which holds comma-separated lists for each observation and produces a global list of unique values'''

def list_uniques(df, column, separator):
    all_split = []
    for _ in list(df[column]):
        for i in range(_.count(separator)):
            all_split.append(_.split(separator)[i])
    all_unique = list(set(all_split))
    all_unique.sort()
    return all_unique


list_uniques.__doc__ = '''
A function which takes in a dataframe and an object column which holds comma-separated lists for each observation and produces a global list of unique values'''
