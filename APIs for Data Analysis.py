#APIs installing for Data Science. The latter can be used as an index of APIs used by me.
!pip install pycoingecko
!pip install plotly
!pip install mplfinance
!pip install pandas
!pip install requests
!pip install bs4
#Pandas. It's important for almost everything.
import pandas as pd

#And other very important APIs for this.

import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc


# Creating a pandas dataframe from a dictionary
import pandas as pd
dict ={'a':[11,21,31], 'b':[10,20,30]}

df=pd.DataFrame(dict)
type(df)

#When calling the method head, the dataframe will communicate with the API and will display the first rows.
df.head()

#Also, you can get the mean out of the Dataframe
df.mean()


                                ######Using PyCoinGecko and plotting with Plotly#####



!pip install pycoingecko
from pycoingecko import CoinGeckoAPI
cg=CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
#We will use only the price and time. So, we will retrieve them from the information obtained before with pandas.

data =pd.DataFrame(bitcoin_data['prices'], columns=(['TimeStamp', 'Price']))

#Since the timestamp is not human readable, we will use the pandas to_datetime to convert it into hours, mins, secs,
##etc.

data['Date']= pd.to_datetime(data['TimeStamp'], unit='ms')

#Now we will create a candle stick plot. It will be composed of the min and max price and the first and last price
## of the day. The first step is to use the agg function to get the desired data in rows.

bitcoin_candlestick= data.groupby(data.Date.dt.date).agg({'Price': ['min','max', 'first', 'last']})

#Then, we will install plotly to plot our candle stick plot with bitcoin prices
!pip install plotly
!pip install dash

#Now, we import the plotly.graph_objects library
import plotly.graph_objects as go




#Now, we will create our candlestick

cd=go.Figure(data=[go.Candlestick(x=bitcoin_candlestick.index,
                                  open=bitcoin_candlestick['Price']['first'],
                                  high=bitcoin_candlestick['Price']['max'],
                                  low=bitcoin_candlestick['Price']['min'],
                                  close=bitcoin_candlestick['Price']['last'])
                   ])


cd.update_layout(xaxis_rangeslider_visible=False,
                 xaxis_title='Date',
                 yaxis_title='Price (USD $)',
                 title='Bitcoin Candlestick Chart over the last 30 Days')



#And finally, we plot it all
import plotly as py
py.offline.plot(cd, filename='bitcoin_candlestick_graph.html')


import requests

#We will use the solotodo webpage to check on prices when the knowledge is enough. First, we need to create
##an object for the URL and use the get function. Then we will check the responses of the server.
url='https://www.solotodo.cl'
r= requests.get(url)
r.status_code                   ##200 stands for ok
stbody=r.request.body
stheaders=r.headers
r.encoding

stheaders['date']


#The GET request is used to modify the request of the query. We will use httbin.org, which is a simple HTTP Request
##and Response service. The GET request is used to retrieve information from a source.
url_get='http://httpbin.org/get'
payload={"name": "Joseph", "ID":"123"}

r=requests.get(url_get, params=payload)
r.url
r.request.body
r.status_code
r.text
r.headers['Content-Type'] #Checking the type of data
r.json() #Reading the data in the data type it is formated in.

#The POST request is similar to the GET request. The main difference is, you will get the response in the body, which
##was usually empty in the GET request. The post request is used to insert or update data. The HTTBIN service will send
###Back the "posted" info or sent data  in the body of the request.

url_post= "http://httpbin.org/post"
payload={"name":"Carsten","ID":"123"}
r_post= requests.post(url_post, data=payload)

#As we can see, the requested info is the get request, but not in the post request.
r.url
r_post.url


r.body
r_post.body
