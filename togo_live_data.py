import requests
import pandas as pd

def wb(country, indicator):
    url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json"
    r = requests.get(url).json()
    data = r[1]
    df = pd.DataFrame(data)
    df = df[['date', 'value']]
    df.columns = ['year', indicator]
    df['year'] = df['year'].astype(int)
    return df

indicators = {
    "SP.POP.0014.TO": "children_0_14",
    "SP.POP.65UP.TO": "elderly_65_plus",
    "SP.DYN.CBRT.IN": "birth_rate",
    "SP.POP.TOTL": "total_population"
}

dfs = []

for code, name in indicators.items():
    df = wb("tg", code)
    df.rename(columns={code: name}, inplace=True)
    dfs.append(df)

final = dfs[0]
for df in dfs[1:]:
    final = final.merge(df, on="year", how="outer")

final = final.sort_values("year")

print(final)
final.to_csv("togo_live_population.csv", index=False)
print("\nSaved: togo_live_population.csv")
