from fuzzywuzzy import process
from gensim import corpora, models, similarities
from pprint import pprint  # pretty-printer

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

documents = ["SEAMLSS GYROLOCOPRINCE 8002561020 NY",
             "AMC NEWPORT CTR #2184 JERSEY CITY NJ",
             "NETFLIX COM CA",
             "MIELLIE DENTAL P C NEW YORK NY",
             "TAXI-NEWARK.COM 844-808-2944 NY",
             "OFFER 10 PROMOTIONAL APR ENDED 03/01/18",
             "L.A GOURMET LONG ISLAND C NY",
             "L.A GOURMET LONG ISLAND C NY",
             "KAMLESH INC LONG ISLAND C NY",
             "WALGREENS #11774 NORTH BERGEN NJ"]

# remove common words and tokenize
stoplist = set('# * . - '.split())
texts = [[word for word in document.lower().split()
          if word not in stoplist]
         for document in documents]

#tokens = [word for sent in sent_tokenize(text) for word in word_tokenize(sent) for document in documents]
print 'StopList Removed', texts

# frequency = defaultdict(int)
# for text in texts:
#     for token in text:
#         frequency[token] += 1
#
# texts = [[token for token in text if frequency[token] > 1]
#            for text in texts]


pprint(texts)

dictionary = corpora.Dictionary(texts)
# dictionary.save('/tmp/deerwester.dict')

print(dictionary)

print(dictionary.token2id)

corpus = [dictionary.doc2bow(text) for text in texts]

tfidf = models.TfidfModel(corpus)

corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
    print(doc)

lsi = models.LsiModel(corpus_tfidf, id2word=dictionary)
corpus_lsi = lsi[corpus_tfidf]

new_doc = "netflix"  # type: str

result = new_doc.lower().split()

print "result", result

vec_bow = dictionary.doc2bow(result)

print "vec_bow", vec_bow
vec_lsi = lsi[vec_bow]
print "vec_lsi", vec_lsi

index = similarities.MatrixSimilarity(corpus_lsi)



print "Matrix Similarity Index ", index
sims = index[vec_lsi]

print("sims ", sims)

sortedSims = sorted(enumerate(sims), key=lambda item: -item[1])

print(sortedSims)

