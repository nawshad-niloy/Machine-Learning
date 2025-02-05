import pandas as pd

DF = pd.read_json('data.json')
print(DF.to_string)


print(DF.corr())

# correlation means how two variables change relative to another . extent : -1 to 1
