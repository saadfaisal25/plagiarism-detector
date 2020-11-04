import string
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

# remove punctuation (. , "" '' :   etc.)
def remPunc(text):
    punc = set(string.punctuation)
    text = ''.join([word for word in text if word not in punc])
    return text

# remove stop words, such as 'the', 'a', 'to', 'for', etc. and return string
def remStopWords(text):
    stop = set(stopwords.words("english"))

    text = ' '.join([word for word in text.split() if word not in stop])
    return text

# make everything lowercase and return string
def makeLower(text):
    text = text.lower()
    return text

# get only root words from all words
def lemmatize():
    pass

# get text from a txt file and return a processed list of text using the helper functions above
def processTXT(filename):
    with open(filename, 'r') as f:
        data = f.read().replace('\n', '')

    data = data.split('.')
    data.remove('')
    
    data = list(map(remPunc, data))
    data = list(map(makeLower, data))
    data = list(map(remStopWords, data))

    return data

#print(processTXT("testfile1.txt"))