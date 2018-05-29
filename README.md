# Required packages:

1. datetime
2. os
3. copy

# Run introduction

You just need to call run.sh in the root directory to run the code.
To test the code through insight_testsuite, you can put the expected results under ./tests folder and call run_tests.sh

# Summary of my approach

Our code is used to process the real-time streaming data. So in my codes, I read and process the data line by line.
Before processing the log data, I defined one dictionary to save the current active users. I also defined a list to maintain the order of the users based on the log data.

When a new line a log comes, I will do the following work:
1. Break the line of log into different columns and pick up the useful information, i.e. ip, date, time, cis, accession, extension
2. Check if any active users passed the inactivity_period. If yes, I will finalize the users' session and output a record.
3. Check if the user of the new record existing in the active users dictionary. If yes, I will update the session of the user to the latest active date, time, and webpage record. If not, I will create a new user record in the current active users dictionary.

After read out all of the log record, I will check the current active users dictionary and finalize all of the users sessions.


## Repo directory structure

The directory structure for my repo:

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── sessionization.py
    │   └── time_diff.py
    │   └── output_oneline.py
    │   └── active_user_features.py
    │   └── new_user_activity.py
    ├── input
    │   └── inactivity_period.txt
    │   └── log.csv
    ├── output
    |   └── sessionization.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── inactivity_period.txt
            |   │   └── log.csv
            |   |__ output
            |   │   └── sessionization.txt
            └── test_2
            |   ├── input
            |   │   └── inactivity_period.txt
            |   │   └── log.csv
            |   |__ output
            |   │   └── sessionization.txt
            ├── test_3
                ├── input
                │   └── inactivity_period.txt
                │   └── log.csv
                |── output
                    └── sessionization.txt

# Brief discription of codes
## Codes in ./src folder

1. sessionization.py
The main function. Used to read log.csv in ./input folder, processing the record, and output the result to ./output/sessionization.txt

2. time_diff.py
This function is used to calculate the difference of two dates and times in unit of second

3. output_oneline.py
This function is used to output one record to file ./output/sessionization.txt

4. active_user_features.py
This is a class to define all of the useful features of one record from log.csv as a object

5. new_user_activity.py
This function is used to collect the useful information and output an object of active_user_features

# Three tests in folder ./insight_testsuite/tests

1. test_1
This is the provides test for testing the directory structure of my submitted code

2. test_2
This test is used to test the output when inactivity_period is 1. 

3. test_3
This test is used to test the output when inactivity_period is 86,400. 
