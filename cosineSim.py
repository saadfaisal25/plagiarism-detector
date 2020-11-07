from math import sqrt

def getWordCounts(data1, data2):
    words = {}
    for i in data1:
        if i in words:
            words[i][0] += 1
        else:
            words[i] = [1, 0]

    for i in data2:
        if i in words:
            words[i][1] += 1
        else:
            words[i] = [0, 1]

    return words

def dotProduct(vec1, vec2):
    dotProd = 0
    for i in range(len(vec1)):
        dotProd += (vec1[i] * vec2[i])
    
    return dotProd

def magnitude(vec1):
    return sqrt(dotProduct(vec1, vec1))

def getCosineSim(data1, data2):
    data1 = ' '.join(data1).split()
    data2 = ' '.join(data2).split()
    words = getWordCounts(data1, data2)
    
    vec1 = []
    vec2 = []

    for i in words:
        vec1.append(words[i][0])
        vec2.append(words[i][1])

    sim = ( dotProduct(vec1, vec2) / (magnitude(vec1) * magnitude(vec2)) ) * 100
    return sim