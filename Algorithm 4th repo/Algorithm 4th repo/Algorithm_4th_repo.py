import random
import timeit
import sys
import csv
import operator

#Array1_RD=[]
#Array2_RD=[]
#Array3_RD=[]
#Array1_RV=[]
#Array2_RV=[]
#Array3_RV=[]

#def swap(data, i, j):
#    data[i], data[j] = data[j], data[i]

#for i in range(1000):
#    Array1_RV.append(1000-i)
#    Array1_RD.append(random.randrange(1,1001))
#for i in range(10000):
#    Array2_RV.append(10000-i)
#    Array2_RD.append(random.randrange(1,10001))
#for i in range(100000):
#    Array3_RV.append(100000-i)
#    Array3_RD.append(random.randrange(1,100001))

#Array_temp=[]
#def printresult(Method,array):
#    Array_temp=list(array)
#    start = timeit.default_timer()
#    Method(Array_temp)
#    end=timeit.default_timer()
#    sys.stdout.write(str(round(end-start,3)))
#    sys.stdout.write("\t\t")

#def heapify(unsorted, index, heap_size):
#    largest = index
#    left_index = 2 * index + 1
#    right_index = 2 * index + 2
#    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
#        largest = left_index
#    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
#        largest = right_index
#    if largest != index:
#        swap(unsorted,largest, index)
#        heapify(unsorted, largest, heap_size)

#def heap_sort(unsorted):
#    n = len(unsorted)
#    for i in range(n // 2 - 1, -1, -1):
#        heapify(unsorted, i, n)
#    for i in range(n - 1, 0, -1):
#        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
#        heapify(unsorted, 0, i)
#    return unsorted

#print("\t\tRandom1000\tReverse1000\tRandom10000\tReverse10000\tRandom100000\tReverse100000")
#sys.stdout.write("Heap\t\t")
#printresult(heap_sort,Array1_RD)
#printresult(heap_sort,Array1_RV)
#printresult(heap_sort,Array2_RD)
#printresult(heap_sort,Array2_RV)
#printresult(heap_sort,Array3_RD)
#printresult(heap_sort,Array3_RV)
#print()
#sys.stdout.write("Python_sorted\t")
#printresult(sorted,Array1_RD)
#printresult(sorted,Array1_RV)
#printresult(sorted,Array2_RD)
#printresult(sorted,Array2_RV)
#printresult(sorted,Array3_RD)
#printresult(sorted,Array3_RV)


# 2번 문제
switch =1 
sortValue=-1
while(switch):
    IR=input("$ ")
    IR=IR.split(' ')
    if IR[0]=="read":
        filename=IR[1]
        infile = open(filename, "r") 
        log = csv.reader(infile, delimiter = ',') 
        log_temp=list(log)
        Values=log_temp.pop(0)
    elif IR[0]=="sort":
        if IR[1]=="-t": # 정렬하는 기준을 선택
            sortValue=1
        elif IR[1]=="-ip":
            sortValue=0
        else:
            print("제대로 된 조건을 넣어서 sort 해주세요")
            continue
        sortedlist = sorted(log_temp, key=operator.itemgetter(sortValue), reverse=False)
    elif IR[0]=="print":
        if sortValue is -1:
            print("먼저 sort를 진행해주세요.")
            continue
        #print(Values)
        for line in range(len(sortedlist)):
            if sortValue is 0:
                print(sortedlist[line][sortValue])
                print("\tTime : ",sortedlist[line][1].split("[")[1])
                print("\tURL : ",sortedlist[line][2])
                print("\tStatus : ",sortedlist[line][3])
            elif sortValue is 1:
                print(sortedlist[line][sortValue].split("[")[1])
                print("\tIP : ",sortedlist[line][0])
                print("\tURL : ",sortedlist[line][2])
                print("\tStatus : ",sortedlist[line][3])

    elif IR[0]=="exit":
        break
infile.close()

