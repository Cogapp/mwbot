import json
from scipy import stats
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist

class Textstats(object):
  def __init__(self, parsed):
    self.data = parsed
    self.analysis = []
    for title in self.data:
      text = title['text']
      line_stats = {
        'text': text,
        'length': len(text),
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

  def most_frequent_words(self, num=50, year=None, stop=False):
    all_text = ''

    if (year):
      titles = [title['text'] for title in self.data if title['year'] == year]
    else:
      titles = [title['text'] for title in self.data]

    for title in titles:
      all_text += title

    all_words = word_tokenize(all_text)

    if stop:
      all_words = [w for w in all_words if w.lower() not in stopwords.words('english')]

    fdist = FreqDist(all_words)
    return fdist.most_common(num)


if __name__ == "__main__":
  year = '2009'
  with open('../mw-years.json') as data:
    parsed = json.loads(data.read())
    ts = Textstats(parsed)
    print('Mean title length:', ts.average_line_length())
    print('Mode title length:', ts.mode()[0])
    print('Most frequent things used in titles in {}:\n'.format(year))
    print(ts.most_frequent_words(year=year, stop=True))
