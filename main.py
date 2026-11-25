def unique_parcel(nums):
    d={}
    for i in nums:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    result=[]
    for i in nums:
        if d[i]==1:
            result.append(i)
        
        
    if not result:
        return None
    return result                        
print(unique_parcel([101,102,103,101,104,105,102,106]))
print(unique_parcel([7,7,8,8,9,9]))
