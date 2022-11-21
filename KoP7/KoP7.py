import pandas as pd

def str_start_with_h(students):
    for i in students['parental level of education']:
        for j in range(len(i)):
            if j>1:
                if i[j]=='h':
                    print(i[j:])
                    break

lambdaF = lambda students: str_start_with_h(students)

studentsPerf = pd.read_csv('C:/Users/admin/source/repos/KoP_JKH/KoP7/StudentsPerformance.csv')

print('Counts students with writing scoregrater then 90\n', len ([i for i in studentsPerf['writing score'] if i >= 90]))

lambdaF(studentsPerf)

##Результаты выполнения##
# Counts students with writing scoregrater then 90
# 78
# helor's degree
# h school
# h school
# h school
# high school
# h school
# high school
# h school
# ...