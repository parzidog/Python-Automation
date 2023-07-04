from speech_recognition import Recognizer, AudioFile
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

recognizer = Recognizer()

with AudioFile("chile.wav") as af:
    audio = recognizer.record(af)

text = recognizer.recognize_google(audio)

# nltk.download("vader_lexicon")

analyzer = SentimentIntensityAnalyzer()
scores = analyzer.polarity_scores(text)


if scores["compound"] > 0:
    print("Positive Speech!")
else:
    print("Negative Speech!")
