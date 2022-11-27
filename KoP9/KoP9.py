import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tips.csv')

smokedf = pd.DataFrame(df[df['smoker']=='Yes'])
nosmokedf = pd.DataFrame(df[df['smoker']=='No'])

fig = plt.figure();
axes = fig.add_axes([0,0,1,1])
axes.bar(x= nosmokedf['day'].unique(), height=nosmokedf['day'].value_counts(), width = 0.4, align = 'edge', label='астота выдачи чаевых некурящими клиентами')
axes.bar(x= smokedf['day'].unique(), height=smokedf['day'].value_counts(), width = 0.4, align = 'edge', label='Частота выдачи чаевых курящими клиентами')

axes.legend(loc=1)
plt.show()