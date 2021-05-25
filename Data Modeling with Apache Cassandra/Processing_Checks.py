import os
import glob
import csv

def process_file():
    '''
    - Checking your current working directory;
    - Get your current folder and subfolder event data;
    - Create a for loop to create a list of files and collect each filepath;
    - Join the file path and roots with the subdirectories using glob.
    '''
    print(os.getcwd())

    filepath = os.getcwd() + '/event_data'

    for root, dirs, files in os.walk(filepath):
        file_path_list = glob.glob(os.path.join(root,'*'))
        
    return file_path_list
    
def process_data(file_path_list,file,filter_cols):
    '''
    - Initiating an empty list of rows that will be generated from each file;
    - For every filepath in the file path list;
    - Reading csv file;
    - Creating a csv reader object;
    - Extracting each data row one by one and append it;
    - Creating a smaller event data csv file called event_datafile_full csv 
    that will be used to insert data into the Apache Cassandra tables.
    '''
#     filter_cols = ['artist','firstName','gender','itemInSession','lastName','length',\
#                    'level','location','sessionId','song','userId']
    
    full_data_rows_list = [] 

    for f in file_path_list:
        with open(f, 'r', encoding = 'utf8', newline='') as csvfile: 
            csvreader = csv.reader(csvfile) 
            next(csvreader)
            for line in csvreader:
                full_data_rows_list.append(line) 

    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    with open(file, 'w', encoding = 'utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(filter_cols)
        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))
    return full_data_rows_list

# file = 'event_datafile_new.csv'
def checking_output_rows(file):
    '''
    Check the number of rows on .csv file
    '''
    with open(file, 'r', encoding = 'utf8') as f:
        print(sum(1 for line in f))

def checking_total_rows(full_data_rows_list):
    '''
    Get total number of rows .
    '''
    print(len(full_data_rows_list))
    
def checking_rows(full_data_rows_list):
    '''
    Check to see what the list of event data rows will look like.
    '''
    return full_data_rows_list