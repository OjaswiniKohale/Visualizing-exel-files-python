import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("HabitTracker.xlsx",skiprows=4)
data = data.iloc[:,1:]
data = data.set_index("Date")

data['Supplements'] = data['Supplements'].map({"Yes":1,"No":0})
data['Journaling'] = data['Journaling'].map({"Yes":1,"No":0})
print(data.corr()) 
sns.heatmap(data.corr(),annot=True,cmap="YlGnBu")
plt.show()