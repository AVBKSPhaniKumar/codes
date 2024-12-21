


A = [(1,"a"),(1,"b"),(1,"c"),(2,"a"),(2,"b"),(2,"c")]


from collections import Counter


# A = [1,2,3,4]
final_set = {}


for i in range(0,len(A)+1):
    final_set[i]=[]

print("final_set >> ", final_set)




for i,list_ in final_set.items():
    if i<len(A):
        tmp = []
        if i==0:
            tmp = [[n] for n in A]
        else:
            print(f"sets with size{i+1}>> ")
            counter_list = []
            for ele1 in list_:
                print("ele1 >> " , ele1, type(ele1))
                for ele in A:
                    print("ele >> ", ele)
                    if ele not in ele1:
                        x = ele1+[ele] #ele1.append(ele)
                        #print(ele1+[ele])
                        c = Counter(x)
                        print("x >> ",x)
                        print("c >> ",c)
                        if c in counter_list:
                            pass
                        else:
                            counter_list.append(c)
                            tmp.append(x)
                    print("tmp >> ", tmp)
        final_set[i+1] = tmp
        
    print(final_set)

final_set[0] = []
print(final_set)
total = 0
for i,set_ in final_set.items():
    print(i, ">> ",len(set_))
    total+=len(set_)
print("total >> ", total)


        


        
