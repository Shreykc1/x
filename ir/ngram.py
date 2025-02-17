def ngrams(sentence, n):
    result = []
    words = [f"${word}$" for word in sentence.split(" ")]
    for word in words:
        for i in range(len(word)-n+1):
            result.append(word[i:i+n])
    return result

n = 4
sentence = "hello world"
print(ngrams(sentence, n))
