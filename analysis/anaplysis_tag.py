import pymongo
from pymongo import MongoClient
import pprint
import read
import csv





def getRelationship(collection, filterList):
    # （库名1，库名2）：次数
    packageRelationship = {}
    file = open('packageRelationship.txt', "w+")
    # packageList = read.getPackageList()
    # print(filterList)
    num = 1


    for i in collection.find():
        tempArray = i['tags']
        # print(tempArray)
        tempArray = list(set(tempArray) & set(filterList))
        # print(tempArray)
        for j in tempArray:
            for k in tempArray:
                if (j, k) not in packageRelationship and j != k and (k, j) not in packageRelationship:
                    packageRelationship[(j, k)] = 1
                elif (j, k) in packageRelationship or (k, j) in packageRelationship:
                    if (j, k) in packageRelationship:
                        packageRelationship[(j, k)] += 1
                    elif (k, j) in packageRelationship:
                        packageRelationship[(k, j)] += 1
        # print(array)
    print(packageRelationship)
    print(packageRelationship.__len__())
    # for (pac1, pac2) in packageRelationship:
        # strr = str(pac1) + "," + str(pac2) + "," + str(packageRelationship[(pac1, pac2)])
        # file.write(strr+'\n')

    csvFile = open("data.csv", "w",newline='')
    writer = csv.writer(csvFile)
    writer.writerow(['Source', 'Target', 'Weight'])

    results = sorted(packageRelationship.items(), key=lambda item: item[1], reverse=True)
    for i in results:
        file.write('<tr>')
        file.write('<td>'+ str(num) + '</td>')
        file.write('<td>'+ str(i[0][0]) + '</td>')
        file.write('<td>'+ str(i[0][1]) + '</td>')
        file.write('<td>'+ str(i[1]) + '</td>')
        # print('<td> %.2f%% </td>' % (re[1] / sum * 100))
        file.write('</tr>')
        num += 1
        writer.writerow((str(i[0][0]), str(i[0][1]), str(i[1])))

    return packageRelationship
