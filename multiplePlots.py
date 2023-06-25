import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("HabitTracker.xlsx",skiprows=4)
data = data.iloc[:,1:]
data = data.set_index("Date")

data['Supplements'] = data['Supplements'].map({"Yes":1,"No":0})
data['Journaling'] = data['Journaling'].map({"Yes":1,"No":0})
print(data) 

#multiple plots
fig, axs = plt.subplots(4,1)
axs[0].plot(data.index,data['Workout'])
axs[0].set_title("Workout stats")
axs[0].set_xlabel("Date")
axs[0].set_ylabel("Time(min)")
axs[1].plot(data.index,data['Drinking Water'])
axs[1].set_title("Water stats")
axs[1].set_xlabel("Date")
axs[1].set_ylabel("Water(l)")
axs[2].plot(data.index,data['Reading'])
axs[2].set_title("Reading stats")
axs[2].set_xlabel("Date")
axs[2].set_ylabel("Pages ")
axs[3].plot(data.index,data['Supplements'])
axs[3].set_title("Supplements stats")
axs[3].set_xlabel("Date")
axs[3].set_ylabel("Yes/No")

plt.tight_layout()
plt.show()