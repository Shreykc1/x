from collections import defaultdict

doc1="new home sales rise top forecasts"
doc2="home sales rise in july"
doc3="increase in home sales in july"
doc4="july new homes sales rise"

inverted_index = defaultdict(set)
docs=[doc1,doc2,doc3,doc4]
for doc in docs:
    for word in doc.split():
        inverted_index[word].add(docs.index(doc)+1)

for word, posting_list in inverted_index.items():
    print(f"{word}:{posting_list}")
