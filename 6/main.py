from collections import defaultdict, Counter
import json
import os
import argparse
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist


def most_frequent_words(data, year, num, stop, extra_stops):
  all_words = []

  if '-' in year:
    start, end = year.split('-')
  else:
    start = year
    end = int(year) + 1

  for year in range(int(start), int(end)):  
    titles = list(set([title['title'] for title in data if title['year'] == str(year)]))
  
    words = word_tokenize('\n'.join(titles))
  
    if stop:
      if extra_stops:
        extras = ['museum', 'web', 'museums', "'s"]
      else:
        extras = []
      words = [w for w in words if w.lower() not in stopwords.words(
          'english') + list(string.punctuation) + extras]
    
    all_words += words

  fdist = FreqDist(all_words)

  return fdist.most_common(num)


def get_docs(data, year, num):
  docs = []

  if '-' in year:
    start, end = year.split('-')
  else:
    start = year
    end = int(year) + 1

  for year in range(int(start), int(end)):  
    titles = list(set([title['title'] for title in data if title['year'] == str(year)])) 
    docs += titles

  return docs


def use_spacy(docs):
  # python main.py -d 2001-2005
  # prints a list of n most common words from the 5 years period and part-of-speech tag e.g. verb, adj etc
  # see https://spacy.io/usage/linguistic-features#pos-tagging
  # for more info
  import spacy
  nlp = spacy.load('en')

  pos_counts = defaultdict(Counter)
  docs = " ".join(docs)
  doc = nlp(docs)
  
  for token in doc:
    pos_counts[token.pos][token.orth] += 1

  words = []
  for pos_id, counts in pos_counts.items():
    pos = doc.vocab.strings[pos_id]
    for orth_id, count in counts.most_common(2):
      print(pos_id, pos, count, doc.vocab.strings[orth_id])
      words.append(doc.vocab.strings[orth_id])
  
  print(" ".join(words))

def use_textacy(text):
  import textacy
  import textacy.keyterms
  doc = textacy.Doc(text)

  print(textacy.keyterms.textrank(doc, normalize='lemma', n_keyterms=10))
  bot = doc.to_bag_of_terms(
       ngrams=(1, 2, 3), named_entities=True, weighting='count',
       as_strings=True)
  print(sorted(bot.items(), key=lambda x: x[1], reverse=True)[:15])


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-d', '--year',
                      type=str, help='Analyse papers from years in range. Output given per year. e.g. 1997-2019 will output data for each year in the range. Or enter a single year')
  parser.add_argument('-w', '--words',
                      type=int, help='Show this many most frequently used words.',
                      default=50)
  parser.add_argument('--stop', help='Filter stopwords from the most frequently used words.',
                      action='store_true', default=False)
  parser.add_argument('--customstop', help='Filter customisable stopwords.',
                      action='store_true', default=False) 
  args = parser.parse_args()

  path, filename = os.path.split(os.path.realpath(__file__))
  with open(os.path.join(path, '../data/all.json')) as fh:
    parsed = json.loads(fh.read())
    docs = get_docs(parsed, args.year, args.words)
    # print(most_frequent_words(parsed, year=args.year, num=args.words, stop=args.stop, extra_stops=args.customstop))
    # use_textacy(text)
    use_spacy(docs)
