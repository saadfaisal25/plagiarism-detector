# loops through all sentences in data1, and returns the number of common sentences between data1 and data2
def senMatch(data1, data2):
    count = 0
    for i in data1:
        if i in data2:
            count += 1

    return count

def getSenSim(data1, data2):
    # calculates the ratio of common sentences to the number of sentences
    sim = senMatch(data1, data2) / len(data1) * 100
    return sim