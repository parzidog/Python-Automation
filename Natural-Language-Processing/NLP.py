from nltk.stem import WordNetLemmatizer
import nltk

# nltk.download("wordnet")
# nltk.download("punkt")

x = "was"
y = "is"

lemmatizer = WordNetLemmatizer()

lemma1 = lemmatizer.lemmatize(x, "v")
lemma2 = lemmatizer.lemmatize(y, "v")

print(lemma1 + " " + lemma2)
