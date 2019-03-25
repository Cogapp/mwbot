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


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-d', '--year',
                      type=str, help='Analyse papers from years in range. Output given per year. e.g. 1997-2019 will output data for each year in the range. Or enter a single year')
  parser.add_argument('-w', '--words',
                      type=int, help='Show this many most frequently used words.',
                      default=20)
  parser.add_argument('--stop', help='Filter stopwords from the most frequently used words.',
                      action='store_true', default=False)
  parser.add_argument('--customstop', help='Filter customisable stopwords.',
                      action='store_true', default=False) 
  args = parser.parse_args()

  path, filename = os.path.split(os.path.realpath(__file__))
  with open(os.path.join(path, '../data/all.json')) as fh:
    parsed = json.loads(fh.read())
    print(most_frequent_words(parsed, year=args.year, num=args.words, stop=args.stop, extra_stops=args.customstop))

