# In[1]:

import os
import numpy as np
import pandas as pd
import pickle
import math
from datetime import datetime

import plotly.offline as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
py.init_notebook_mode(connected=True)

# 打印多行
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# In[2]:

# 比特币历史数据
df = pd.read_csv('E:/Repos/BTC_Quantization/Datum_History/CoinMarketCap_Csv/20130428-20210725.tsv', sep='\t')
df.head()

# In[3]:

# 数据清理
def remove_usd_symbol(money):
    return float(money.replace("$", "").replace(',',''))

def convert_to_date(dateString):
    return datetime.strptime(dateString, '%b %d, %Y')

df['Date'] = df['Date'].apply(lambda x: convert_to_date(x))
df['Open'] = df['Open'].apply(lambda x: remove_usd_symbol(x))
df['High'] = df['High'].apply(lambda x: remove_usd_symbol(x))
df['Low'] = df['Low'].apply(lambda x: remove_usd_symbol(x))
df['Close'] = df['Close'].apply(lambda x: remove_usd_symbol(x))
df['Volume'] = df['Volume'].apply(lambda x: remove_usd_symbol(x))
df['Market Cap'] = df['Market Cap'].apply(lambda x: remove_usd_symbol(x))

# 逆序
df = df.sort_values(by = "Date")

# 设置Date为index
df = df.set_index('Date')

df.head()

# In[4]:

# 图1  btc量价图

btc_trace_close = go.Scatter(x=df.index, y=df['Close'], name='price')

btc_bar = go.Bar(x=df.index, y=df["Volume"].map(lambda x: x/10000000), name='volume')

py.iplot([btc_trace_close, btc_bar])


# In[5]:

# 图2 ahr999定投指数
# https://btctom.com/
# AHR999 = 比特币价格/200日定投成本*比特币价格/指数增长估计
# AHR999囤币指标：0.45～1.2
# AHR999x = 200日定投成本/比特币价格*指数增长估计/比特币价格*3

df_ahr999 = df.copy(deep=True)

# 1.获取200日定投成本
def get_first_200day_unit_price(df):
    # 假设每天定投10000刀
    day_cost = 10000
    total_cost = 200 * day_cost
    total_count = df.iloc[0: 199]['Close'].apply(lambda x: day_cost/x).sum(axis=0)
    unit_price = total_cost/total_count
    return unit_price

def get_200day_unit_price(df):
    if(not set(['price200']).issubset(df.columns)):
        df.insert(df.shape[1], 'price200', 1)
        
    for idx in range(df.shape[0]):
        if(idx >= 200):
            price200 = get_first_200day_unit_price(df.iloc[idx-200:])
            df.iloc[idx, 6] = price200
    return df

df_ahr999 = get_200day_unit_price(df_ahr999)

# 2.计算ahr999币价指数增长估计
# 拟合币价 y = 10^(5.84log(币龄)-17.01)
def get_ahr999factor(df):
    if(not set(['ahr999factor']).issubset(df.columns)):
        df.insert(df.shape[1], 'ahr999factor', 1)
        
    for row in df.itertuples():
        days = (row[0]  - datetime(2009,1,3)).days

        price_ahr999factor = math.pow(10, 5.84 * math.log10(days) - 17.01)
        df.loc[row[0], 'ahr999factor'] = price_ahr999factor
    return df
    
df_ahr999 = get_ahr999factor(df_ahr999)

# 3. 获取ahr999
def get_ahr999(df):
    if(not set(['ahr999']).issubset(df.columns)):
        df.insert(df.shape[1], 'ahr999', 1)
    for idx in range(df.shape[0]):
        if(idx >= 200):
            row = df.iloc[idx]
            ahr999 = row['Close'] / row['price200'] * row['Close'] / row['ahr999factor']
            df.iloc[idx, 8] = ahr999
    return df

df_ahr999 = get_ahr999(df_ahr999)

