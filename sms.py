# custom transformer class that transforms the sms text into sentence embeddings
from sentence_transformers import SentenceTransformer
from sklearn.base import BaseEstimator, TransformerMixin

class SMSSentenceTransformer(BaseEstimator, TransformerMixin):
  def __init__(self):
    self.sentence_transformer = SentenceTransformer("all-mpnet-base-v2")

  def fit(self, X, y=None):
    return self

  def transform(self, X):
    X_new = X.copy()
    embeddings = self.sentence_transformer.encode(X_new["v2"].values, show_progress_bar=False)
    X_new[[f"e{i}" for i in range(embeddings.shape[1])]] = embeddings
    X_new.drop("v2", axis=1, inplace=True)

    return X_new