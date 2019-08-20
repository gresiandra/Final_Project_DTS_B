# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 09:15:44 2019

@author: ASUS
"""

import pandas as pd
import numpy as np
import dash
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from scipy.stats import pearsonr as p
from scipy.stats import spearmanr as s
import scipy.stats as stats

df_juli = pd.read_csv('http://data.jakarta.go.id/dataset/046790f8-0df6-426f-9e0a-7fbe56bc29dd/resource/d6d7861b-fe29-4e6a-8b35-0a31d2055e7b/download/Harga-Harian-Bapok-Juli-2018-edited.csv')
df_agustus = pd.read_csv('http://data.jakarta.go.id/dataset/046790f8-0df6-426f-9e0a-7fbe56bc29dd/resource/73165ae8-3b09-4ad6-b05a-d76ef0f9b345/download/Harga-Harian-Bapok-Agustus-2018-edited.csv')
df_september = pd.read_csv('http://data.jakarta.go.id/dataset/046790f8-0df6-426f-9e0a-7fbe56bc29dd/resource/2f867617-1917-4243-821e-44e9523c7421/download/Harga-Harian-Bapok-September-2018-revised.csv')
df_oktober = pd.read_csv('http://data.jakarta.go.id/dataset/046790f8-0df6-426f-9e0a-7fbe56bc29dd/resource/04267cf4-c7c2-4d76-9656-382466b01200/download/Harga-Harian-Bapok-Oktober-2018-rev.csv')
df_november = pd.read_csv(r'D:\Digitalent\BelajarPhyton\Final Project\dataset\November.csv')
df_desember = pd.read_csv('http://data.jakarta.go.id/dataset/046790f8-0df6-426f-9e0a-7fbe56bc29dd/resource/d32f6b9a-dd7b-405c-83ca-cbe898d134b3/download/Harga-Harian-Bapok-Desember-2018.csv')

tanggal = []
bulan = []

#harga item per 6 bulan
BPjul0 = df_juli[df_juli['komoditi'] == 'Beras Medium'].head(19)
BPagus0 = df_juli[df_juli['komoditi'] == 'Beras Medium'].head(19)
BPsep0 = df_september[df_september['komoditi'] == 'Beras Medium'].head(19)
BPokt0 = df_oktober[df_oktober['komoditi'] == 'Beras Medium'].head(19)
BPnov0 = df_november[df_november['komoditi'] == 'Beras Medium'].head(19)
BPdes0 = df_desember[df_desember['KOMODITI'] == 'Beras Medium'].head(19)

BPjul1 = df_juli[df_juli['komoditi'] == 'Minyak Goreng Curah'].head(19)
BPagus1 = df_juli[df_juli['komoditi'] == 'Minyak Goreng Curah'].head(19)
BPsep1 = df_september[df_september['komoditi'] == 'Minyak Goreng Curah'].head(19)
BPokt1 = df_oktober[df_oktober['komoditi'] == 'Minyak Goreng Curah'].head(19)
BPnov1 = df_november[df_november['komoditi'] == 'Minyak Goreng Curah'].head(19)
BPdes1 = df_desember[df_desember['KOMODITI'] == 'Minyak Goreng Curah'].head(19)

BPjul2 = df_juli[df_juli['komoditi'] == 'Gula Pasir'].head(19)
BPagus2 = df_juli[df_juli['komoditi'] == 'Gula Pasir'].head(19)
BPsep2 = df_september[df_september['komoditi'] == 'Gula Pasir'].head(19)
BPokt2 = df_oktober[df_oktober['komoditi'] == 'Gula Pasir'].head(19)
BPnov2 = df_november[df_november['komoditi'] == 'Gula Pasir'].head(19)
BPdes2 = df_desember[df_desember['KOMODITI'] == 'Gula Pasir'].head(19)

BPjul3 = df_juli[df_juli['komoditi'] == 'Telur Ayam Ras'].head(19)
BPagus3 = df_juli[df_juli['komoditi'] == 'Telur Ayam Ras'].head(19)
BPsep3 = df_september[df_september['komoditi'] == 'Telur Ayam Ras'].head(19)
BPokt3 = df_oktober[df_oktober['komoditi'] == 'Telur Ayam Ras'].head(19)
BPnov3 = df_november[df_november['komoditi'] == 'Telur Ayam Ras'].head(19)
BPdes3 = df_desember[df_desember['KOMODITI'] == 'Telur Ayam Ras'].head(19)

BPjul4 = df_juli[df_juli['komoditi'] == 'Ayam Boiler'].head(19)
BPagus4 = df_juli[df_juli['komoditi'] == 'Ayam Boiler'].head(19)
BPsep4 = df_september[df_september['komoditi'] == 'Ayam Boiler'].head(19)
BPokt4 = df_oktober[df_oktober['komoditi'] == 'Ayam Boiler'].head(19)
BPnov4 = df_november[df_november['komoditi'] == 'Ayam Boiler'].head(19)
BPdes4 = df_desember[df_desember['KOMODITI'] == 'Ayam Boiler'].head(19)

list_BP0 = []
list_BP0.extend(BPjul0['harga'])
list_BP0.extend(BPagus0['harga'])
list_BP0.extend(BPsep0['harga'])
list_BP0.extend(BPokt0['harga'])
list_BP0.extend(BPnov0['harga'])
list_BP0.extend(pd.to_numeric(BPdes0['HARGA']))

list_BP0 = list(map(int, list_BP0))

list_BP1 = []
list_BP1.extend(BPjul1['harga'])
list_BP1.extend(BPagus1['harga'])
list_BP1.extend(BPsep1['harga'])
list_BP1.extend(BPokt1['harga'])
list_BP1.extend(BPnov1['harga'])
list_BP1.extend(pd.to_numeric(BPdes1['HARGA']))

list_BP1 = list(map(int, list_BP1))

list_BP2 = []
list_BP2.extend(BPjul2['harga'])
list_BP2.extend(BPagus2['harga'])
list_BP2.extend(BPsep2['harga'])
list_BP2.extend(BPokt2['harga'])
list_BP2.extend(BPnov2['harga'])
list_BP2.extend(pd.to_numeric(BPdes2['HARGA']))

list_BP2 = list(map(int, list_BP2))

list_BP3 = []
list_BP3.extend(BPjul3['harga'])
list_BP3.extend(BPagus3['harga'])
list_BP3.extend(BPsep3['harga'])
list_BP3.extend(BPokt3['harga'])
list_BP3.extend(BPnov3['harga'])
list_BP3.extend(pd.to_numeric(BPdes3['HARGA']))

list_BP4 = list(map(int, list_BP3))

list_BP4 = []
list_BP4.extend(BPjul4['harga'])
list_BP4.extend(BPagus4['harga'])
list_BP4.extend(BPsep4['harga'])
list_BP4.extend(BPokt4['harga'])
list_BP4.extend(BPnov4['harga'])
list_BP4.extend(pd.to_numeric(BPdes4['HARGA']))

list_BP4 = list(map(int, list_BP4))

i=0
a=1
bln = 6
tgl = 1
flag = 1
datelist = []
date = ''

while(i<len(list_BP0)):
    date = '2018-'+str(bln)+'-'+str(tgl)
    datelist.append(date)
    if i%19==0 and flag > 0:
        tgl=1
        bln+=1
        flag = 0 
    i+=1
    tgl+=1
    flag = 1

df = pd.DataFrame(zip(datelist,list_BP0,list_BP1,list_BP2,list_BP3,list_BP4), columns=['Date', 'Beras Medium',
                         'Minyak Goreng Curah', 'Gula Pasir', 'Telur Ayam Ras', 'Ayam Boiler'])
df = df.drop(index=0, axis = 0)

bulans=[7,8,9,10,11,12]

beras_medium7 = df['Beras Medium'][:19].mean()
beras_medium8 = df['Beras Medium'][19:38].mean()
beras_medium9 = df['Beras Medium'][38:57].mean()
beras_medium10 = df['Beras Medium'][57:76].mean()
beras_medium11 = df['Beras Medium'][76:95].mean()
beras_medium12 = df['Beras Medium'][95:114].mean()
list_beras = []
list_beras.append(beras_medium7)
list_beras.append(beras_medium8)
list_beras.append(beras_medium9)
list_beras.append(beras_medium10)
list_beras.append(beras_medium11)
list_beras.append(beras_medium12)

minyak_goreng_curah7 = df['Minyak Goreng Curah'][:19].mean()
minyak_goreng_curah8 = df['Minyak Goreng Curah'][19:38].mean()
minyak_goreng_curah9 = df['Minyak Goreng Curah'][38:57].mean()
minyak_goreng_curah10 = df['Minyak Goreng Curah'][57:76].mean()
minyak_goreng_curah11 = df['Minyak Goreng Curah'][76:95].mean()
minyak_goreng_curah12 = df['Minyak Goreng Curah'][95:114].mean()
list_minyak = []
list_minyak.append(minyak_goreng_curah7)
list_minyak.append(minyak_goreng_curah8)
list_minyak.append(minyak_goreng_curah9)
list_minyak.append(minyak_goreng_curah10)
list_minyak.append(minyak_goreng_curah11)
list_minyak.append(minyak_goreng_curah12)

gula_pasir7 = df['Gula Pasir'][:19].mean()
gula_pasir8 = df['Gula Pasir'][19:38].mean()
gula_pasir9 = df['Gula Pasir'][38:57].mean()
gula_pasir10 = df['Gula Pasir'][57:76].mean()
gula_pasir11 = df['Gula Pasir'][76:95].mean()
gula_pasir12 = df['Gula Pasir'][95:114].mean()
list_gula = []
list_gula.append(gula_pasir7)
list_gula.append(gula_pasir8)
list_gula.append(gula_pasir9)
list_gula.append(gula_pasir10)
list_gula.append(gula_pasir11)
list_gula.append(gula_pasir12)

telur_ayam_ras7 = df['Telur Ayam Ras'][:19].mean()
telur_ayam_ras8 = df['Telur Ayam Ras'][19:38].mean()
telur_ayam_ras9 = df['Telur Ayam Ras'][38:57].mean()
telur_ayam_ras10 = df['Telur Ayam Ras'][57:76].mean()
telur_ayam_ras11 = df['Telur Ayam Ras'][76:95].mean()
telur_ayam_ras12 = df['Telur Ayam Ras'][95:114].mean()
list_telur = []
list_telur.append(telur_ayam_ras7)
list_telur.append(telur_ayam_ras8)
list_telur.append(telur_ayam_ras9)
list_telur.append(telur_ayam_ras10)
list_telur.append(telur_ayam_ras11)
list_telur.append(telur_ayam_ras12)

ayam_boiler7 = df['Ayam Boiler'][:19].mean()
ayam_boiler8 = df['Ayam Boiler'][19:38].mean()
ayam_boiler9 = df['Ayam Boiler'][38:57].mean()
ayam_boiler10 = df['Ayam Boiler'][57:76].mean()
ayam_boiler11 = df['Ayam Boiler'][76:95].mean()
ayam_boiler12 = df['Ayam Boiler'][95:114].mean()
list_ayam = []
list_ayam.append(ayam_boiler7)
list_ayam.append(ayam_boiler8)
list_ayam.append(ayam_boiler9)
list_ayam.append(ayam_boiler10)
list_ayam.append(ayam_boiler11)
list_ayam.append(ayam_boiler12)

df_new = pd.DataFrame(zip(bulans,list_beras,list_minyak,list_gula,list_telur,list_ayam),
                      columns=['Bulan','Beras Medium','Minyak Goreng Curah', 'Gula Pasir', 'Telur Ayam Ras', 'Ayam Boiler'])

df_new.to_csv('FinalProjectClean1.csv')

df.to_csv('FinalProjectClean.csv')

correlations = df.corr(method="spearman")

f,ax = plt.subplots(figsize=(10,10))
sns.heatmap(correlations, annot=True, linewidths=.5, fmt='.3f', ax=ax)
plt.savefig('heatmap.png')
plt.show()

test_png = 'heatmap.png'
test_base64 = base64.b64encode(open(test_png, 'rb').read()).decode('ascii')

#pasar_x = df['Gula Pasir']
#pasar_y = df['Telur Ayam Ras']
#
#slope, intercept, r_value, p_value, std_err = stats.linregress(pasar_x,pasar_y)
#garis_miring = slope * pasar_x + intercept
#
#spearman_mpgwt, pvalue = s(df['Gula Pasir'], df['Telur Ayam Ras'])

dfma = pd.read_csv("FinalProjectClean.csv",skipinitialspace=True,usecols=['Telur Ayam Ras'])

dfma['MA']=dfma.rolling(window=3).mean()
print(dfma)

pdata = list(range(len(dfma)))
 
#DASH APP
app = dash.Dash()

app.layout = html.Div(children=[
    html.Br(),
    html.Label('X and Y Value'),
    html.H1(''),
    dcc.Dropdown(id='dropdown',
                 options = [
                 {'label':'Beras Medium', 'value':'Beras Medium'},
                 {'label':'Minyak Goreng Curah', 'value':'Minyak Goreng Curah'},
                 {'label':'Gula Pasir', 'value':'Gula Pasir'},
                 {'label':'Telur Ayam Ras', 'value':'Telur Ayam Ras'},
                 {'label':'Ayam Boiler', 'value':'Ayam Boiler'},
                 ],
                    value = 'Beras Medium',
    ),
    html.H2('Harga Rata-Rata Item per Bulan',
        style={
        'textAlign': 'center',
    }),
    html.Div(id='output-container'),
    html.H2('Heatmap Korelasi Harga',
        style={
        'textAlign': 'center',
    }),
    html.Img(src='data:image/png;base64,{}'.format(test_base64)),
    html.H2('Moving Average Telur Ayam Ras',
        style={
        'textAlign': 'center',
    }),
    dcc.Graph(
        id='plotMA',
        figure={
            'data': [
                {'x': pdata, 'y': dfma['Telur Ayam Ras'], 
                 'type': 'lines', 'name': 'Harga Real'},
                {'x': pdata, 'y': dfma['MA'], 
                 'type': 'lines', 'name': 'MA Data'},
            ],
            'layout': go.Layout(
                xaxis={'title': 'Bulan'},
                yaxis={'title': 'Harga'},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )                    
        }
    ),
    html.H2('Grafik Beras Medium per Hari',
        style={
        'textAlign': 'center',
    }),
    dcc.Graph(
        id='plot',
        figure={
            'data': [
                {'x': df['Date'], 'y': df['Beras Medium'], 'type': 'bar', 'name': 'Jumlah Penerbangan'},
            ],
            'layout': go.Layout(
                xaxis={'title': 'Bulan'},
                yaxis={'title': 'Harga'},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )                    
        }
    ),
#    html.H2('Regresi Linear Gula dan Telur Ayam',
#        style={
#        'textAlign': 'center',
#    }),
#    dcc.Graph(
#        id='regresilinear',
#        figure={
#            'data': [
#                go.Scatter(
#                    x=df['Gula Pasir'],
#                    y=df['Telur Ayam Ras'],
#                    mode='markers',
#                    opacity=0.8,
#                    name='data',
#                    marker={
#                        'size': 15,
#                        'line': {'width': 0.5, 'color': 'white'}
#                    }
#                ),
#                go.Scatter(
#                    x=df['Gula Pasir'],
#                    y=garis_miring,
#                    mode='lines',
#                    name='linear regression line',
#                    opacity=0.8,
#                )
#            ],
#            'layout': go.Layout(
#                title='Pearson Value: %.2f ' %(r_value) + ' Spearman Value: %.2f' %(spearman_mpgwt),
#                xaxis={'title': 'Gula Pasir'},
#                yaxis={'title': 'Telur Ayam Ras'},
#                legend={'x': 0, 'y': 1},
#                hovermode='closest'
#            )
#        },                       
#    )
])
    
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='dropdown', component_property='value')])

def update_output(value):  
    return dcc.Graph(
        id='plott',
        figure={
            'data': [
                {'x': df_new['Bulan'], 'y': df_new[''+value], 'type': 'lines', 'name': 'Jumlah Penerbangan'},
            ],
            'layout': go.Layout(
                xaxis={'title': 'Bulan'},
                yaxis={'title': 'Harga'},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )                    
        }
    ),

if __name__ == '__main__':
    app.run_server(debug=False)