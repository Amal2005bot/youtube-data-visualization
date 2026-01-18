
from google.colab import files

uploaded = files.upload()

import pandas as pd
import io

df = pd.read_csv(io.BytesIO(uploaded['most_subscribed_youtube_channels.csv']))
display(df)

df = df.replace(',', '')
display(df.head())

import plotly.express as px
fig = px.histogram(df, x='subscribers', title='Subscriber Count')
fig.show()

fig = px.pie(df, values="subscribers", names="category", title="YouTube Categories")
fig.show()

fig = px.box(df, y='started', title='Years Started')
fig.show()