import pandas as pd

data = pd.read_html('https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/')
df = data[0]
print(df.head())

#1. zmiana nagłówków
df.columns = ['POZ', 'TYTUŁ', 'ARTYSTA', 'ROK', 'MAX POZ']
#2. pojedyńczy artyści na liście
num_unique_artists = df["ARTYSTA"].unique()
print(f"Liczba unikalnych artystów: {num_unique_artists}")
#3 najczęsciej pojawiąjące się
most_artists = df['ARTYSTA'].value_counts().head()
print("Zespoły najczęściej pojawiające się na liście:")
print(most_artists)

#4 Wielkie litery
df.columns = [col.title() for col in df.columns]

#5 usuwanie max
df = df.drop(columns=['Max Poz'])

#6 najlepszy rok
best_year = df['Rok'].value_counts().idxmax()
print(f"Rok z największą liczbą albumów: {best_year}")

#7 ile albumów między 60 a 90
albums_60_90 = df[(df['Rok'] >= 1960) & (df['Rok'] <= 1990)].shape[0]
print(f"Liczba albumów wydanych między 1960 a 1990 rokiem: {albums_60_90}")

#8 najmłodszy
earliest_albums = df.sort_values('Rok').drop_duplicates('Artysta', keep='first')
print(earliest_albums)

#9 lista najwczęsniej wydanych
earliest_albums = df.sort_values('Rok').drop_duplicates('Artysta', keep='first')
print(earliest_albums)

#10 Zapis do SCV
earliest_albums.to_csv('najwczesniejsze_albumy.csv', index=False)









