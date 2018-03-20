import pandas as pd

data = pd.read_csv("chopstick-effectiveness.csv")

for col in data.columns:
    data[col] = pd.to_numeric(data[col], errors='coerce')

print "Head of dataset"
print data.head()
print "==============="
print "Head of Efficiency Column"
print data['Food Pinching Efficiency'].head()
