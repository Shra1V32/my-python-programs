import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mail_addresses.csv')
df.fillna("Not Assigned", inplace=True)
df.plot()
plt.show()