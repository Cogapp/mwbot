import markovify
import os
from pathlib import Path

path, filename = os.path.split(os.path.realpath(__file__))
data_dir = Path(path)
with open(path / data_dir / "../data/titles.txt") as f:
  text = f.read()

text_model = markovify.NewlineText(text)
for i in range(20):
  print(text_model.make_sentence(tries=100))
