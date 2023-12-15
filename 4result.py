info = [] 
result = [] 
with open('data.txt', 'r') as f: 
    for line in f: 
        data = line.strip().split(',') 
        info.append(data) 
for row in info: 
    if len(row) >= 4: 
        url = row[3] 
        if '.org' in url: result.append(url) 
        num_sites = len(result) 
        print(num_sites)