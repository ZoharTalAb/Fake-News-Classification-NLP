import pandas as pd

train = pd.read_csv("data/train.csv", sep=";", index_col=0)
test = pd.read_csv("data/test.csv", sep=";", index_col=0)

print("=== TRAIN SHAPE ===")
print(train.shape)

print("\n=== TEST SHAPE ===")
print(test.shape)

print("\n=== COLUMNS ===")
print(train.columns)

print("\n=== LABEL DISTRIBUTION ===")
print(train["label"].value_counts())
