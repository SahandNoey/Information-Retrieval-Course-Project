# Persian News Article Information Retrieval System

Implemented **Information Retrieval (IR)** system on a dataset of Persian news articles. You can find the [Test Data here](https://github.com/SahandNoey/Information-Retrieval-Course-Project/blob/master/IR_data_news_5k%202.json).

For each query, the system retrieves and prints **only the first document ID** using three distinct index types:

1. **Standard Index**: Uses **TF-IDF** and **cosine similarity** to search across all documents.
2. **Positional Index**: Prioritizes documents containing consecutive terms from the query. If none are found, it behaves like the Standard Index.
3. **Champion List Index**: Focuses on documents where the query term occurs at least five times, providing faster search results, though it may miss some relevant documents.

## System Highlights

### 1. Text Preprocessing
The preprocessing pipeline ensures that the text is prepared for efficient retrieval by performing:
- **Lemmatization**: Converts different word forms and verb tenses into their root forms.
- **Normalization**: Ensures consistency by unifying case and removing special characters.
- **Tokenization**: Splits the text into individual words (tokens) for further analysis.

### 2. Inverted Index Creation
An **Inverted Index** was constructed to facilitate fast document retrieval. This index maps each word to a list of the documents (articles) in which it appears.

### 3. Positional Index Support
A **Positional Index** is also included, which tracks the position of terms in documents. This index enhances the system’s ability to process phrase queries by identifying documents where specific terms appear in sequence.

### 4. Phrase Query Handling
The system can process phrase queries, leveraging the **Positional Index** to find documents that contain the exact phrase by verifying the term positions.

### 5. Relevance Calculation
To rank documents based on their relevance to the query:
- **TF-IDF (Term Frequency-Inverse Document Frequency)** is used to assign importance to terms within both individual documents and the overall collection.
- **Cosine Similarity** measures how closely each document matches the query.

### 6. Champion List for Efficient Search
A **Champion List** technique is employed to enhance retrieval speed. By focusing on a limited subset of highly relevant documents (those where terms occur at least five times), the system can deliver faster results, though some related documents might not be retrieved.

---

This version keeps all the key details but organizes and rephrases them to make the structure and flow a bit different from the original. Let me know if you'd like any further adjustments!
