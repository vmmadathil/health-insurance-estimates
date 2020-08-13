#import statements
import pandas as pd
import numpy as np
import mysql.connector

#variables for connecting to my DB
username = 'root'
password = 'Economics100!'
host='127.0.0.1'

#trying to connect to the DB
try:
    #connecting to the database
    con = mysql.connector.connect(
        host=host,
        user=username,
        password=password
    )
    print('successfully connected')
except:
    print('could not connect')


#cursor for the db connection
cursor = con.cursor()

#creating the initial table
query = '''
CREATE TABLE health_insurance_modeling.adult_data AS (
    SELECT *
    FROM health_insurance_modeling.ipums_data_raw AS A
    WHERE A.AGE  >= 18 
        AND 
        A.YEAR = 2008
    );
'''
#executing the query
cursor.execute(query)

print('created initial adult table')


#array for years
years = ['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']

#looping through the years
for year in years:
    
    #query for sql
    query = '''
    INSERT INTO health_insurance_modeling.adult_data (
    SELECT *
    FROM health_insurance_modeling.ipums_data_raw AS A
    WHERE A.AGE  >= 18 
        AND 
        A.YEAR = {}
    );
    '''.format(year)
    #execute code
    cursor.execute(query)

    print('Inserted {} into table'.format(year))


#creating the child data tables

#creating the initial table
query = '''
CREATE TABLE health_insurance_modeling.child_data AS (
    SELECT *
    FROM health_insurance_modeling.ipums_data_raw AS A
    WHERE A.AGE  < 18 
        AND 
        A.YEAR = 2008
    );
'''
#executing the query
cursor.execute(query)
print('created initial child table')


#for loop to populate the child data table
for year in years:
    
    #query for sql
    query = '''
    INSERT INTO health_insurance_modeling.child_data (
    SELECT *
    FROM health_insurance_modeling.ipums_data_raw AS A
    WHERE A.AGE  < 18 
        AND 
        A.YEAR = {}
    );
    '''.format(year)

    #execute code
    cursor.execute(query)
    print('Inserted {} into table'.format(year))

#closing the connection to the DB
con.close()


