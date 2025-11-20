def average_rainfall (rainfall_data):
    average_list=[]
    for i in rainfall_data:
        average = 0
        if len(i) ==0:
            average_list.append(0)
            continue
        else:
            nums_rainfall = 0
            total_rainfall = 0
        for j in i:
            if j>=0:
                total_rainfall += j
                nums_rainfall+= 1
        average = total_rainfall / nums_rainfall 
        average_list.append(average)
    return average_list

rainfall_sample=[
    [], # no rain in September
    [3.2,3.6,2.2], #Three rainfall measurements in October
    [4.1, 4.6], #Two rainfall measurements in November 
]
print(average_rainfall(rainfall_sample)) #expected output: [0,3.0,4.35]

rainfall_2=[
    [1.1], 
    [3.3,4.8,7.3], 
    [3.7, 9.8], 
]
print(average_rainfall(rainfall_2))
rainfall_3=[
    [], 
    [], 
    [], 
]

print(average_rainfall(rainfall_3))
