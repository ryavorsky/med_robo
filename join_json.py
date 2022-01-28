import json

with open('bibliography.json', 'r', encoding='utf-8') as bib_data:
    bib = sorted(json.load(bib_data), key=lambda d: d['ID'])

with open('abstracts.json', 'r', encoding='utf-8') as tex_data:
    tex = sorted(json.load(tex_data), key=lambda d: d['ID']) 

ID1 = [b['ID'] for b in bib]
ID2 = [t['ID'] for t in tex]

for i in range(len(ID1)):
    bib[i]['reference'] = tex[i]['title']
    bib[i]['abstract'] = tex[i]['abstract']
    

print('Done')

with open('med_robo_papers.json', 'w', encoding='utf-8') as res_file:
    res_file.write(json.dumps(bib, indent=4, ensure_ascii=False, sort_keys=True))
    res_file.close()