# 4. 获取ahr999x
def get_ahr999x(df):
    if(not set(['ahr999x']).issubset(df.columns)):
        df.insert(df.shape[1], 'ahr999x', 1)
    for idx in range(df.shape[0]):
        if(idx >= 200):
            row = df.iloc[idx]
            ahr999x = 3 / row['ahr999']
            df.iloc[idx, 9] = ahr999x
    return df

df_ahr999 = get_ahr999x(df_ahr999)
df_ahr999 = df_ahr999[200:]

# 5.画图
trace_ahr999 = go.Scatter(
    x = df_ahr999.index, 
    y=df_ahr999['ahr999'].map(lambda x: x),
    text='ahr999',
    name='ahr999')
trace_ahr999x = go.Scatter(
    x = df_ahr999.index, 
    y=df_ahr999['ahr999x'].map(lambda x: x),
    text='ahr999x',
    name='ahr999x')
trace_045 = go.Scatter(
    x = df_ahr999.index, 
    y=df_ahr999['ahr999'].map(lambda x: 0.45),
    text='0.45',
    name='0.45')
trace_120 = go.Scatter(
    x = df_ahr999.index, 
    y=df_ahr999['ahr999'].map(lambda x: 1.20),
    text='1.2',
    name='1.2')
trace = [trace_ahr999, trace_045, trace_120]
layout = go.Layout(
    title="ahr999",
    hovermode='closest',
    xaxis=dict(title='Date', autorange=True),
    yaxis=dict(title='Ahr999', type='log', autorange=True))
fig = go.Figure(data=trace, layout=layout)
py.iplot(fig)

# ahr999x
trace = [trace_ahr999x, trace_045, trace_120]
layout = go.Layout(
    title="ahr999x",
    hovermode='closest',
    xaxis=dict(title='Date', autorange=True),
    yaxis=dict(title='Ahr999x', type='log', autorange=True))
fig = go.Figure(data=trace, layout=layout)
py.iplot(fig)

# In[6]:

# 图3 π周期逃顶指标
# https://www.lookintobitcoin.com/charts/pi-cycle-top-indicator/

df_pi_cycle = df.copy(deep=True)

# 1. 获取ma111
def get_ma111(df):
    if(not set(['ma111']).issubset(df.columns)):
        df.insert(df.shape[1], 'ma111', 1)
    
    for idx in range(df.shape[0]):
        if(idx >= 111):
            ma111 = df.iloc[idx-111:idx-1]['Close'].sum(axis=0)/111
            df.iloc[idx, 6] = ma111
    return df

# 2. 获取ma350*2
def get_ma350mul2(df):
    if(not set(['ma350mul2']).issubset(df.columns)):
        df.insert(df.shape[1], 'ma350mul2', 1)
        
    for idx in range(df.shape[0]):
        if(idx >= 350):
            ma350 = df.iloc[idx-350:idx-1]['Close'].sum(axis=0)/350 * 2
            df.iloc[idx, 7] = ma350
    return df
            
df_pi_cycle = get_ma111(df_pi_cycle)
df_pi_cycle = get_ma350mul2(df_pi_cycle)
df_pi_cycle = df_pi_cycle[350:]

# 3. 画图
trace_ma111 = go.Scatter(x=df.index, y=df_pi_cycle['ma111'], text='ma111', name='MA 111')
trace_ma350mul2 = go.Scatter(x=df.index, y=df_pi_cycle['ma350mul2'], text='ma350 * 2', name='MA 350 *2')
trace_close = go.Scatter(x=df.index, y=df_pi_cycle['Close'])
trace=[trace_ma111, trace_ma350mul2, trace_close]

layout = go.Layout(
    title="Pi Top",
    hovermode='closest',
    xaxis=dict(title='Date', autorange=True),
    yaxis=dict(title='Pi Top', type='log', autorange=True))

fig = go.Figure(data=trace, layout=layout)

py.iplot(fig)

