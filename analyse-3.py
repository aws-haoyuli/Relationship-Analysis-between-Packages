# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 23:45:30 2018

@author: shuqi
"""
import json

string = ''
with open ('packageList.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        string+=line
packages = string.split(' ')
packageList = []
for pa in packages:
    if pa.find('.') != -1 :
        pa = pa[0: pa.find('.')]
    packageList.append(pa)
#print(packageList)
paSet = set(packageList)
#print(paSet)

paCount = {}
paRela = {}
for pa in paSet:
    paCount[pa] = 0
    for pa2 in paSet:
        if pa != pa2:
            paRela[(pa, pa2)] = 0

topics = {}
for num in range(1, 16801):
    data = {}
    with open('datas2/repository'+str(num)+'.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    topic = data['topic']
    for to in topic:
        if to in paCount:
            paCount[to] += 1
            for to2 in topic:
                if to != to2 and (to, to2) in paRela:
                    paRela[(to, to2)] += 1
            

result1 = sorted(paCount.items(), key = lambda item:item[1], reverse = True)
result2 = sorted(paRela.items(), key = lambda item:item[1], reverse=True)


cnt = 1
for re in result1:
    print('<tr>')
    print('<td>', cnt, '</td>')
    print('<td>', re[0], '</td>')
    print('<td>', re[1], '</td>')
    print('</tr>')
    cnt += 1
    if cnt > 20:
        break
cnt = 0
cntt = 0
for re in result2:
    cnt += 1
    if cnt % 2 == 0:
        continue
    cntt += 1
    print('<tr>')
    ree = re[0]
    print('<td>', cntt, '</td>')
    print('<td>', ree[0], '</td>')
    print('<td>', ree[1], '</td>')
    print('<td>', re[1], '</td>')
    print('</tr>')
    if cntt >= 20:
        break 

"""
topics = {}
for num in range(1, 16801):
    data = {}
    with open('datas2/repository'+str(num)+'.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    topic = data['topic']
    for to in topic:
        if to in topics:
            topics[to] += 1
        else:
            topics[to] = 1

result1 = sorted(topics.items(), key = lambda item:item[1], reverse=True)
    
cnt = 1
for re in result1:
    print('<tr>')
    print('<td>', cnt, '</td>')
    print('<td>', re[0], '</td>')
    print('<td>', re[1], '</td>')
    print('</tr>')
    cnt += 1
    if cnt > 30:
        break
"""