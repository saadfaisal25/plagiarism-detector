# returns a list of all unique words from the data
def getWordCount(data):
    words = {}
    for i in data:
        if i not in words:
            words[i] = 1

    return words

# returns a list of words that are in both of the given dictionaries
def intersection(words1, words2):
    intersect = []
    for i in words1:
        if i in words2:
            intersect.append(i)

    return intersect

def getJaccardSim(data1, data2):
    words1 = getWordCount(' '.join(data1).split())
    words2 = getWordCount(' '.join(data2).split())
    words = list(words1.keys()) + list(words2.keys())

    lenInt = len(intersection(words1, words2))
    lenUnion = len(words) - lenInt

    # using the Jaccard index formula to calculate similarity ratio, then converting value to a percentage
    sim = ( lenInt / lenUnion ) * 100
    return sim