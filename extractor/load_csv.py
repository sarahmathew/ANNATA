import pandas as pd
from text_locations import transcripts

def generateDataframe(file):
    df = pd.read_csv(file,encoding='utf-8')
    print(df)

def run_prog(dictionary_array):
    for dictionary in dictionary_array: 
        # Load Passive - Active CSV files
        # generateDataframe('PA_output' + dictionary['results'])

        # Load Part of Speech CSV files
        generateDataframe('POS_output' + dictionary['results'])

run_prog(transcripts)
