#!/usr/bin/python
import sys
import csv
import math

def entropy(P, N):
    #return (-(P/(P+N)) * math.log2(P/(P+N))) - ((N / (P+N)) * math.log2(N / P + N))
    q = P / (P + N)
    return -(q * math.log2(q) + (1 - q) * math.log2(1 - q))



def recursive_split(data, attributes, last_column, before_entropy, tree, key_list):
    
    gain = []
    before = set()
    positive_subset = []
    split_data = {}
    for x in range(len(attributes)):
        present = set()
        tmp = {}    
        information_gain = 0
        i = 0
        for y in data:
            element = y[x].strip(',')
            key = str(attributes[x])+" "+element
            if key in present:
                tmp[key].append(last_column[i])
                split_data[key].append(last_column[i])
            else:
                tmp[key] = [last_column[i]]
                split_data[key] = [last_column[i]]
                present.add(key)
                before.add(key)
            i+=1 
        present = list(present)
        total = len(last_column)
        information_gain = 0
        for z in present:
            P = 0
            N = 0
            for e in tmp[z]:
                if e == "Yes":
                    P += 1
                else:
                    N += 1
            #print(z)
            #print(P)
            #print(N)
            #print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            current_total = P+N
            if (N / current_total) != 0.0 and (P / current_total) != 0.0:
                information_gain += (current_total/total) * entropy(P, N)
            if P != 0 and N != 0:
                positive_subset.append(z)
        information_gain = before_entropy-information_gain
        gain.append(round(information_gain,2))
    max_gain = max(gain)
    max_attribute = attributes[gain.index(max_gain)]
    data_id = ' '
    sp = ' '
    print("Attributes: " + str(attributes))
    print("Information Gain: " + str(gain))
    print("Highest Information Gain: " + max_attribute + " with " + str(max_gain))
    for ps in positive_subset:
        if ps.find(max_attribute) != -1:
            sp = ps.split()
            data_id = sp[1]+","
            
    
    before = list(before)
    oP = 0
    oN = 0

    for b in before:

        P = 0
        N = 0
        if b.find(max_attribute) != -1:
            for s in split_data[b]:
                if s == "Yes":
                    P+=1
                else:
                    N+=1
            if P >= N:
                oP+=1
                if b == sp:
                    tree[b] = (("node", "Yes", b))
                else:
                    tree[b] = (("Yes", b))
                key_list.append(b)
            else:
                oN+=1
                if b == sp:
                    tree[b] = (("node", "Yes", b))
                else:
                    tree[b] = (("No", b))
                key_list.append(b)
    new_entropy = before_entropy
    if (oN / (oP + oN)) != 0.0 and (oP / (oP + oN)) != 0.0:
        new_entropy = entropy(oP, oN)
    else:
        new_entropy = 1.0
    newdata = []
    new_last_column = []
    it = 0
    for n in data:
        if data_id == n[gain.index(max_gain)]:
            newdata.append(n)
            new_last_column.append(last_column[it])
        it+=1
    
    counter = 0

    for d in newdata:
        d.pop(gain.index(max_gain))
    attributes.pop(gain.index(max_gain))
    print("---------------------------------------------")
    print("\n\n")
    if new_last_column and attributes:
        recursive_split(newdata, attributes,new_last_column,new_entropy, tree, key_list)
    return tree, key_list

def main(argv):
    print(argv[1])
    data = []
    attributes = ["Alt", "Bar", "Fri", "Hun", "Pat", "Price", "Rain", "Res", "Type", "Est"]
    with open(argv[1], "r") as fp:
        for line in fp:
            line = line.split()
            data.append(line)
    
    last_column = []
    for l in data:
        last_column.append(l[len(l)-1])
    before_entropy = 1
    tree = {}
    keys = []
    recursive_split(data, attributes, last_column, before_entropy, tree, keys)
    print("The Tree: \n\n")
    full_attr = ["Alternate", "Bar", "Fri/Sat", "Hungry", "Patrons", "Raining", "Reservation", "Type", "WaitEstimate"]
    path = []
    for k in keys:
        for f in full_attr:
            if f.find(k.split()[0]) != -1 and f not in path:
                path.append(f)
    popcount = 0
    for p in path:
        print("             " +p)
        print("\n")
        for k in keys:
            if p.find(k.split()[0]) != -1:
                if tree[k][0] != "node":
                    print(tree[k][1],end="      ")
                else:
                    print(str(tree[k][2]) + "(NODE)",end="          ")
        print("\n\n")
        for k in keys:
            if p.find(k.split()[0]) != -1:
                if tree[k][0] != "node":
                    print(tree[k][0],end="               ")
                else:
                    print(tree[k][1],end="               ")
        print("\n\n\n")








if __name__=="__main__":
    main(sys.argv[0:])
