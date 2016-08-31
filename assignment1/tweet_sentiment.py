import sys
import json
import re

scores = {}

def sentiment_score(file):
    for line in file:
        term, score = line.split("\t")
        scores[term] = int(score)

def tweet_sentiment(file):
    for line in file:
        result = json.loads(line)
        result_str = result.get('text', 'zz').encode('utf-8')
        words = re.compile('\w+').findall(result_str)
        word_score(words)

def word_score(word_list):
    tweet_score = 0
    for word in word_list:
        try:
            word_val = scores[word]
            tweet_score += word_val
        except KeyError:
            continue
    print tweet_score


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentiment_score(sent_file)
    tweet_sentiment(tweet_file)

if __name__ == '__main__':
    main()
