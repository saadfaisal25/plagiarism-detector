import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

# remove punctuation (. , "" '' :   etc.)
def remPunc(text):
    punc = "!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~'\n"
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

# convert all words to the stem of the word
def stem():
    pass

# get text from a txt file and return a processed list of text using the helper functions above
def processTXT(filename):
    with open(filename, 'r') as f:
        data = f.read().replace('\n', '')

    data = data.strip().split('.')
    data.remove('')
    
    data = list(map(makeLower, data))
    data = list(map(remStopWords, data))
    data = list(map(remPunc, data))
    data = list(map(remStopWords, data))

    return data