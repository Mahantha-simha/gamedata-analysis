import pandas as pd
import numpy as np

pd.set_option('future.no_silent_downcasting', True)
pd.set_option('display.max_columns', None)


df1 = pd.read_json('GameFactMockData2.json')
df=pd.json_normalize(df1['gamefact_data'])


a=df[df['GameDuration'] < 0]
df.drop(a.index, inplace=True)


# # print(df.info())
# # print(df.columns)
# # print(df.head())
# # print(df.shape)


df['GameDuration'] = df['GameDuration'].astype(str)
drop = df[df['GameDuration'].str.len() > 2]
df.drop(drop.index, inplace=True)


# df.dropna() # here it will not drop null value because the null itself is in string format

df.replace('None', np.nan, inplace=True)
df.replace('Invalid', np.nan, inplace=True)

dro=df[df['EventID'],['StadiumID'],['RefereeID'],['TimeID'],['DateID'] == np.nan]







# df.to_csv('213e4Jason.csv')

# drop2=df[df['DateID']=='Invalid']
# df.drop(drop2.index, inplace=True)
# print("Data Information",df.info())


cols_to_int = ['EventID', 'RefereeID', 'TimeID', 'DateID', 'PauseID','HighlightID', 'GameDuration','GameNumberOfPause', 'GameInterruption', 'GameMinuteOfPause', 'GameDurationOfPause']
df[cols_to_int] = df[cols_to_int].astype(int)

# print(df.head())



# df.to_csv('ModifiedJason.csv')

#column Event ID

# dropping=df[df['EventID']=='None']
# df.drop(dropping.index, inplace=True)
# df['EventID']=df['EventID'].astype(int)

# print(df.info())

# #column Referee ID
# def xy(x):
#     if 'None' in x:
#         return x.replace('None',np.nan)
#     else :return x

# df['RefereeID']=df['RefereeID'].astype(str).apply(xy) 
# df['RefereeID']=df['RefereeID'].astype(int)  

# print(df['RefereeID'])

# print(df["EventID"].unique())