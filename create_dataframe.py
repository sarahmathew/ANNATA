import pandas
from helper import splitToSentences

def import_data(file_name):
    data = pandas.DataFrame(columns=['id', 'sentence', 'interview_id'])

    with open(file_name) as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content if x != '\n']
        #print(len(content))
        interview_id = 1
        sentence_id = 1
        for sample in content:
            sentences = splitToSentences(sample);
            print(len(sentences))
            for sentence in sentences:
                row = [sentence_id, sentence, interview_id]
                data.loc[len(data)] = row
                sentence_id += 1
            interview_id += 1
    return data


corpus_features = import_data('samples.txt')
