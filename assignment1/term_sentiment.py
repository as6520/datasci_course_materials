import sys
import json
import re

scores = {}
missing_words = {}


def sentiment_score(file_obj):
    for line in file_obj:
        word, score = line.split("\t")
        scores[word] = int(score)


def term_sentiment(file_obj):
    for line in file_obj:
        result = json.loads(line)
        tweet = result.get('text','zz').encode('utf8')
        words = re.compile('\w+').findall(tweet)
        word_score(words)
        missing_score()


def word_score(word_list):
    tweet_score = 0
    new_word = []
    for word in word_list:
        try:
            tweet_score += scores[word]
        except KeyError:
            new_word.append(word)
    for word in new_word:
        if word in missing_words:
            missing_words[word].append(tweet_score)
        else:
            missing_words[word] = [tweet_score]


def missing_score():
    for word, score_list in missing_words.items():
        new_score = sum(score_list)
        print word + "\t" + str(new_score)


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentiment_score(sent_file)
    term_sentiment(tweet_file)


if __name__ == '__main__':
    main()
