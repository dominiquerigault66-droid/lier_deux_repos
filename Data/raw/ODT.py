
import pandas as pd
df = pd.read_csv("odt.csv", sep=";", encoding='latin1')
print("\n\n", df.describe(), "\n\n", df.info(), "\n\n", df)