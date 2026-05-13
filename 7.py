import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag

from sklearn.feature_extraction.text import TfidfVectorizer

# Download required resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('wordnet')

# Sample document
text = "Natural Language Processing is very interesting and useful for text analytics."

print("Original Text:\n")
print(text)

# 1. Tokenization
tokens = word_tokenize(text)

print("\nTokens:\n")
print(tokens)

# 2. POS Tagging
pos = pos_tag(tokens)

print("\nPOS Tags:\n")
print(pos)

# 3. Stopword Removal
stop_words = set(stopwords.words('english'))

filtered_words = [
    word for word in tokens
    if word.lower() not in stop_words
]

print("\nAfter Stopword Removal:\n")
print(filtered_words)

# 4. Stemming
stemmer = PorterStemmer()

stemmed_words = [stemmer.stem(word) for word in filtered_words]

print("\nStemmed Words:\n")
print(stemmed_words)

# 5. Lemmatization
lemmatizer = WordNetLemmatizer()

lemmatized_words = [
    lemmatizer.lemmatize(word)
    for word in filtered_words
]

print("\nLemmatized Words:\n")
print(lemmatized_words)

# Documents for TF-IDF
documents = [
    "Natural Language Processing is useful",
    "Text analytics uses NLP",
    "NLP is interesting"
]

# TF-IDF
vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

print("\nTF-IDF Feature Names:\n")
print(vectorizer.get_feature_names_out())

print("\nTF-IDF Matrix:\n")
print(tfidf_matrix.toarray())