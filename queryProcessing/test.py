import sys
sys.path.append("/home/sahand/vsCodeProjects/PythonProjects/information-retrieval-final-project/indexConstruction")
sys.path.append("/home/sahand/vsCodeProjects/PythonProjects/information-retrieval-final-project/preprocessor")
sys.path.append("/home/sahand/vsCodeProjects/PythonProjects/information-retrieval-final-project/queryProcessing")
sys.path.append("/home/sahand/vsCodeProjects/PythonProjects/information-retrieval-final-project")
import time
import json
import heapq
from math import log10

file_path = "/home/sahand/vsCodeProjects/PythonProjects/information-retrieval-final-project/Dataset/IR_data_news_12k.json"

with open(file_path, 'r') as file:
    data = json.load(file)

from queryProcessing.queryProcessor import QueryProcessor
from queryProcessing.queryProcessor import PositionalQueryProcessor
from queryProcessing.queryProcessor import EfficientQueryProcessor
from indexConstruction.invertedIndex import InvertedIndex

def print_results(result):
    for i in range(len(result)):
        if isinstance(result[i], tuple):
            json_id_str = str(result[i][0] - 1)
            print(f"DocID in json: {json_id_str}, Score: {result[i][1]}, Title: {data[json_id_str]['title']}, URL: {data[json_id_str]['url']}")
        else:
            json_id_str = str(result[i] - 1)
            print(f"DocID in json: {json_id_str}, Score: PHRASE-QUERY-RESULT, Title: {data[json_id_str]['title']}, URL: {data[json_id_str]['url']}")
        
        print("**** ****\n")
            
def print_in_red(str):
    print(f"\033[91m{str}\033[0m")

ii = InvertedIndex.load("12k-ii.pkl", "rb")
champII = InvertedIndex.load("12k-champII.pkl", "rb")
qp = QueryProcessor(ii)
qp2 = PositionalQueryProcessor(ii)
qp3 = EfficientQueryProcessor(ii, champII)

# dc = ii._InvertedIndex__dictionary
# maxHeap = []
# minHeap = []
# for key in dc:
#     heapq.heappush(maxHeap, (-dc[key].getDF(), key, dc[key].getPostings()[0].getDocID() - 1, dc[key].getPostings()[0].getPositions()))
#     heapq.heappush(minHeap, (dc[key].getDF(), key, dc[key].getPostings()[0].getDocID() - 1, dc[key].getPostings()[0].getPositions()))

# for j in range(3):
#     someMax = heapq.heappop(maxHeap)
#     print(f"Max num {j + 1}: {someMax[1]}, frequency: {-someMax[0]}, firstDocument docID: {someMax[2]}")

# for j in range(3):
#     someMin = heapq.heappop(minHeap)
#     print(f"Min num {j + 1}: {someMin[1]}, frequency: {someMin[0]}, docID: {someMin[2]}, positions: {someMin[3]}")

# dc = ii._InvertedIndex__dictionary
# print(f"length of dictionary: {len(dc)}")
# maxHeap = []
# minHeap = []
# for key in dc:
#     pl = dc[key]
#     heapq.heappush(maxHeap, (-log10(ii.getDocCount() / pl.getDF()), key))
#     heapq.heappush(minHeap, (log10(ii.getDocCount() / pl.getDF()), key))

# theMaxIDF = heapq.heappop(maxHeap)
# theMinIDF = heapq.heappop(minHeap)

# print(f"Word with max idf: {theMaxIDF[1]}, idf-value: {-theMaxIDF[0]}")
# print(f"Word with min idf: {theMinIDF[1]}, idf-value: {theMinIDF[0]}")

# term_tfs = []
# for key in dc:
#     for p in dc[key].getPostings():
#         if p.getDocID() - 1 == 4092:
#             term_tfs.append((key, p.getTF(), dc[key].getDF()))

# maxHeap = []
# minHeap = []
# for el in term_tfs:
#     heapq.heappush(maxHeap, (-(1 + log10(el[1]) * log10(ii.getDocCount() / el[2])), el[0]))
#     heapq.heappush(minHeap, ((1 + log10(el[1]) * log10(ii.getDocCount() / el[2])), el[0]))

# someMax = heapq.heappop(maxHeap)
# someMin = heapq.heappop(minHeap)
# print(f"Word with max tf-idf: {someMax[1]}, tf-idf: {-someMax[0]}")
# print(f"Word with min tf-idf: {someMin[1]}, tf-idf: {someMin[0]}")

start = time.time()
res = qp.search("اخبار", 10)
end = time.time()
print_in_red(f"normal cosine search spent time: {end - start}, result is:")
print_results(res)

start = time.time()
res2 = qp2.search("لیگ برتر آسیا", 10)
end = time.time()
print_in_red(f"\npositional + normal cosine search spent time: {end - start}, result is:")
print_results(res2)

start = time.time()
res3 = qp3.search("المصری الیوم الاهلی", 10)
end = time.time()
print_in_red(f"\nchamp list + normal cosine search spent time: {end - start}, result is:")
print_results(res3)
