import pandas as pd

df = pd.DataFrame()
df = pd.read_csv("goibibo_flights_data.csv")

print("Первые 5 строк")
print(df.head())

print("Информация о датафрейме")
print(df.info())

print("Описательная статистика")
df['price']=df['price'].apply(lambda x: x.replace(',','')).astype('float') #перевод цены в число
print(df.describe())