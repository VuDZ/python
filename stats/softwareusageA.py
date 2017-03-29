import csv

pathes = dict()

with open('d:\work\stat\SoftwareInfo.csv', encoding="utf-8-sig") as csvSource:
        reader = csv.reader(csvSource, delimiter=';')
        for row in reader:
                path = row[0]
                descr = row[1]
                dirIdx = path.rfind('\\')
                directory = path[0:dirIdx]
                filename = path[dirIdx + 1:]
                if directory in pathes:
                    descrs = pathes[directory]
                    if descr not in descrs:
                        descrs[descr] = filename
                else:
                    pathes[directory] = dict()
                    pathes[directory][descr] = filename

        for directory, descrMap in pathes.items():
            if len(descrMap) > 1:
                print(directory + '\\')
                for descr, file in descrMap.items():
                    print('\t' + file + '\t->\t' + descr)

print('done')