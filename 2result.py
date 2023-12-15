info = []
result = []
with open('data.txt', 'r') as f:
   for line in f:
      data = line.strip().split(',')
      info.append(data)
      
for row in info:
   if row[4] == 'Latvia' and row[7] == 'Telecommunications':
      result.append(int(row[8]))
      print(sum(result))
