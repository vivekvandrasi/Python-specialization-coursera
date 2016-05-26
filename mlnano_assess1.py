
def count_words(text,num):
    counts=dict();
    textarr = text.split()
    for word in textarr:
        counts[word] = counts.get(word,0) + 1
    counts_sort = sorted(counts.items(), key=lambda element: (-element[1],element[0]))
    return counts_sort[:3]
    
print count_words("betty bought a bit of butter but the butter was bitter",3)
