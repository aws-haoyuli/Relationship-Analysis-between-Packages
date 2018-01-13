from pymongo import MongoClient
import read
import matplotlib.pyplot as plt
import numpy as np


def getCounts(collection):
    packageCounts = {}
    temp = {}
    file = open('counts.txt', "w+")
    num = 0
    filterList = read.getPackageList()
    pic = {}
    ## 统计出现次数或者热度
    for i in collection.find():
        sum = 0
        status = i['status']
        for ii in status:
            sum += int(status[ii].replace(',',''))
        tempArray = i['tags']
        tempArray = set(filterList) & set(tempArray)
        for j in tempArray:
            if j in packageCounts:
                packageCounts[j] += sum
            else:
                packageCounts[j] = sum
    ## 出现次数大于1的找出来，排序，写入文件
    for i in packageCounts:
        if packageCounts[i] > 1:
            temp[i] = packageCounts.get(i)
    packageCounts = temp
    results = sorted(packageCounts.items(), key=lambda item: item[1], reverse=True)
    for i in results:
        if num<50:
            file.write('<tr>')
            file.write('<td>'+ str(num) + '</td>')
            file.write('<td>'+ str(i[0]) + '</td>')
            file.write('<td>'+ str(i[1]) + '</td>')
            # print('<td> %.2f%% </td>' % (re[1] / sum * 100))
            file.write('</tr>')
            num += 1
            pic[i[0]] = int(i[1])

    print(pic)


    print(packageCounts)
    print(packageCounts.__len__())
    return packageCounts
