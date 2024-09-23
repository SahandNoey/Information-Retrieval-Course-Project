# Information Retrieval System

Implemented a basic Information Retrieval (IR) system on a dataset of  Persian news articles.
[Test Data](https://github.com/SahandNoey/Information-Retrieval-Course-Project/blob/master/IR_data_news_5k%202.json) is uploaded.

For each query, we print **only the first retrieved document ID** by three type of indices:
- **Normal Index** that uses TF-IDF and cosine similarity on the whole documents to search on.
- **Positional Index** that tries to find documents that has at least some of the terms placed consecutively, and if doesn't find any document with this property, it acts just like Normal Index.
- **Champion List Index** that searchs on documents that have at least 5 occurrence of the term given. As a result, it retrieves documents faster but it may not retrieve all the related documents.


## Features

### 1. Preprocessing
The preprocessing phase included several key steps:
- **Lemmatization**: Converted different tenses of verbs and variations of words into their root form.
- **Normalization**: Standardized the text by converting all characters to a uniform case and removing any special characters.
- **Tokenization**: Split the text into individual tokens (words/terms) for analysis.

### 2. Inverted Index
An **Inverted Index** was built over the dataset to allow for efficient document retrieval. Each token is mapped to the list of documents (news articles) where it appears.

### 3. Positional Index
The system also supports a **Positional Index**, where both the term and its position within the document are stored. This allows for more advanced query retrieval techniques such as phrase queries.

### 4. Positional Query Retrieval
Implemented **Positional Query Retrieval**, where the system can handle phrase queries and return documents where the exact phrase appears by checking word positions within documents.

### 5. TF-IDF & Cosine Similarity
For calculating the relevance of documents to a given query:
- **TF-IDF (Term Frequency-Inverse Document Frequency)** was used to weigh terms by their importance in both the document and the overall dataset.
- **Cosine Similarity** was implemented to measure the similarity between the query and each document.

### 6. Champions List
To optimize retrieval, **Champions Lists** were implemented. This technique calculates similarity scores for a limited set of the most relevant documents (top-K documents), improving retrieval speed.
