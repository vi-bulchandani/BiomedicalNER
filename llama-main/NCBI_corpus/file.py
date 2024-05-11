import re
from datasets import load_dataset
import tqdm
def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


dataset = load_dataset("ncbi_disease")
test=dataset["test"]



#
# with open('NCBI_corpus_testing.txt', 'r') as file:
#     data = file.read().replace('\n', '')
for row in test:
    sentence = ' '.join(row['tokens'])
    print(sentence)

# print(clean_text)
