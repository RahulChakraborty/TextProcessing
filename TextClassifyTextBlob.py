from textblob import TextBlob
from textblob import Word
from textblob.classifiers import NaiveBayesClassifier

# blob = TextBlob("I have a lovely bunch of coconuts.")
# for words,pos in blob.tags:
#     print words, pos
#
# w= Word('running')
# print w.lemmatize()

#Text Classify

train = [
      ('I love this sandwich.', 'pos'),
      ('this is an amazing place!', 'pos'),
      ('I feel very good about these beers.', 'pos'),
      ('this is my best work.', 'pos'),
      ("what an awesome view", 'pos'),
      ('I do not like this restaurant', 'neg'),
      ('I am tired of this stuff.', 'neg'),
      ("I can't deal with this", 'neg'),
      ('he is my sworn enemy!', 'neg'),
      ('my boss is horrible.', 'neg')
  ]

test = [
      ('the beer was good.', 'pos'),
      ('I do not enjoy my job', 'neg'),
      ("I ain't feeling dandy today.", 'neg'),
      ("I feel amazing!", 'pos'),
      ('Gary is a friend of mine.', 'pos'),
      ("I can't believe I'm doing this.", 'neg')
  ]

cl = NaiveBayesClassifier(train)
print cl.classify("This is an amazing library!")
print cl.accuracy(test)

print cl.show_informative_features(5)



prob_dist = cl.prob_classify("This one's a doozy.")
print

prob_dist.max()

