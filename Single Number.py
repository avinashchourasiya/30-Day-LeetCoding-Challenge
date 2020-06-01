# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# arr=[int(x) for x in input().split(' ')];
#
# x=0;
# for i in arr:
#     print(int(x^i));
#
# from collections import Counter
# arr=[4,1,2,1,2]
# arr1=dict(Counter(arr));
# m=1;key=0;
# for k,v in arr1.items():
#     if(v<=m):                                          #solution 1 my
#         # print(k,v);
#         m=v;
#         key=k;
# print(key)

arr=[4,2,1,1,3,6,5];            #   this solution works only if the all the number occures 2 time and only 1 number occur 1
x=0;
for i in arr:
    x^=i
    # print(x);
print('ans=',x)





















