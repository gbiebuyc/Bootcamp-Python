import pandas as pd

def howManyMedals(df, participant_name):
    ret = {}
    df = df[df['Name'] == participant_name]
    for year, df_year in df.groupby('Year'):
        G = df_year[df_year['Medal'] == 'Gold'].shape[0]
        S = df_year[df_year['Medal'] == 'Silver'].shape[0]
        B = df_year[df_year['Medal'] == 'Bronze'].shape[0]
        ret[year] = {'G': G, 'S': S, 'B': B}
    return ret
