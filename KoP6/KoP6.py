import pandas as pd

players = pd.read_csv('C:/Users/admin/source/repos/KoP_JKH/KoP6/football.csv')

wageAvr = int(sum([int(i) for i in players['Wage']])/len(players['Wage']))

frame = pd.DataFrame(players)
frame = frame[frame['Wage']>=wageAvr]

speedAvr = sum([int(i) for i in frame['SprintSpeed']])/len(frame)

print(speedAvr)

#Результат счёта#
#67,56638061585058
