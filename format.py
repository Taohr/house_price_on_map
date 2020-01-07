def format():
    file = open('2019.4.1', 'r')
    data = file.readlines();
    data = [item[:-1] for item in data]



    table = []
    num = 0

    for item in data:
        if item == '%s'%(num+1):
            table.append([])
            num += 1
        table[-1].append(item)

    [print('\t'.join(line)) for line in table]
    pass


# format()


def maps():
    file = open('latlon_145173.txt', 'r')
    data = file.readlines()
    data = [item[:-1] for item in data][1:]
    locations = []
    for item in data:
        arr = item.split(',')
        la = arr[4]
        lo = arr[5]
        name = arr[8]
        locations.append([la, lo, name])
    [print('\t'.join(pos)) for pos in locations]
    pass

# maps()


def jsdata():
    file = open('2019.4.4', 'r')
    data = file.readlines()
    data = [item[:-1] for item in data]
    data = [item.split('\t') for item in data]
    # print(data[:10])
    labels = []
    for pos in data:
        name = pos[1]
        la = pos[6]
        lo = pos[7]
        price = pos[3]
        rate = pos[4]
        change = pos[5]
        if la == '0' or lo == '0':
            continue
        labels.append([la, lo, name, price, rate, change])
    # [print(item, ',') for item in labels]
    print(labels)
    pass

jsdata()