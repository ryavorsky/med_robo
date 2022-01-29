import json

with open('med_robo_papers.json', 'r', encoding='utf-8') as data_file:
    data = json.load(data_file)

print(len(data))
print(data[0])

result = []

for d in data:
    authors = d['author'].split(' and ')
    for a in authors:
        result.append([d['ID'], a, d['reference']])

with open('authors_papers.txt', 'w', encoding='utf-8') as res_file:
    for r in result:
        res_file.write('\t'.join(r)+'\n')
    res_file.close
    
