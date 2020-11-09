from math import sqrt

# returns a dictionary of all unique words in both data sets and the occurrences of each word for each data set
# words[word] = [wordcount in data1, wordcount in data2]
def getWordCounts(data1, data2):
    words = {}
    # add all words from data1
    for i in data1:
        if i in words:
            words[i][0] += 1
        else:
            words[i] = [1, 0]

    # add all words from data2
    for i in data2:
        if i in words:
            words[i][1] += 1
        else:
            words[i] = [0, 1]

    return words

# calculates and returns the dot product of 2 vectors with variable dimensions
def dotProduct(vec1, vec2):
    dotProd = 0
    # for every dimension in the vectors, calculate the dot product of that dimension and add it to dotProd, which will give the total dot product
    for i in range(len(vec1)):
        dotProd += (vec1[i] * vec2[i])
    
    return dotProd

# calculates and returns the magnitude of a vector using the dotProduct() function
# ||A|| = sqrt(A * A)
def magnitude(vec1):
    return sqrt(dotProduct(vec1, vec1))

def getCosineSim(data1, data2):
    data1 = ' '.join(data1).split()
    data2 = ' '.join(data2).split()
    words = getWordCounts(data1, data2)
    
    # splits the words dictionary into 2 separate lists (vectors) of the counts of each word
    vec1 = []
    vec2 = []
    for i in words:
        vec1.append(words[i][0])
        vec2.append(words[i][1])

    # using the cosine similarity formula to calculate the cosine similarity between the two vectors
    sim = ( dotProduct(vec1, vec2) / (magnitude(vec1) * magnitude(vec2)) ) * 100
    return sim