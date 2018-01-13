def getPackageList():
    f = open('./libs.txt', 'r')
    for line in f.readlines():
        # print(line)
        line = line.strip()
        # print(linestr)
        linestrlist = line.split(" ")
        # print(linestrlist)
    packageList = set(linestrlist)
    f.close()

    f = open('./built-in_libs.txt', 'r', encoding='UTF-8')
    for line in f.readlines():
        line = line.strip()
        pac = line.split(" ")[1]
        packageList.add(pac)
    print(packageList)
    # packageList已经是可以用的包了，下面是把它们存进文件
    # f = open('./packageList.txt', 'w+')
    # for i in packageList:
        # f.write(i+" ")
    return packageList
