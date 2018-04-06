import random
import math ## use ceiling function

from helper import read_corpus, splitToSentences, get_substring, remove_char

#min sample size is smaller than size of corpus
def get_text_sample(corpus_folder, min_sample_size):

    corpus_docs = read_corpus(corpus_folder)

    file = open("samples1.txt","w")

    for i in corpus_docs:

        sentences = splitToSentences(i);
        corpus_sentences = []
        for sentence in sentences:
            corpus_sentences.append(remove_char(sentence, '\n'))

        text_size = len(corpus_sentences)
        sample_size = math.ceil(text_size * .05)

        if(sample_size < min_sample_size):
            sample_size = min_sample_size

        random_position = random.randint(0,text_size)

        sample_text = ""

        if(random_position + sample_size < text_size):
            sample_text = get_substring(corpus_sentences, random_position, random_position+sample_size)
        else:
            sample_text = get_substring(corpus_sentences, random_position, text_size)
            sample_text += get_substring(corpus_sentences, 0, sample_size - (text_size - random_position))

        file.write(sample_text)
        file.write('\n\n')

    file.close()

get_text_sample('interviewer_removed', 10)


'''
get length of text (in terms of sentences)
get 5% of sentence, or some threshold

get random number for position (make sure it's enough for size)

output text and add commas to a text file


size 10
min = 2
loc = 5
5+2 = 7 +1 <= 10
'''
