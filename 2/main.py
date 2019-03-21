import json
import os
import argparse
import string
from scipy import stats
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist


class Processor(object):
  def __init__(self, parsed):
    self.data = parsed
    self.analysis = []
    for item in self.data:
      title = item['title']
      line_stats = {
        'text': title,
        'length': len(title),
      }
      self.analysis.append(line_stats)

  def average_line_length(self):
    total = 0
    for item in self.analysis:
      total = total + len(item['text'])
    return total / len(self.analysis)

  def mode(self):
    data = [len(item['text']) for item in self.analysis]
    return stats.mode(data)

  def most_frequent_words(self, year, num, stop):
    all_text = ''

    if (year is not 'all'):
      titles = [title['title'] for title in self.data if title['year'] == year]
    else:
      titles = [title['title'] for title in self.data]

    for title in titles:
      all_text += title

    all_words = word_tokenize(all_text)

    if stop:
      all_words = [w for w in all_words if w.lower() not in stopwords.words('english') + list(string.punctuation)]

    fdist = FreqDist(all_words)
    return fdist.most_common(num)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-y", "--year", 
                      type=str, help="Analyse papers from one year.", 
                      default="all")
  parser.add_argument("-w", "--words", 
                      type=int, help="Show this many most frequently used words.", 
                      default=20)
  parser.add_argument("--stop", help="Filter stopwords from the most frequently used words.",
                      action="store_true", default=False)
  args = parser.parse_args()

  path, filename = os.path.split(os.path.realpath(__file__))
  with open(os.path.join(path, "../data/all.json")) as fh:
    parsed = json.loads(fh.read())
    ts = Processor(parsed)
    print('Mean title length:', ts.average_line_length())
    print('Mode title length:', ts.mode()[0])
    print('Most frequently used words:')
    print(ts.most_frequent_words(year=args.year, num=args.words, stop=args.stop))
