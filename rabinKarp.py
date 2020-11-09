# this function returns a hash value for a given word in O(1) using the first and last characters of the word and its length
def hash(word):
    if len(word) >= 3:
        # uses the middle character to hash for longer words to reduce the chance of a false positive when checking for hashes
        hash = ord(word[0]) * ord(word[-1]) * ord(word[len(word)//2]) * len(word)
    else:
        hash = ord(word[0]) * ord(word[-1]) * len(word)
    return hash

# returns the total hash value of a list of words
def getListHash(words):
    words = ' '.join(words).split()
    listHash = 0
    for word in words:
        listHash += hash(word)

    return listHash

def getRKSim(data1, data2):
    # break the list of sentences into separate words
    data2 = ' '.join(data2).split()

    count = 0
    for data in data1:
        pat = data.split()
        patlen = len(pat)

        # assigns the hash value of the pattern and hash value of the first sequence in data2 
        patHash = getListHash(pat)
        textHash = getListHash(data2[:patlen])

        # loop through data2 and look for matching hash values
        for i in range(len(data2) - patlen + 1):
            if patHash == textHash:

                valid = True
                # if hash values match, check if the sequence is equal to the pattern by checking for a non-matching word
                for j in range(patlen):
                    if pat[j] != data2[i+j]:
                        valid = False
                        break

                # if all the words match, increment count     
                if valid:
                    count += 1
            
            # if this isn't the last iteration of the loop, update textHash by subtracting the hash of the last word and adding the hash of the next word
            if i < len(data2) - patlen:
                textHash = textHash - hash(data2[i]) + hash(data2[i+patlen])

    # return the ratio of matches to the length of data1
    sim = count / len(data1) * 100
    return sim