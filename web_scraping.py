import requests 
import datetime
'''
Kp index: ID 27
R (Sunspot No.): ID 51
Dst-index (nT): ID 32
ap index (nT): ID 26
f10.7 index: ID 59
'''

'''
------------------------------------------------------------------
1. Example for getting numeric data file with header and footer lines 
   using wget and curl methods in UNIX environment.
--------------------------------------------------
For curl command:
> curl -d  "activity=retrieve&res=hour&spacecraft=omni2&start_date=20050101&end_date=20050301&vars=8&vars=23&scale=Linear&ymin=&ymax=&view=0&charsize=&xstyle=0&ystyle=0&symbol=0&symsize=&linestyle=solid&table=0&imagex=640&imagey=480&color=&back=" https://omniweb.gsfc.nasa.gov/cgi/nx1.cgi > test_curl.txt
Requested data (home page) will be saved at "test_curl.txt" file

For wget command:
>wget --post-data "activity=retrieve&res=hour&spacecraft=omni2&start_date=20050101&end_date=20050301&vars=8&vars=23&scale=Linear&ymin=&ymax=&view=0&charsize=&xstyle=0&ystyle=0&symbol=0&symsize=&linestyle=solid&table=0&imagex=640&imagey=480&color=&back=" https://omniweb.gsfc.nasa.gov/cgi/nx1.cgi -O test_wget.txt
 Requested data (home page) will be saved at "test_wget.txt" file
'''

# Get today's date in YYYYMMDD format
today = datetime.datetime.now().strftime('%Y%m%d')

# Set the URL and parameters
url = "https://omniweb.gsfc.nasa.gov/cgi/nx1.cgi"
params = {
    "activity": "retrieve",
    "res": "day",
    "spacecraft": "omni2",
    "start_date": today,
    "end_date": today,
    "vars": [27, 51, 32, 26, 59],
    "scale": "Linear",
    "view": 0,
    "table": 0
}

# Send the POST request
response = requests.post(url, data=params)

# Check if the request was successful
if response.status_code == 200:
    # Save the response content to a file
    output_file = f"data_{today}.txt"
    with open(output_file, 'w') as file:
        file.write(response.text)
    print(f"Data saved to {output_file}")
else:
    print(f"Failed to retrieve data: {response.status_code}")