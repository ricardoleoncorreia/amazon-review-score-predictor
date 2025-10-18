import pandas as pd
import numpy as np
import os

from sklearn.feature_extraction.text import CountVectorizer

def filter_dataset_by_language(filename, language, index_col=0):
    print(f"Processing {filename}.csv...")
    
    input_path = os.path.join('../data/raw', f'{filename}.csv')
    df = pd.read_csv(input_path, index_col=index_col)
    
    df_filtered = df[df['language'] == language]

    os.makedirs('../data/interim', exist_ok=True)

    output_path = os.path.join('../data/interim', f'{filename}.csv')
    df_filtered.to_csv(output_path, index=False)

    original_records = len(df)
    filtered_records = len(df_filtered)

    return {
        'filename': filename,
        'original_records': original_records,
        'filtered_records': filtered_records,
        'percentage': round(100 * filtered_records / original_records, 2) if original_records > 0 else 0,
        'unique_languages': df_filtered['language'].unique().tolist()
    }

class NLPUtils:
  @staticmethod
  def lemmatize_text(nlp, text: str, exceptions: list[str]=[]) -> str:
    doc = nlp(text.lower())
    lemmatized_words = [token.lemma_ for token in doc if NLPUtils._is_valid_token(token, exceptions=exceptions)]
    return " ".join(lemmatized_words)

  @staticmethod
  def _is_valid_token(token: str, min_word_length: int=4, exceptions:list[str]=[]):
    has_min_length = len(token.lemma_) >= min_word_length
    is_exception = token.text.lower() in exceptions
    return (not token.is_stop and not token.is_punct and has_min_length) or is_exception

  @staticmethod
  def count_common_words(df, ngram_range: tuple[int, int], max_count: int=30):
    count_vectorizer = CountVectorizer(ngram_range=ngram_range)
    words_count = count_vectorizer.fit_transform(df)
    count_per_word = words_count.toarray().sum(axis=0)
    index_order = np.argsort(-count_per_word)
    words_labels = np.array(count_vectorizer.get_feature_names_out())[index_order][0:max_count]
    count_per_word = count_per_word[index_order][0:max_count]

    return {
      'labels': words_labels,
      'counts': count_per_word
    }
