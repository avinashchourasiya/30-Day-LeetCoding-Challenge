#Navie Approch
# arr=[1, 0, 3];
# l=len(arr)
# s=0;
# length=0;
#
# m=0;
# for i in range(l):
#     c = 0;
#     s=0;
#     for j in range(i,l):
#         s+=arr[j];
#         c+=1;
#         if(s==0):
#             m=max(m,c);
# print(m)

#Best Approch
# arr=[int(x) for x in input().split(' ')];
arr=[15, -2, 2, -8, 1, 7, 10, 23]
sum=0;
d=dict();
d[0]=-1;
val=0;
m=0;
for index,nums in enumerate(arr):
    sum+=nums;
    print(sum)
    if(sum in d):
        val=index-d[sum];
        m=max(m,val);
    else:
        d[nums]=index;
print(d)
print(m)

























