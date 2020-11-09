import nltk
from nltk.corpus import stopwords 
nltk.download('stopwords') # downloads stopwords on your system, can be removed if you already have it

# remove all punctuation
def remPunc(text):
    # converting to a set for O(1) lookup
    punc = set("!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~'\n")
    text = ''.join([word for word in text if word not in punc])
    return text

# remove stop words, such as 'the', 'a', 'to', 'for', etc. and return string
def remStopWords(text):
    stop = set(stopwords.words("english"))
    text = ' '.join([word for word in text.split() if word not in stop])
    return text

# make everything lowercase and return string
def makeLower(text):
    return text.lower()

# removes all single letters, numbers, and empty elements
def filterText(text):
    letters = set("abcdefghijklmnopqrstuvwxyz")
    nums = set("1234567890")

    # uses list comprehensions to remove the elements
    text = [x for x in text if x not in letters]
    text = [x for x in text if x not in nums]
    text = [x for x in text if x != '']

    return text

# get only root words from all words, to be implemented in the future
def lemmatize():
    pass

# convert all words to the stem of the word, to be implemented in the future
def stem():
    pass

# get text from a txt file and return a processed list of text using the helper functions above
def processTXT(filename):
    with open(filename, 'r') as f:
        data = f.read().replace('\n', '')

    data = makeLower(data)
    data = data.strip().split('.')
     
    # uses the map function to apply the function to each item in the list, which is faster and more readable than a for loop
    data = list(map(remStopWords, data))
    data = list(map(remPunc, data))
    data = list(map(remStopWords, data))
    data = filterText(data)

    return data