info = []
result1 = []
result2=[]
with open('data.txt', 'r') as f:
   for line in f:
      data = line.strip().split(',')
      info.append(data)
      
for row in info:
    need_row = row[3][0:6]
    if row[4] == 'Latvia' and need_row == 'https:':
        result1.append(row[3])
        num_sites = len(result1)
        print(num_sites)