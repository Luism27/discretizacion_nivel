import json
from functions.positive import isPositive
from functions.read_data import read_data
from functions.get_variables import obtain_variables
index = []
data_time, other_data = read_data('data.json')
for x in range(0, len(data_time)-1) :
    if not isPositive(other_data[x]) and isPositive(other_data[x+1]):
        index.append(x)
print(index)
n = len(index) - 1
maxi, max_index, mini, min_index, variables = obtain_variables(n, other_data,index)

for num in range (0,n):
    max_menos1 = variables[num][0]
    maximo = variables[num][1]
    max_mas1 = variables[num][2]
    min_menos1 = variables[num][3]
    minimo = variables[num][4]
    min_mas1 = variables[num][5]

print(maxi)
print(max_index)
print(mini)
print(min_index)
print(variables)