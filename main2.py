import pandas as pd
import json
import matplotlib.pyplot as plt

with open("sala302.json","r") as file:
    rawData = json.load(file)

df = pd.DataFrame(rawData['data'])

df = df.drop(columns=['_id','location','created_at','deviceId'])

df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp',inplace=True)
df = df.sort_index()


print(df)

print(df.describe())

df['hour'] = df.index.hour
df['date'] = df.index.date
hourProfile = df.groupby('hour')[['temperature','humidity']].mean()
print(hourProfile)
print("------------------------------------------")
#444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
df['day'] = df.index.day
dayProfile = df.groupby('day')[['temperature','humidity']].mean()
print(dayProfile)

df[['temperature','humidity']].plot(figsize=(12,6), title = "larp")
plt.ylabel('Warotsc')
plt.grid(True)
plt.show()


df[['pressure']].plot(figsize=(12,6), title = "larp")
plt.ylabel('Warotsc')
plt.grid(True)
plt.show()