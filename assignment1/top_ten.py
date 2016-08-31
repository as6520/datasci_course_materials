import sys
import json
import operator

hashtag_frequency = {}


def best_hastags(file_obj):
    for line in file_obj:
        result = json.loads(line)
        res = result.get('entities')
        if res is not None:
            hashtags = res.get('hashtags')
            if len(hashtags)>0:
                hashtag_str = hashtags[0].get('text').encode('utf-8')
                try:
                    hashtag_frequency[hashtag_str] += 1
                except KeyError:
                    hashtag_frequency[hashtag_str] = 1
    sorted_hash_tags = sorted(hashtag_frequency.items(),
                              key=operator.itemgetter(1),
                              reverse=True)
    for i in range(10):
        print sorted_hash_tags[i][0] + "\t" + str(sorted_hash_tags[i][1])

def main():
    tweet_file = open(sys.argv[1])
    best_hastags(tweet_file)


if __name__ == '__main__':
    main()