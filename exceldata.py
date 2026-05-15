import pandas as pd

df=pd.read_csv('game.csv')

pd.set_option('display.max_columns', None)
data=df.copy()

print(data.info())
print(data.columns)
print(data.head())
print(data.shape)

cols_to_int = ['RefereeID', 'GameID', 'TimeID', 'PauseID', 'HighlightID', 'GameNumberOfPause', 'GameInterruption', 'GameMinuteOfPause', 'GameDurationOfPause']
data[cols_to_int] = data[cols_to_int].astype(int)

data=data.dropna()
data=data.drop(data[data['DateID']=='Invalid'].index)
data = data.drop_duplicates()

print("The Shape of the Data",data.shape)
print(data.head())

data.to_csv('Modified.csv')















