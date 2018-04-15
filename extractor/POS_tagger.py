#!/usr/bin/env python
import os, requests, re
import csv
import pandas as pd
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.parse.stanford import StanfordParser
from nltk.parse.stanford import StanfordDependencyParser
from nltk.tag.stanford import StanfordPOSTagger
from text_locations import transcripts


java_path = "usr/bin/java"
os.environ['JAVAHOME'] = java_path
current_dir = os.path.dirname(os.path.abspath(__file__))

stanford_parser_dir = current_dir + '/stanford_NLP/stanford-postagger-full-2015-04-20'
path_to_model = stanford_parser_dir + "/models/english-bidirectional-distsim.tagger"
path_to_jar = stanford_parser_dir + "/stanford-postagger.jar"
tagger=StanfordPOSTagger(path_to_model, path_to_jar)

POS_TAGS = ["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS", "MD", "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRP$", "RB", "RBR", "RBS", "RP", "SYM", "TO", "UH", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "WDT", "WP", "WP$", "WRB"] 

# Save document from dataframe to CSV
def save_csv_file(document_df, database_location):
    cols = list(document_df.columns.values)
    cols.insert(0, cols.pop())
    cols.insert(0, cols.pop())

    document_df = document_df[cols]
    with open(database_location , 'w', newline='', encoding='utf-8') as csvFile:
        document_df.to_csv(csvFile, sep=',', index=False)

def parse_sentence(sentence):
    sentence = sentence.strip('\n')
    sentence = sentence.strip('\t')
    tagsInSentence = set()
    sentence_data = {}
    sentence_data["sentence"] = sentence
    # Setting higher memory limit for long sentences
    tagger.java_options='-mx4096m'
    for tags in POS_TAGS:
        sentence_data[tags] = []
    for word, tag in tagger.tag(sentence.split()):
        if tag in sentence_data:
            sentence_data[tag].append(word)
            tagsInSentence.add(tag)

    sentence_data["tags"] = tagsInSentence
    
    return  sentence_data         

def extract_sentences(page_content):
    this_text_data = []
    sentences_to_parse = sent_tokenize(page_content)
    for sentence in sentences_to_parse:
        new_data_row = parse_sentence(sentence)
        this_text_data.append(new_data_row)
    document_df = pd.DataFrame(this_text_data)

    return document_df


def get_text_from_dir(location):
    with open(location, 'r') as local_file:
        file_content = local_file.read()
        return file_content


def run_prog(dictionary_array):
    print(dictionary_array)
    for dictionary in dictionary_array:
        print ('Processing ' +  dictionary['location'] )
        text = get_text_from_dir(dictionary['location'])
        sentences_data = extract_sentences(text)

        save_csv_file(sentences_data, 'POS_output' + dictionary['results'])


run_prog(transcripts)
