import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("togo_live_population.csv")

df.plot(x="year", y=["children_0_14", "elderly_65_plus", "total_population"])
plt.title("Togo Population Trends")
plt.xlabel("Year")
plt.ylabel("Population")
plt.show()
