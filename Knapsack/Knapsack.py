memo={}
parent=[]
def DP(val,s,i,x):
    if i==len(val) or x==0:
        return 0
    if i in memo:
        return memo[(i,x)]
    #Not Possible to be added
    if s[i]>x:
        memo[(i,x)]=DP(val,s,i+1,x)
        return memo[(i,x)]
    else:
        #Not Added
        if DP(val,s,i+1,x)>val[i]+DP(val,s,i+1,x-s[i]):
            memo[(i,x)]=DP(val,s,i+1,x)
        #Added
        else:
            memo[(i,x)]=val[i]+DP(val,s,i+1,x-s[i])
            if i not in parent:
                parent.append(i)
        return memo[(i,x)]
        

'''Driver Program'''
val=[4,2,2,1,10]
s=[12,1,2,1,4]
size=15
value=DP(val,s,0,size)
print('Maximum Value:',value)
print('Subset:',end=' ')
for i in sorted(parent):
    print(val[i],end=' ')
