def senMatch(data1, data2):
    count = 0
    for i in data1:
        if i in data2:
            count += 1

    return count

def getSenSim(data1, data2):
    sim = senMatch(data1, data2) / len(data1) * 100
    return sim