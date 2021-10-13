#!/usr/bin/env python
import pandas as pd

pl_url = 'https://www.bbc.co.uk/sport/football/premier-league/table'

def pl_main(url):
    dfs = pd.read_html(url)
    df = dfs[0].loc[:19,['Team','P','W','D','L','F','A','GD','Pts']]
    df = df.reset_index()
    df['index'] = df['index']+1
    df = df.rename(columns={'index':'pos'})
    df = df.set_index('pos')
    print()
    print(df)
    print(dfs[0].loc[20]['Team'])

if __name__=='__main__':
    pl_main(pl_url)
