

def index_words(text):
    results = []
    if text:
        results.append(0)
    for index, word in enumerate(text):
        if word == ' ':
            results.append(index + 1)
    return results

def index_words_iter(text):
    if text:
        yield 0
    for index, word in enumerate(text):
        if word == ' ':
            yield index + 1




text = 'Best programming language in the world'
results = index_words(text)
results_iter = list(index_words_iter(text))
print(results)
print(results_iter)
