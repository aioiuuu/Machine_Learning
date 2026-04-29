import pandas as pd

dfjo = pd.DataFrame(
    dict(A=range(1,4), B=range(4,7), C=range(7,10)),
    columns=list('ABC'),
    index=list('xyz'),
)

print(dfjo)

dfjo.to_json("df.json",orient="columns")