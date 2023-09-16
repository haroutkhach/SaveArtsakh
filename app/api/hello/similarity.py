from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Preprocess the text (replace with your actual news articles)
article1 = "Separatist parliament in Azerbaijan's breakaway Nagorno-Karabakh region elects new president"
article2 = "Karabakh Separatist Leader Resigns Amid Deepening Blockade Crisis"

# Tokenize, remove stopwords, and convert to lowercase
def preprocess_text(text):
    # Implement your preprocessing logic here
    # You can use NLTK or spaCy for more advanced preprocessing
    # For simplicity, we'll split words by spaces and convert to lowercase
    return text.lower().split()

# Combine the preprocessed text into a list
corpus = [article1, article2]

# TF-IDF vectorization
tfidf_vectorizer = TfidfVectorizer(tokenizer=preprocess_text)
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

# Calculate cosine similarity
similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

# The similarity value is in similarity_matrix[0][1]
similarity = similarity_matrix[0][1]

# Set a similarity threshold (e.g., 0.95)
similarity_threshold = 0.05

# Check if the articles have at least 95% similarity
if similarity >= similarity_threshold:
    print("The articles are similar.")
else:
    print("The articles are not similar.")
