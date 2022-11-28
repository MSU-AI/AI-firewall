import csv
import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from pycaret.classification import *

def create_csv(url):
    fp = open("url.csv", "w", encoding="UTF8", newline='')
    writer = csv.writer(fp)
    header = ["id", "url", "type"]
    writer.writerow(header)

    row = ["0", url, "benign"]
    writer.writerow(row)
    fp.close()

def count_suspicious_chars(row):
    unicode_count, inequality_count, pipe_count, semicolon_count, curlybrace_count, caret_count, hyphen_count, underscore_count = 0, 0, 0, 0, 0, 0, 0, 0
    for char in row['url']:
        if str(type(char)) == "<type 'unicode'>":
            unicode_count += 1
        elif char == '<' or char == '>':
            inequality_count += 1
        elif char == '|':
            pipe_count += 1
        elif char == ';':
            semicolon_count += 1
        elif char == '{' or char == '}':
            curlybrace_count += 1
        elif char == '^':
            caret_count += 1
        elif char == '-':
            hyphen_count += 1
        elif char == '_':
            underscore_count += 1
    
    consecutive_num_count = str(max(re.findall(r"\d+", row['url']), key=len, default=0))
    if consecutive_num_count == '0':
        consecutive_num_count = 0
    else:
        consecutive_num_count = len(consecutive_num_count)

    return unicode_count, inequality_count, pipe_count, semicolon_count, curlybrace_count, caret_count, \
        consecutive_num_count, hyphen_count, underscore_count

def prepare_data():
    url_df = pd.read_csv("url.csv")
    all_counts = url_df.apply(lambda row: count_suspicious_chars(row), axis=1)
    
    url_df['unicode'] = [tup[0] for tup in all_counts]
    url_df['inequality'] = [tup[1] for tup in all_counts]
    url_df['pipe'] = [tup[2] for tup in all_counts]
    url_df['semicolon'] = [tup[3] for tup in all_counts]
    url_df['curlybrace'] = [tup[4] for tup in all_counts]
    url_df['caret'] = [tup[5] for tup in all_counts]
    url_df['consecutive_num'] = [tup[6] for tup in all_counts]
    url_df['hyphen'] = [tup[7] for tup in all_counts]
    url_df['underscore'] = [tup[8] for tup in all_counts]

    fp = open("url.csv", "w")
    fp.truncate()
    fp.close()

    url_df.to_csv("url.csv")

def apply_model():
    test_set = pd.read_csv("url.csv")
    loaded_model = load_model("basic_RF_url_classifier")
    results = predict_model(loaded_model, test_set)
    fp = open("url.csv", "w")
    fp.truncate()
    fp.close()
    results = results['Label'].iloc[0]
    results = results[:]
    return results
    
