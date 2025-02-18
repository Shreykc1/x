from collections import defaultdict

def incidence_matrix(docs):
    docs_data = {doc_id: doc for doc_id, doc in enumerate(docs)}
    length = len(docs)
    incidence = {"==Token==": [f"DocID{doc_id}" for doc_id in range(length)]}
    all_tokens = set()
    for data in docs_data.values():
        all_tokens.update(data.split())
    for token in all_tokens:
        if token:
            incidence[token] = [1 if token in docs_data[i].split() else 0 for i in range(length)]
    return incidence

def query_incidence(incidence, query):
    def process_query(tokens):
        if not tokens: return None
        and_results = []
        i = 0
        while i < len(tokens):
            if tokens[i] == "AND":
                prev_result = and_results.pop()
                next_result = incidence[tokens[i + 1]]
                and_results.append([a & b for a, b in zip(prev_result, next_result)])
                i += 2
            else:
                if tokens[i] != "OR":
                    and_results.append(incidence[tokens[i]])
                i += 1
        if len(and_results) == 1: return and_results[0]
        return [any(results) for results in zip(*and_results)]
    return process_query(query.split())

documents = [
    "Quick brown fox jumps over lazy dog",
    "A fast fox and a sleepy dog were in the yard",
    "Dogs are very loyal animals and love their owners"
]

incidence = incidence_matrix(documents)
# [print(row) for row in incidence]
[print(a,b) for a,b in incidence.items()]
query = "Quick OR loyal"
result = query_incidence(incidence, query)
print(result)
