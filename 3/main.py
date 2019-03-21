import os
import argparse
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def stemmed(docs):
  stemmer = PorterStemmer()
  return [" ".join([stemmer.stem(word) for word in doc.lower().split()]) for doc in docs]


def calculate_tfidf(docs):
  # max_df ignore terms appearing in more than x% documents
  # min_df ignore terms appearing in less than x% documents
  tfidf_vectorizer = TfidfVectorizer(max_df=0.8, min_df=2,
                                     ngram_range=(1, 2),
                                     sublinear_tf=True, 
                                     use_idf=True,
                                     max_features=500,
                                     stop_words='english')
  tfidf = tfidf_vectorizer.fit_transform(docs)
  weights = np.asarray(tfidf.mean(axis=0)).ravel().tolist()
  weights_df = pd.DataFrame({'term': tfidf_vectorizer.get_feature_names(), 'weight': weights})
  print(weights_df.sort_values(by='weight', ascending=False).head(20))



if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument(
      "input", help="Location of file containing newline separated text, relative to current directory.")
  args = parser.parse_args()

  with open(os.path.join(os.getcwd(), "{}".format(args.input))) as fh:
    lines = fh.readlines()
    calculate_tfidf(lines)
