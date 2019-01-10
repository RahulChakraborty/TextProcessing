from fuzzywuzzy import process
from pprint import pprint  # pretty-printer

documents = ["SEAMLSS GYROLOCOPRINCE 8002561020 NY",
             "AMC NEWPORT CTR #2184 JERSEY CITY NJ",
             "NETFLIX COM CA",
             "MIELLIE DENTAL P C NEW YORK NY",
             "TAXI-NEWARK.COM 844-808-2944 NY",
             "OFFER 10 PROMOTIONAL APR ENDED 03/01/18",
             "L.A GOURMET LONG ISLAND C NY",
             "L.A GOURMET LONG ISLAND C NY",
             "KAMLESH INC LONG ISLAND C NY",
             "WALGREENS #11774 NORTH BERGEN NJ",
             "HOME DEPOT GA ATLANTA",
             "THE HOME DEPOT GEORGIA"]

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

new_doc = "THE HOME DEPT"  # type: str

match= process.extract(new_doc,texts,limit=500)

for item in match:
        print "Text :: ", item[0]
        print  "Score ::", item[1]
