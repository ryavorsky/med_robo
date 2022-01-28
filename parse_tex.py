from pylatexenc.latexwalker import LatexWalker
import json

with open('tex.txt', 'r', encoding='utf-8') as tex_file:
    source = ' '.join(tex_file.readlines()).replace('\n', ' ')

w = LatexWalker(source)
(nodelist, pos, len_) = w.get_latex_nodes(pos=0)


res = []
N = len(nodelist) // 5

print(len(nodelist), N)

for i in range(N):
    paper = dict()
    #paper['o'] = nodelist[5*i].latex_verbatim()
    paper['title'] = nodelist[5*i+1].latex_verbatim()[15:-1]
    #paper['o2'] = nodelist[5*i+2].latex_verbatim()[6:-1]
    paper['ID'] = nodelist[5*i+3].latex_verbatim()[6:-1]
    paper['abstract'] = nodelist[5*i+4].latex_verbatim()
    res.append(paper)

print('Done')

with open('abstracts.json', 'w', encoding='utf-8') as res_file:
    res_file.write(json.dumps(res, indent=4, ensure_ascii=False))
    res_file.close()

