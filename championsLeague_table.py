#!/usr/bin/env python
import pandas as pd

cl_url = 'https://www.bbc.com/sport/football/champions-league/table'

def cl_main(url):
    dfs = pd.read_html(url)
    for i in range(len(dfs)):
        print(f'Group {chr(65+i)}')
        df = dfs[i].loc[:3,['Team','P','W','D','L','F','A','GD','Pts']]
        df = df.reset_index()
        df['index'] = df['index']+1
        df = df.rename(columns={'index':'pos'})
        df = df.set_index('pos')
        print(df)
        print(dfs[i].loc[4]['Team'])
        print()

if __name__=='__main__':
    cl_main(cl_url)
