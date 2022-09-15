import pandas as pd
from tableone import TableOne, load_dataset

example_data = load_dataset('pn2012')

example_data['death'] = example_data['death'].rename(index={0: "alive", 1: "dead"})

example_data_columns = ['Age', 'SysABP', 'Height', 'Weight', 'ICU', 'death']

example_categorical = ['ICU', 'death']

example_groupby = ['death']
example_labels={'death': 'mortality'}

exampleTab1 = TableOne(example_data, columns=example_data_columns, 
categorical=example_categorical, groupby=example_groupby, rename=example_labels, pval=False)

print(exampleTab1.tabulate(tablefmt = "fancy_grid"))

exampleTab1.to_csv('descriptive\example1\data\exampleTab1.csv')

example_data['death'].head(5)