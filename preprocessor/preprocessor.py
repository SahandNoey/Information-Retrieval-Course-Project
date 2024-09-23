# normalizer = Normalizer()
# tokenizer = Tokenizer()
# lem = Lemmatizer()
# stem = Stemmer()

# def preprocess(contents):
#     preprocessed_docs = {}
#     for content in contents:
#         # normalizing
#         normalized_content = normalizer.normalize(content)
#         content_tokens = tokenizer.tokenize(normalized_content)
        
#         tokens = []
#         for token in content_tokens:
#             # token = stemmer.convert_to_stem(token)
#             token = stem.stem(token)
#             token = lem.lemmatize(token, 'V')
#             tokens.append(token)
        
#         # tokens of each doc
#         preprocessed_docs[doc_id] = tokens
       
#     return preprocessed_docs


# def preprocess_query(query:str):
#     query = normalizer.normalize(query)
#     query = tokenizer.tokenize(query)
#     tokens = []
#     for token in query:
#         token = stem.stem(token)
#         token = lem.lemmatize(token, 'V')
#         tokens.append(token)
    
#     return tokens
from preprocessor.normalizer import Normalizer
from preprocessor.tokenizer import Tokenizer
from hazm import Lemmatizer, Stemmer

normalizer = Normalizer()
tokenizer = Tokenizer()
lem = Lemmatizer()
stem = Stemmer()

def preprocess(contents):
    # normalizing
    normalized_content = normalizer.normalize(contents)
    content_tokens = tokenizer.tokenize(normalized_content)
    
    tokens = []
    for token in content_tokens:
        # token = stemmer.convert_to_stem(token)
        token = stem.stem(token)
        token = lem.lemmatize(token, 'V')
        tokens.append(token)
       
    return tokens


def preprocess_query(query:str):
    query = normalizer.normalize(query)
    query = tokenizer.tokenize(query)
    tokens = []
    for token in query:
        token = stem.stem(token)
        token = lem.lemmatize(token, 'V')
        tokens.append(token)
    
    return tokens