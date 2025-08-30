import pandas as pd
import numpy as np

df_video_with_plane = pd.read_csv("./audio_with_train.csv")
df_video_without_plane = pd.read_csv(".audio_without_train.csv")

df1 = df_video_with_plane.drop(['Unnamed: 0'], axis=1)
df2 = df_video_without_plane.drop(['Unnamed: 0'], axis=1)

mini = 100000
maxi = 0
for column in df1.columns:
  mini = min(mini,df1[column].min())
  maxi = max(maxi,df1[column].max())

for column in df2.columns:
  mini = min(mini,df2[column].min())
  maxi = max(maxi,df2[column].max())

for column in df1.columns:
  df1[column] = (df1[column] - mini) / (maxi-mini)

for column in df2.columns:
  df2[column] = (df2[column] - mini) / (maxi-mini)

df1.to_csv("../VIDEO_2/audio_with_train_normalized.csv")
df2.to_csv("../VIDEO_2/audio_without_train_normalized.csv")