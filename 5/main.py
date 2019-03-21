import markovify
import os
from pathlib import Path
import re
import spacy

nlp = spacy.load("en")


class POSifiedText(markovify.Text):
  def sentence_split(self, text):
    return re.split(r"\s*\n\s*", text)

  def word_split(self, sentence):
    return ["**".join((word.orth_, word.pos_)) for word in nlp(sentence)]

  def word_join(self, words):
    sentence = ""
    prevword= ""
    for word in words:
      word, type = word.split("**")
      if type == 'PUNCT' or prevword in ['#']:
        sentence += word
      else:
        sentence += " {}".format(word)
      prevword = word
    return re.sub(r'"\s(\w)', '"$1', sentence)


path, filename = os.path.split(os.path.realpath(__file__))
data_dir = Path(path)
with open(path / data_dir / "../data/titles.txt") as f:
  text = f.read()

text_model = POSifiedText(text)
for i in range(20):
  print(text_model.make_sentence())
