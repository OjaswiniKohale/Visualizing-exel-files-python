import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("HabitTracker.xlsx",skiprows=4)
data = data.iloc[:,1:]
data = data.set_index("Date")

#here index is the date column as we have set it
#a simple line plot
plt.plot(data.index,data['Workout'])
plt.title("Workout Statistics")
plt.xlabel("Date")
plt.ylabel("Time in min")
plt.show()
#another way using seaborn
sns.lineplot(data=data,x="Date",y="Workout")
plt.title("Workout Statistics")
plt.xlabel("Date")
plt.ylabel("Time in min")
plt.show()