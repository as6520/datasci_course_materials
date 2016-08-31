import sys
import json
import re

frequency_dict = {}


def find_frequency(file_obj):
    for line in file_obj:
        result = json.loads(line)
        tweet = result.get("text", "zz").encode("utf-8")
        words = re.compile('\w+').findall(tweet)
        for word in words:
            if word in frequency_dict:
                frequency_dict[word] += 1
            else:
                frequency_dict[word] = 1
    for word, freq in frequency_dict.items():
        print word + "\t" + str(freq)


def main():
    tweet_file = open(sys.argv[1])
    find_frequency(tweet_file)

if __name__ == '__main__':
    main()