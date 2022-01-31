import json
import yake

kw_extractor = yake.KeywordExtractor()

with open('med_robo_papers.json', 'r', encoding='utf-8') as data_file:
    data = json.load(data_file)

language = "en"
max_ngram_size = 2
deduplication_threshold = 0.9
numOfKeywords = 20
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)



with open('keywords.txt', 'w', encoding='utf-8') as res_file:
    for paper in data:
        keywords = custom_kw_extractor.extract_keywords(paper['title'] + '. '+ paper['abstract'])
        res_file.write(paper['ID'] + '\n')
        res_file.write(paper['reference'] + '\n')
        for kw in keywords:
            res_file.write(str(kw) + '\n')
        res_file.write('\n')
    res_file.close()


