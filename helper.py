import nltk
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string # allows us to define punctutation to remove
from nltk.corpus import wordnet as wn # allows us to access pos types
from nltk.corpus import PlaintextCorpusReader # to read documents

porter_stemmer = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()

# Tokenize text string by word
def splitToWords(text):
    return WhitespaceTokenizer().tokenize(text)

# Tokenize text string by sentence
def splitToSentences(text):
    return sent_tokenize(text)

# change words to lowercase in a list
def convertToLowercase(text):
    return [word.lower() for word in text]

# remove punctuation from the string
def removePunctuation(text):
    exclude = set(string.punctuation)
    keep_these_punct = ['/', '%', '-']
    for punct in keep_these_punct:
        exclude.remove(punct)
    converted_text = ''.join(ch for ch in text if ch not in exclude)
    return converted_text

# Apply stemming to words in a list
def stemWords(words):
    return [porter_stemmer.stem(word) for word in words]

# Apply lemmatization to words in a list
def lemmatizeWords(words):
    convert_words = []
    words_with_pos = nltk.pos_tag(words)
    for pos_tag in words_with_pos:
        simplify_pos = penn_to_wn(pos_tag[1])
        if(simplify_pos == None):
            convert_words.append(wordnet_lemmatizer.lemmatize(pos_tag[0]))
        else:
            convert_words.append(wordnet_lemmatizer.lemmatize(pos_tag[0], simplify_pos))
    #print(words == convert_words)
    return convert_words

# Apply part of speech tagging to a list of words
def partOfSpeechTag(words):
    return nltk.pos_tag(words)


stopset = set(nltk.corpus.stopwords.words('english'))
extra_stopwords = ["like", "it’s", "uh", "going", "that’s", "think", "actually", "kind", "…", "know", "come", "u", "really"]
for word in extra_stopwords:
    stopset.add(word)

# removes stop words from a list of words
def removeStopWords(text):
    return [word for word in text if word not in stopset]

# checks if a word isnt in the stopset
def notStopWord(word):
    return word not in stopset


## the following functions check what a tag is
def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']


def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']


def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']


def penn_to_wn(tag):
    if is_adjective(tag):
        return wn.ADJ
    elif is_noun(tag):
        return wn.NOUN
    elif is_adverb(tag):
        return wn.ADV
    elif is_verb(tag):
        return wn.VERB
    return None

# takes in list of words, returns list of bigrams
def create_ngrams(sentence, n):
    if(n == 1):
        return splitToWords(sentence)
    if(n == 2):
        return list(nltk.bigrams(sentence))
    if(n == 3):
        return list(nltk.trigrams(sentence))
    else:
        print("ngram length not supported as of now")
        return sentence


def read_corpus(corpus_root):
    corpus = PlaintextCorpusReader(corpus_root, '.*')

    corpus_titles = []
    corpus_docs = []

    for titles in corpus.fileids():
        corpus_titles.append(titles)
        corpus_docs.append(corpus.raw(titles))

    return corpus_docs

def get_substring(text, start_position, end_position):
    substring = ""
    for i in range(start_position, end_position):
        substring += str(text[i])
        substring += " "
    return substring

def remove_char(text, character):
    converted_text = ''.join(ch for ch in text if ch != character)
    return converted_text
