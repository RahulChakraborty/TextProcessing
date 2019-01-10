import  nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import RegexpTokenizer
import string

# Tokenizing words and sentences

data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
stopWords = set(stopwords.words('english'))
words = word_tokenize(data)
wordsFiltered = []
phrases = sent_tokenize(data)

# StopWords

print('Words:::    ',words)
print('Phrases :::: ',phrases)

for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)

print('wordsFiltered:::: ' ,wordsFiltered)

tokenizer = RegexpTokenizer(r'\w+')
print tokenizer.tokenize('Eighty-seven miles to go, yet.  Onward!')

text = '''It is a blue, small, and extraordinary ball. Like no other'''
tokens = [word for sent in sent_tokenize(text) for word in word_tokenize(sent)]
print filter(lambda word: word not in ',-.', tokens)


#Stemming

ps = PorterStemmer()

sentence = "ntflx"
words = word_tokenize(sentence)

for word in words:
    print(word + ":" + ps.stem(word))

#POS Tagger

document = 'Today the Netherlands celebrates King\'s Day. To honor this tradition, the Dutch embassy in San Francisco invited me to'
sentences = nltk.sent_tokenize(document)

data = []
for sent in sentences:
    data = data + nltk.pos_tag(nltk.word_tokenize(sent))

for word in data:
    if 'NNP' in word[1]:
        print(word)