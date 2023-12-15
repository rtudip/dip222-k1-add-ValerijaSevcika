info = [] 
result = []
with open('data.txt', 'r') as f: 
    for line in f: 
        data = line.strip().split(',') 
        info.append(data) 
for row in info:
    if len(row) >=4 and any('Oman' in url for url in row[3:]): 
        year = row[6]
        print(year)
        