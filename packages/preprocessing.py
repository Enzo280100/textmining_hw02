import re
import pandas as pd
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer
from collections import Counter
from tabulate import tabulate
import swifter
from tqdm import tqdm

def get_wordnet_pos(treebank_tag):
    """Converts POS tags to WordNet format for lemmatization"""
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def build_complete_stopwords(corpus, top_n=50, min_length=3):
    """Build comprehensive stopwords set with additional filtering"""
    english_stops = set(stopwords.words('english'))
    domain_stops = {
        'news', 'report', 'reports', 'breaking', 'update', 'reuters', 'said',
        'article', 'coverage', 'video', 'audio', 'bloomberg', 'cnn', 'bbc',
        'times', 'today', 'york', 'associated', 'press', 'ap', 'click', 'read',
        'st', 'nd', 'rd', 'th', 'the', 'etc', 'ie', 'eg'
    }
    
    all_tokens = []
    for doc in corpus.dropna():
        doc_clean = re.sub(r'[^\w\s]', ' ', doc.lower())
        doc_clean = re.sub(r'\d+', ' ', doc_clean)
        doc_clean = re.sub(r'\s+', ' ', doc_clean)
        
        tokens = word_tokenize(doc_clean)
        tokens = [t for t in tokens if len(t) >= min_length]
        all_tokens.extend(tokens)
    
    freq_counts = Counter(all_tokens)
    most_common_tokens = {word for word, _ in freq_counts.most_common(top_n)}
    full_stopwords = english_stops.union(domain_stops, most_common_tokens)
    
    return full_stopwords

def preprocess_text(text, stopwords_set, lemmatizer, min_token_length=3):
    """Enhanced text preprocessing with better token filtering"""
    if pd.isna(text):
        return ''

    text = re.sub(r'https?://\S+|www\.\S+', ' ', text.lower())
    text = re.sub(r'\d+(st|nd|rd|th)', ' ', text)
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\b\d+\b', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stopwords_set and len(t) >= min_token_length]
    
    if not tokens:
        return ''
    
    pos_tags = pos_tag(tokens)
    lemmatized_tokens = [
        lemmatizer.lemmatize(token, get_wordnet_pos(pos))
        for token, pos in pos_tags
    ]
    
    result_tokens = [t for t in lemmatized_tokens if len(t) >= min_token_length and t != 'th']
    return ' '.join(result_tokens)

def process_text_pipeline(df, text_column='full_content', batch_size=1000):
    """Complete text processing pipeline for a DataFrame"""
    FULL_STOPWORDS = build_complete_stopwords(df[text_column], top_n=50, min_length=3)
    LEMMATIZER = WordNetLemmatizer()
    
    df['processed_content'] = df[text_column].swifter.apply(
        lambda x: preprocess_text(
            x, stopwords_set=FULL_STOPWORDS, lemmatizer=LEMMATIZER, min_token_length=3
        )
    )
    
    # Create the preview
    df['processed_preview'] = df['processed_content'].str.slice(0, 200) + \
                              df['processed_content'].swifter.apply(lambda x: "..." if len(x) > 200 else "")
    
    # Check for empty results and tokens like "th"
    th_count = df['processed_content'].str.contains(r'\bth\b').sum()
    empty_count = (df['processed_content'] == '').sum()
    short_count = (df['processed_content'].str.split().str.len() <= 3).sum()
    
    print(f"Documents containing 'th': {th_count} ({th_count/len(df)*100:.2f}%)")
    print(f"Empty documents: {empty_count} ({empty_count/len(df)*100:.2f}%)")
    print(f"Documents with 3 or fewer tokens: {short_count} ({short_count/len(df)*100:.2f}%)")
    
    # Remove empty previews
    empty_previews = df[df['processed_preview'].isna() | (df['processed_preview'] == '')]
    df.drop(empty_previews.index, inplace=True)
    
    return df

if __name__ == "__main__":
    print("This script is designed to be imported as a module.")
