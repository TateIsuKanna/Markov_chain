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

with open("res.txt",encoding="UTF-8") as f:
    for centence in f:
        a=centence.split()
        wordlist = ["<SOS>"] + a + ["<EOS>"]
        #wordlist = ["<SOS>"] + list(map("".join,list(itertools.zip_longest(a[::2],a[1::2],fillvalue="")))) + ["<EOS>"]
        #for left,right in zip(wordlist,wordlist[1:]):
        add_rate(zip()
        add_rate(zip(map("".join,zip(wordlist,wordlist[1:])),wordlist[2:]))
        #wordlist = list(map("".join,list(itertools.zip_longest(a[1::2],a[2::2],fillvalue="")))) + ["<EOS>"]
        #for left,right in zip(wordlist,wordlist[1:]):
        #    if left in rate:
        #        if right in rate[left]:
        #            rate[left].update({right:rate[left][right]+1})
        #        else:
        #            rate[left][right]=1
        #    else:
        #        rate[left]={right:1}

print(rate)

import time
while True:
    sentence=""
    word="<SOS>"
    while True:
        word=random.choices(list(rate[word].keys()),list(rate[word].values()))[0]
        if word=="<EOS>":
            break
        sentence+=word
    print(sentence)
    time.sleep(2)
