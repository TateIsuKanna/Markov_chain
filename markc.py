#時刻や曜日も

import itertools
import random

rate={}

def add_rate(list):
    for left,right in list:
        if left in rate:
            if right in rate[left]:
                rate[left].update({right:rate[left][right]+1})
            else:
                rate[left][right]=1
        else:
            rate[left]={right:1}

all_sentences=set()

import sys
if len(sys.argv)==2:
    spaced_path=sys.argv[1]
else:
    spaced_path="res.txt"
with open(spaced_path,encoding="UTF-8") as f:
    for sentence in f:
        sentence_list=sentence.split()
        all_sentences.add("".join(sentence_list))
        wordlist = ["<SOS>"] + sentence_list + ["<EOS>"]
        add_rate([(("<SOS>",),wordlist[1])])
        add_rate(zip(zip(wordlist,wordlist[1:]),wordlist[2:]))

import time
while True:
    words=["<SOS>"]
    i=-1
    while True:
        word=random.choices(list(rate[tuple(words[i:i+2])].keys()),list(rate[tuple(words[i:i+2])].values()))[0]
        if word=="<EOS>":
            break
        words.append(word)
        i+=1
    sentence="".join(words[1:])
    if sentence not in all_sentences:
        print(sentence)
        time.sleep(2)
