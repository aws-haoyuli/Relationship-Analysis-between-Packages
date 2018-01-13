# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 22:58:06 2018

@author: shuqi
"""
import json

packageCount = {}
packageRelationship = {}
allPackages = []

for num in range(1, 1001):
    data = {}
    with open('datas/repository'+str(num)+'.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    packages = data['packages']
    newPackages = []
    for pa in packages:
        idx = pa.find(' as ')
        if idx != -1:
            pa = pa[0:idx]
        if len(pa) > 1 and pa.find(' ') == -1 and pa != '\n' and pa.find('"') == -1 and pa.find('(') == -1 and pa.find(')') == -1 and pa.find('/') == -1 and pa != 'Django':
            newPackages.append(pa)
    # allPackages.append(newPackages)
    for pa in newPackages:
        if pa in packageCount:
            packageCount[pa] += 1
        else:
            packageCount[pa] = 1
        for pa2 in newPackages:
            if pa != pa2:
                a = (pa, pa2)
                if a in packageRelationship:
                    packageRelationship[a] += 1
                else:
                    packageRelationship[a] = 1
   
result1 = sorted(packageCount.items(), key = lambda item:item[1], reverse = True)
result2 = sorted(packageRelationship.items(), key = lambda item:item[1], reverse=True)

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
    if cntt >= 40:
        break 

import csv
csvFile = open("data.csv", "w",newline='')
writer = csv.writer(csvFile)
writer.writerow(['Source', 'Target', 'Weight'])
for re in result2:
    writer.writerow((re[0][0], re[0][1], str(re[1])))
csvFile.close()