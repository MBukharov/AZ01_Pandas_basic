import pandas as pd

df = pd.read_csv("goibibo_flights_data.csv")

print("Первые 5 строк")
print(df.head())

print("Информация о датафрейме")
print(df.info())

print("Описательная статистика")
df.drop(df.columns[[11,12]],axis=1,inplace=True)    #удаление столбцов с пустыми данными
df['price']=df['price'].apply(lambda x: x.replace(',','')).astype('float') #перевод цены в число
print(df.describe())