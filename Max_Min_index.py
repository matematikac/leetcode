Array=[2,4,51,3,1,0]
Min= Array[0]
Max=Array[0]
max_ind=0
min_ind=0
#print(Max, Min,max_ind)
for i in range(len(Array)):
        if Array[i]>Max:
            Max=Array[i]
            max_ind=i
for i in range(len(Array)):
        if Array[i]<Min:
            Min = Array[i]
            min_ind =i

print("Maximalan element je:",Max,"a njegov indesk je:",max_ind ,'\n',"Minimalan element je:",Min,"a njegov indeks je:", min_ind)