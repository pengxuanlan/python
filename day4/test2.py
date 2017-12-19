list_1 =['alex','eric','rain']
list_2=''
for i in range(len(list_1)):
    if i==0:
        list_2=list_1[i]
    else:
        list_2=list_2+"_"+list_1[i]
print (list_2)
#list_2=list_2.strip('_')
#print(list_2)
