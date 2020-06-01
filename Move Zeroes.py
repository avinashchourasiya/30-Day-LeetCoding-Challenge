# def movezero(arr):
#     z=arr.count(0);
#     while(0 in arr):
#         arr.remove(0);
#     for i in range(z):                               # solution 1
#         arr.insert(len(arr),0);
#     return (arr);
#
# arr=[0,1,0,3,12];
# print(movezero(arr))



# one=[1,2,3,4];
# two=[0,0];                                           # solution 2
# print(one+two);


arr=[1,8 ,0,3,0, 12, 5];
ind=0;rev=0;
for i in range(len(arr)):
    if(arr[i] != 0):
        arr[ind]=arr[i];
        ind+=1;
        print(arr,'==',ind);
    else:rev+=1;
for i in range(1,rev+1):
    arr[-i]=0;
print(arr)























