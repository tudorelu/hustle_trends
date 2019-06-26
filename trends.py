from pytrends.request import TrendReq

from plotly import tools
import plotly.offline as py
import plotly.graph_objs as go

import pandas as pd
from datetime import datetime


# Login to Google. Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq()

keyword = input('Type a keyword / phrase and press ENTER \n')

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list=[keyword])

# Interest Over Time
print('Search Interest Over Time')
iot_df = pytrend.interest_over_time()
print(iot_df)

iot_trace = go.Scatter(x=iot_df.index, y=iot_df[keyword], name = "Over Time")# domain={'x':[0, 1], 'y':[0, 0.5]})

# Interest by Region
print('Current Interest by Region')
ibr_df = pytrend.interest_by_region()
ibr_df = ibr_df[ibr_df[keyword] > 4]
ibr_df = ibr_df.sort_values(keyword, ascending=False)
# sort regions based on their interest in a decreasing order
print(ibr_df)

ibr_trace = go.Bar(x=ibr_df.index, y=ibr_df[keyword], name = "By Region");
ibr_pie = go.Pie(labels=ibr_df.index, values=ibr_df[keyword]);

# Related Queries, returns a dictionary of dataframes
print('Related Queries')
related_queries_dict = pytrend.related_queries()
top = related_queries_dict[keyword]['top']
top.sort_values('value', ascending=False)
print(top)

related_trace = go.Bar(x=top['query'], y=top['value'], name = "Related Searches");

fig = tools.make_subplots(rows=3, cols=1)

fig.append_trace(iot_trace, 1, 1)
fig.append_trace(ibr_trace, 2, 1)
fig.append_trace(related_trace, 3, 1)

#fig = go.Figure(data=data, layout=layout);
fig['layout'].update(height=600, width=800, title='Search insights for \"'+keyword+'\"')

py.plot(fig, filename='Insights/'+keyword+'_insights.html')

print('\n\n ~~~~~~~~ Some general data about Google Searches Today: ~~~~~~~~ \n\n');

# Get Google Hot Trends data
print('Current Trending Searches')
trending_searches_df = pytrend.trending_searches()
print(trending_searches_df)

# Get Google Hot Trends data
print('Today\'s Trending Searches')
today_searches_df = pytrend.today_searches()
print(today_searches_df)
