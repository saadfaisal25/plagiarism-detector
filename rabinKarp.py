def hash(word):
    if len(word) >= 3:
        hash = ord(word[0]) * ord(word[-1]) * ord(word[len(word)//2]) * len(word)
    else:
        hash = ord(word[0]) * ord(word[-1]) * len(word)
    return hash

def getListHash(words):
    words = ' '.join(words).split()
    listHash = 0
    for word in words:
        listHash += hash(word)

    return listHash

def getRKSim(data1, data2):
    data2 = ' '.join(data2).split()

    count = 0
    for data in data1:
        pat = data.split()
        patlen = len(pat)

        patHash = getListHash(pat)
        textHash = getListHash(data2[:patlen])

        for i in range(len(data2) - patlen + 1):
            if patHash == textHash:

                valid = True
                for j in range(patlen):
                    if pat[j] != data2[i+j]:
                        valid = False
                        break
                    
                if valid:
                    count += 1
            
            if i < len(data2) - patlen:
                textHash = textHash - hash(data2[i]) + hash(data2[i+patlen])

    sim = count / len(data1) * 100
    return sim