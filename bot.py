#時刻や曜日も
import json
with open("auth.json") as jfs:
    authdata=json.load(jfs)

import twitter
auth = twitter.OAuth(**authdata)
t = twitter.Twitter(auth=auth)

import itertools
import random
import datetime

tweet_per_hour=2.78
tweet_rate=[[0.08816102198455139, 0.04664289958407605, 0.03401663695781343, 0.01567142008318479, 0.00564468211527035, 0.004084967320261438, 0.008095662507427213, 0.04122103386809269, 0.03312537136066548, 0.013443256090314914, 0.015151515151515152, 0.01567142008318479, 0.02904040404040404, 0.04567736185383244, 0.028594771241830064, 0.02369281045751634, 0.02161319073083779, 0.032234105763517526, 0.04827688651218063, 0.0647653000594177, 0.06885026737967914, 0.10918003565062388, 0.1006387403446227, 0.10650623885918004], [0.09635011243729459, 0.03580695381421899, 0.016000691921812835, 0.0034596090641757483, 0.006313786542120741, 0.00536239404947241, 0.010984258778758001, 0.03234734475004324, 0.019460300985988582, 0.013838436256702993, 0.014530358069538143, 0.015568240788790867, 0.041255838090295795, 0.02170904687770282, 0.024822695035460994, 0.016260162601626018, 0.025514616848296142, 0.0398719944646255, 0.055699705933229544, 0.08796056045666839, 0.08138730323473448, 0.10223144784639336, 0.10949662688116243, 0.12376751427088739], [0.07749803304484658, 0.046420141620771044, 0.03571990558615264, 0.010228166797797011, 0.004327301337529505, 0.002989771833202203, 0.007159716758457908, 0.02832415420928403, 0.02077104642014162, 0.016522423288749016, 0.025019669551534226, 0.018804091266719117, 0.03870967741935484, 0.027458693941778127, 0.02903225806451613, 0.024232887490165226, 0.029504327301337528, 0.03068450039339103, 0.04799370574350905, 0.07655389457120378, 0.07686860739575138, 0.1047993705743509, 0.1099921321793863, 0.11038552321007081], [0.08032549145987754, 0.05776667740895907, 0.029487592652271993, 0.009506928778601353, 0.005398001933612633, 0.004672897196261682, 0.011923944569771189, 0.03303254914598775, 0.026506606509829198, 0.011521108604576216, 0.012246213341927168, 0.014340960360941025, 0.03335481791814373, 0.024653561069932325, 0.03303254914598775, 0.0279568159845311, 0.034160489848533676, 0.04793747985820174, 0.05502739284563326, 0.07992265549468257, 0.06646793425717049, 0.09805027392845633, 0.10409281340638092, 0.0986142442797293], [0.08584811487368502, 0.04254012132381172, 0.025186209014819935, 0.011287721723105276, 0.00506795669200645, 0.013668125623896184, 0.021961145665361285, 0.03616678184750058, 0.029639867925977118, 0.017814635644628735, 0.013514551178683868, 0.014589572295170083, 0.034170314059740456, 0.03294171849804193, 0.031175612378100286, 0.021884358442755124, 0.024571911233970668, 0.03585963295707594, 0.0654227136604469, 0.08515702987022959, 0.07095139368809031, 0.08723028488059587, 0.09314290102127006, 0.10020732550103663], [0.08149405772495756, 0.047792869269949065, 0.025806451612903226, 0.005942275042444821, 0.004499151103565365, 0.0032258064516129032, 0.0045840407470288625, 0.024533106960950762, 0.017826825127334467, 0.017062818336162987, 0.02359932088285229, 0.02563667232597623, 0.02606112054329372, 0.034125636672325974, 0.03191850594227504, 0.03769100169779287, 0.039134125636672325, 0.05458404074702886, 0.0599320882852292, 0.06426146010186758, 0.07410865874363327, 0.08259762308998302, 0.10127334465195247, 0.11230899830220713], [0.08318610129564193, 0.0708186101295642, 0.05131036513545347, 0.017594228504122497, 0.004932273262661956, 0.002429328621908127, 0.0045641931684334515, 0.007950530035335688, 0.010011778563015312, 0.013766195524146055, 0.015017667844522967, 0.024808598351001177, 0.030918727915194347, 0.04549469964664311, 0.034231448763250884, 0.03872202591283863, 0.044979387514723204, 0.04630447585394582, 0.04799764428739694, 0.05742049469964664, 0.04983804475853946, 0.09062131919905772, 0.10019140164899883, 0.1068904593639576]]

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
    try:
        now=datetime.datetime.now()
        if random.random()<tweet_rate[now.weekday()][now.hour]*tweet_per_hour*24/60:
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
                    break
            print(tweet_rate[now.weekday()][now.hour],tweet_rate[now.weekday()][now.hour]*tweet_per_hour*24/60*100,"%")
            print(sentence)
            t.statuses.update(status=sentence)
        time.sleep(60)
    except:
        print(sys.exc_info)
