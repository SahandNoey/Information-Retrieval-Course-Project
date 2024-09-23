import sys
sys.path.append("/home/sahand/vsCodeProjects/PythonProjects/information-retrieval-final-project/indexConstruction")
sys.path.append("/home/sahand/vsCodeProjects/PythonProjects/information-retrieval-final-project/preprocessor")
sys.path.append("/home/sahand/vsCodeProjects/PythonProjects/information-retrieval-final-project")

import json
from preprocessor.preprocessor import preprocess
from indexConstruction.invertedIndex import InvertedIndex, InvertedIndexType


file_path = "/home/sahand/vsCodeProjects/PythonProjects/information-retrieval-final-project/Dataset/IR_data_news_12k.json"

with open(file_path, 'r') as file:
    data = json.load(file)

ii = InvertedIndex(InvertedIndexType.POSITIONAL, len(data))
champII = InvertedIndex(InvertedIndexType.POSITIONAL, len(data))
counter = 0

for i in data:
    counter += 1
    content = data[str(i)]['content']
    
    condition = False
    if counter == 1:
        condition = True
        print("docID:", int(i))
    tokens = preprocess(content)

    doc_terms = {}
    for j in range(len(tokens)):
        if tokens[j] not in doc_terms:
            doc_terms[tokens[j]] = [0, []]
        
        doc_terms[tokens[j]][0] += 1
        doc_terms[tokens[j]][1].append(j + 1)
    
    for key in doc_terms:
        ii.addPosting(key, int(i) + 1, doc_terms[key][0], doc_terms[key][1])
        # if tf >= 3, so it's a good doc to be in champion list
        if doc_terms[key][0] >= 3:
            champII.addPosting(key, int(i) + 1, doc_terms[key][0], doc_terms[key][1])
    
    if (counter) % 500 == 0:
        print("done processing doc: ", counter)

ii_deleted = ii.deleteMostRepeated(50)
champII_deleted = champII.deleteMostRepeated(50)
InvertedIndex.save(ii_deleted, "12k-ii-deleted-terms.pkl", "wb")
InvertedIndex.save(ii, "12k-ii.pkl", "wb")
InvertedIndex.save(champII_deleted, "12k-champII-deleted-terms.pkl", "wb")
InvertedIndex.save(champII, "12k-champII.pkl", "wb")