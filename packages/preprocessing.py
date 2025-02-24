import re
from sklearn.base import BaseEstimator, TransformerMixin
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import nltk


class Tokenizer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        '''
        Tokenize the text: split the text into words.
        Example: tokenize('The cat is on the mat.') -> ['The', 'cat', 'is', 'on', 'the', 'mat.']
        '''
        return X.apply(word_tokenize)

class Normalizer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        '''
        Normalize the tokens: convert to lowercase and remove punctuation.
        Example: normalize(['The', 'cat', 'is', 'on', 'the', 'mat.']) -> ['the', 'cat', 'is', 'on', 'the', 'mat']
        '''
        return X.apply(lambda tokens: [re.sub(r'[^\w\s]', '', token.lower()) for token in tokens])

class RemoveStopwords(BaseEstimator, TransformerMixin):
    def __init__(self, language='english'):
        '''
        Initialize with a set of stopwords for the specified language.
        If no language is specified, the default is English.
        '''
        self.stopwords = set(stopwords.words(language))

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        '''
        Remove stopwords from the list of tokens.
        Example: remove_stopwords(['the', 'cat', 'is', 'on', 'the', 'mat']) -> ['cat', 'mat']
        '''
        return X.apply(lambda tokens: [token for token in tokens if token not in self.stopwords])

class Lemmatizer(BaseEstimator, TransformerMixin):
    def __init__(self):
        '''
        Initialize the WordNetLemmatizer.
        '''
        self.lemmatizer = WordNetLemmatizer()

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        '''
        Lemmatize the tokens: convert to their base form.
        Example: lemmatize('running') -> 'run' or lemmatize('better') -> 'good'
        '''
        return X.apply(lambda tokens: [self.lemmatizer.lemmatize(token) for token in tokens])

class Stemmer(BaseEstimator, TransformerMixin):
    def __init__(self):
        '''
        Initialize the SnowballStemmer for English
        '''
        self.stemmer = SnowballStemmer("english")

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        '''
        Apply stemming to the tokens: reduce to their root form.
        Example: stem('wars') -> 'was' or stem('mother') -> 'moth'
        '''
        return X.apply(lambda tokens: [self.stemmer.stem(token) for token in tokens])

class JoinTokens(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        '''
        Join the tokens back into a single string.
        '''
        return X.apply(lambda tokens: ' '.join(tokens))
