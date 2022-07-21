import pandas as pd

def page_time_per_user(in_root_url, in_filenames, out_file_path):
    
    '''
    Transform web traffic data stored in time-record format where
    each row is a page view into a per-user format where each row is a different user and the
    columns represent the time spent on each of the pages.
        
    ================
        
    Parameters
    in_root_url : str
               the public root url of the stored traffic data
    
    in_filenames: list
              csv files of traffic data stored in a list e.g
              ['a.csv', 'b.csv', 'c.csv']         

    out_file_path: str
                directory or folder to save the output csv file named user_page_time.csv

    '''
    
    #concatenate root url with filename to get individual file url all stored in a list
    urls = [in_root_url + i for i in in_filenames]
    
    #read each csv file into a dataframe and then combine all into a single dataframe
    df = pd.concat((pd.read_csv(file) for file in urls), ignore_index = True)
   
    #Form a dataframe of unique users 
    df_user = pd.DataFrame(df['user_id'].unique(), columns = ['user_id'] )
    
    #unique pages visited by users 
    paths = df['path'].unique()
    
    '''
    For each page visited by users, a dictionary where the key is the user-id and the 
    value is the length of time spent(in seconds) on the page is created
    
    The dictionaries are converted into dataframes and joined by user_id column
    
    NaN values from the resulting dataframe are replaced with zeros. Pages with null values 
    mean that the pages were not visited by the user 
    '''
    for page  in paths:
        
        #filter out individaul page data
        df_page = df[df['path'] == page]

        #dictionary to store user_ids and lenght of time spent on a particular page 
        user_len = {}

        for i in range(len(df_page)):
            user_len[df_page.iloc[i]['user_id']] = df_page.iloc[i]['length']
            
        user_len = pd.DataFrame(pd.Series(user_len).rename(page))
        
        user_len.index.rename('user_id', inplace = True)

        #joining the dataframes for each path
        df_user = df_user.merge(user_len, 'left', on = 'user_id')
        
    #replacing null values with zero
    df_user.sort_values('user_id').fillna(0, inplace = True)
    
    
    
    #output result into specified directory
    df_user.to_csv(out_file_path + 'user_page_time.csv', index = False)

