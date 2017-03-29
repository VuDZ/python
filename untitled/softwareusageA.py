import csv

pathes = dict()

with open('d:\work\stat\SoftwareInfo.csv', encoding="utf-8-sig") as csvSource:
        reader = csv.reader(csvSource, delimiter=';')
        for row in reader:
                path = row[0]
                descr = row[1]
                dirIdx = path.rfind('\\')
                dir = path[0:dirIdx]
                filename = path[dirIdx + 1:]
                if dir in pathes:
                    descrs = pathes[dir]
                    if descr not in descrs:
                        descrs[descr] = filename
                else:
                    pathes[dir] = dict()
                    pathes[dir][descr] = filename

        for dir, list in pathes.items():
            if len(list) > 1:
                print(dir + '\\')
                for d, f in list.items():
                    print('\t' + f + '\t->\t' + d)

print('done')