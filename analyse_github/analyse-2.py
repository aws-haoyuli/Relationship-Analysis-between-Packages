# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 21:37:22 2018

@author: shuqi
"""

import json

licenses = {}
counts = {}
relationship = {}

for num in range(1, 16801):
    data = {}
    with open('datas2/repository'+str(num)+'.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    lic = data['license']
    if lic is not None:
        li = lic['key']
        if li in licenses:
            licenses[li] += 1
        else:
            licenses[li] = 1

    # tags = data['topics']
    # for tag in tags:
    
   
result1 = sorted(licenses.items(), key = lambda item:item[1], reverse=True)

sum = 0
for re in result1:
    sum += re[1]

d = []
for re in result1:
    d.append(re[0])
    print('<tr>')
    print('<td>', re[0], '</td>')
    print('<td>', re[1], '</td>')
    print('<td> %.2f%% </td>' % (re[1]/sum * 100))
    print('</tr>')
print(d)