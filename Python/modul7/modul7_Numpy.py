import pandas as pd

#5 dane z wikipedii:
population_data = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population') [0]

print("Podgląd danych o populacji:")
print(population_data.head())

state_abbreviations_df = pd.read_html('https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States')[0]

print("\nPodgląd danych o skrótach stanów:")
print(state_abbreviations_df.head())

