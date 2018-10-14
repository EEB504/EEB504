#Script to download Neon Data from
#http://data.neonscience.org/browse-data?showAllDates=true&showAllSites=true&showTheme=org
#For the ABBY Site, relative humidity data
# The script will download the data, clean the data, and extract median RH value
# 2018-10-14
# Nikhil Deshmukh

# import all useful libraries
import requests
import urllib.request
import shutil
import pandas as pd
import numpy as np

## Iterate through all the months
year_months = [
          "2016-04",
          "2016-05",
          "2016-06",
          "2016-07",
          "2016-08",
          "2016-09",
          "2016-10",
          "2016-11",
          "2016-12",
          "2017-01",
          "2017-02",
          "2017-03",
          "2017-04",
          "2017-05",
          "2017-06",
          "2017-12",
          "2018-01",
          "2018-02",
          "2018-03",
          "2018-04",
          "2018-05",
          "2018-06",
          "2018-07",
          "2018-08",
          "2018-09"]

## define helper functions
def callAPIandDownloadData(year_month):

    # make the api call
    base_url = 'http://data.neonscience.org/api/v0'
    endpoint = 'data'
    product_code= 'DP1.00098.001' # relative humidity
    site_code = 'ABBY'

    package = '?package=basic'

    api_call = str.join('/',[base_url,endpoint,product_code,
                         site_code,year_month,package])

    r=requests.get(api_call)
    # get the download URL
    url = r.json()['data']['files'][1]['url']
    url = url.split('?')[0]
    file_name="ABBY_rel_humid_"+year_month+"_RAW.csv" # distinguish raw data
    # save the data file
    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)


#initialize an empty list
medians=[]

for year_month in year_months:
    callAPIandDownloadData(year_month)
    # load the data file
    df = pd.read_csv("ABBY_rel_humid_"+year_month+"_RAW.csv")
    # test for null value fraction
    if df.isnull().sum()['RHMean']/len(df)<0.3:
        # compute the median for RH column
        median=df['RHMean'].median()
    else:
        median=np.nan
    # append the computed median to a list/array or whatever
    # add the median for this file to the list
    medians.append({year_month: median})
    print(medians)
