import pandas as pd

jobs = pd.read_csv("datasets/Jobs.csv", index_col=0)
print(jobs)