import pandas as pd

def youngestFellah(df, year):
    df = df[df['Year'] == 2004]
    m = df[df['Sex'] == 'M'].sort_values('Age')
    f = df[df['Sex'] == 'F'].sort_values('Age')
    m_age = m.loc[m.index[0], 'Age']
    f_age = f.loc[f.index[0], 'Age']
    return {'f': f_age, 'm': m_age}
