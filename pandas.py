import pandas as pd

data = [
    ('row1', 'one'),
    ('row2', 'two'),
]

df = pd.DataFrame(data, columns=["col1", 'col2'])

print(df.head())
