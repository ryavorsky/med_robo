import bibtexparser
import json

with open('lit.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

print('Done')

with open('bibliography.json', 'w', encoding='utf-8') as res_file:
    res_file.write(json.dumps(bib_database.entries, indent=4, ensure_ascii=False))
    res_file.close()

