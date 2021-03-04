'''
A function which takes in: the location of files (folder), a string common in files' name, two alternative index labels (in case files were not saved consistently - both can be the same), and a binary argument for dropping duplicates, and returns a concatenated dataframe from all files in the folder with the string in name
'''


def concat_from_files(folder, str_in_name, index_col, alt_index_col, drop_dups):
    data_files = os.listdir(folder) # list of all files in the referenced folder
    relevant_files = [file for file in data_files if file[:len(str_in_name)]==str_in_name] # subset of only files to be merged, based on string common in names of files
    batch_ = {i: 'batch_'+str(i) for i in range(len(relevant_files))} # dictionary for references to which each batch will be assigned before merging
    for i in range(len(relevant_files)):
        try:
            batch_[i] = pd.read_csv(folder+relevant_files[i], index_col=index_col)
        except:
            batch_[i] = pd.read_csv(folder+relevant_files[i], index_col=alt_index_col)

    df = pd.concat([batch_[i] for i in range(len(relevant_files))])
    if drop_dups:
        df.drop_duplicates(inplace=True) # dropping movies which were scraped twice by accident
    return df

concat_from_files.__doc__ = '''
A function which takes in: the location of files (folder), a string common in files' name, two alternative index labels (in case files were not saved consistently - both can be the same), and a binary argument for dropping duplicates, and returns a concatenated dataframe from all files in the folder with the string in name
'''
