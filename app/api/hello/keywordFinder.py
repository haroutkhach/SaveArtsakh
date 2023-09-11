import nltk
import networkx as nx
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

# nltk.download('punkt')
# nltk.download('stopwords')

def extractKeywords(news_article, num_keywords=1):
    # Tokenize the text into sentences and words
    sentences = sent_tokenize(news_article)
    words = [word_tokenize(sentence.lower()) for sentence in sentences]

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    filtered_words = [[word for word in sentence if word.isalnum() and word not in stop_words] for sentence in words]

    # Create a graph for TextRank
    graph = nx.Graph()

    # Add nodes (words) to the graph
    for sentence in filtered_words:
        graph.add_nodes_from(sentence)

    # Add edges (co-occurrence) to the graph
    for sentence in filtered_words:
        for word1 in sentence:
            for word2 in sentence:
                if word1 != word2:
                    graph.add_edge(word1, word2)

    # Calculate TextRank scores
    scores = nx.pagerank(graph)

    # Sort words by their TextRank scores
    sorted_keywords = sorted(scores, key=scores.get, reverse=True)

    # Get the top N keywords
    top_keywords = sorted_keywords[:num_keywords]

    return top_keywords

