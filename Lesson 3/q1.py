# Q1

data = [
    ['tom', 'reacher', 25],
    ['bruce', 'wayne', 30], 
    ['peter', 'parker', 26],
    ['bruce', 'banner', 22]
]

columns = ['FName', 'LName', 'Age']

df = pd.DataFrame(data, columns=columns)

print(df)