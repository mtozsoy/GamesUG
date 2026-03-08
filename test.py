import pandas as pd

df = pd.read_csv('games.csv')
# Bakalım Pandas sütunları nasıl eşleştirmiş
print(df[['AppID', 'Name', 'Release date', 'Developers']].head(5))