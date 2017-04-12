"""Functions used for Parsing"""
# These functions were to large to fit in the files themselves

###################Text Cleaning##################
# dependencies
import re


def text_clean(dirtytext):
    """
    Clean text by stripping out unnecessary characters.
    Parameters
    ----------
    dirtytext : The text to be cleaned.
    """
    # replace single quotes with nothing
    tmp = re.sub("'", '', dirtytext)

    # replace commas with nothing
    tmp = re.sub(",", '', tmp)

    # replacing @ sign with just the person's username its directed too
    # also stripping links
    tmp = re.sub(r"(@)|(https?://\S*)", " ", tmp)

    #
    tmp = ' '.join(re.sub(r"(\w+:\/\/\S+)", " ", tmp).split())

    # stripping multiple spaces
    tmp = re.sub(r'[\s]+', ' ', tmp)

    # stripping excess white space
    tmp = re.sub(r'[^\w]', ' ', tmp)

    #
    tmp = re.sub(' +', ' ', tmp)

    # stripping out numbers
    tmp = re.sub('[1|2|3|4|5|6|7|8|9|0]', '', tmp)

    # if empty we just want it to be empty
    tmp = re.sub('nan', ' ', tmp)

    # lowercase the results
    tmp = tmp.lower()
    return tmp

###################Find and Replace##################
# dependencies
import re


def findandreplace(text, word, subsitutedword):
    """
    Splits the text by spaces and then if a splitted word contains your target word or phrase it replaces that word with the subsituted word.
    ----------
    text : The string of text that has the word of interest
    word : The word you want to be substituted.
    subsitutedword : The word you want to replace it with.
    """
    # split on white space
    text_list = text.split()

    # loop through all words in list
    for j in range(0, len(text_list)):

        # if word is target word apply replacement
        text_list[j] = re.sub(r'(^.*' + word + '.*$)', subsitutedword, text_list[j])
    return(text_list)

###################Standard Natural Language Processing##################
# dependencies
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def process(text, lang):
    """
    Function to deal with tokenizing, stemming or lemmantizing, and stop word filtering.

    Parameters
    ----------
    text : text of interest in string format.
    lang : language for stop word filtering.

    """
    # functions used
    tokenizer = RegexpTokenizer(r'\w+')
    lemmatizer = WordNetLemmatizer()

    # remove case
    text = text.lower()

    # tokenizing
    words = tokenizer.tokenize(text)

    # lemmantizing
    lemmed_tokenized_words = [lemmatizer.lemmatize(i) for i in words]

    # stop words
    stop_words = [i for i in lemmed_tokenized_words if i not in lang]

    return stop_words