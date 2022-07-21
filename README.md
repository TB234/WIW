##### The python file named page_time_report.py is a script that aggregates web traffic data (in csv files) which include information such as the pages visited and the length of time spent on each page for different users. It outputs a single csv file that contains unique user ids and the length of time each spent on each web page. Read the doc string in the script for more info
Running the script

    Download the file into the directory of your choice and copy the path of the directory

    Add the path of the directory to sys.path so that python can find the module when it is called. Follow the instruction at the following link on how to do this for different operating system. https://bic-berkeley.github.io/psych-214-fall-2016/using_pythonpath.html

    Open a python shell and import the page_time_per_user function from the module. The function takes three postional arguments namely:

    in_root_url : str

            the public root url of the stored web traffic data

    in_filenames: list

            csv files of web traffic data stored in a list          

    out_file_path: str

              directory or folder to save the output csv file named _user_page_time.csv

The function returns a csv file named user_page_time.csv that is stored in the out_file_path

Example:

# imports function from module. Ensure module's directory is added to sys.path to prevent a module error

from page_time_report import page_time_per_user       

# function arguments

in_root_url = 'https://public.wiwdata.com/engineering-challenge/data/'

in_filenames = [chr(i) + ".csv" for i in range (ord('a'), ord('z'))] 

out_file_path = '/home/tbunix/wiw/'  #replace with a valid path on your computer 

# excuting function

page_time_per_user(in_root_url, in_filenames, out_file_path)

The function prints out the following statement after the program runs successfully:

    Access output file: user_page_time.csv at /home/tb23unix/aws/

