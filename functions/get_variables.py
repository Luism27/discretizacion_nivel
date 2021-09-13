def obtain_variables(n,other_data,index):
    maximos =[]
    minimos = []
    max_index = []
    min_index = []
    variables_temp = [[0 for x in range(6) ] for y in range(n)]
    for i in range(0,n):
        temp_array = []
        for indice in range(index[i], index[i+1]):
            temp_array.append(other_data[indice])
        maximos.append(max(temp_array))
        minimos.append(min(temp_array))
        indice_max = other_data.index(max(temp_array))
        indice_min = other_data.index(min(temp_array))
        max_index.append(indice_max)
        min_index.append(indice_min)
        variables_temp[i][0] = other_data[indice_max - 1]
        variables_temp[i][1]= other_data[indice_max]
        variables_temp[i][2] = other_data[indice_max + 1]
        variables_temp[i][3] = other_data[indice_min - 1]
        variables_temp[i][4]= other_data[indice_min]
        variables_temp[i][5] = other_data[indice_min + 1]
    return maximos, max_index, minimos, min_index, variables_temp