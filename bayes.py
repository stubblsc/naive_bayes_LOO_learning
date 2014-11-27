#!/usr/bin/env python

def read_classes_and_attributes(filename):
    file = open(filename, 'r')
    lines = file.readlines()

    global num_samples
    num_samples = int(lines[0][lines[0].index(':')+1:].strip())
    lines = lines[1:]

    global classes
    classes = lines[0][lines[0].index(':')+1:].replace('and',''). replace(',','').split()
    classes = [c.strip() for c in classes]
    classes = list(map(int, classes))
    lines = lines[1:]

    global attributes
    for line in lines:
        attr = line[line.index('{')+1:line.index('}')].split(',')
        attr = [a.strip() for a in attr]
        attributes.append(attr)

def read_data_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()

    data = []

    for line in lines:
        d = line.split()
        d[-1] = int(d[-1])
        data.append(d)

    return data

def process_data():
    global data
    global classes
    pass_count = 0

    for i in range(0,9999):
        test = data[i]
        c_probs = []
        for c in classes:
            probs = []
            for k in range(0,len(test)-1):
                count = 0
                c_count = 0
                for j in range(0,9999):
                    if i == j:
                        continue
                    else:
                        if data[j][k] == test[k] and data[j][-1] == c:
                            count += 1
                    if data[j][-1] == c:
                        c_count += 1
                probs.append(count/(num_samples-1))
                test_prob = c_count/(num_samples-1)
            prob = test_prob
            for p in probs:
                prob *= p
            c_probs.append(prob)
        if classes[c_probs.index(max(c_probs))] == test[-1]:
            print(classes[c_probs.index(max(c_probs))],'-',test[-1],':PASS')
            pass_count += 1
        else:
            print(classes[c_probs.index(max(c_probs))],'-',test[-1],':FAIL')
    print('PASS RATE: ',pass_count/(num_samples-1))


num_samples = 0
classes = []
attributes = []
f = input('What data file would you like to use? ')
read_classes_and_attributes(f.strip('.txt')+'_attr.txt')
data = read_data_file(f)
process_data()
