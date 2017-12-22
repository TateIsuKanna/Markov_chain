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

all_centences=set()

with open("res.txt",encoding="UTF-8") as f:
    for centence in f:
        centence_list=centence.split()
        all_centences.add("".join(centence_list))
        wordlist = ["<SOS>"] + centence_list + ["<EOS>"]
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
    centense="".join(words[1:])
    if centense not in all_centences:
        print(centense)
        time.sleep(2)
