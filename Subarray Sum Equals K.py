# from collections import defaultdict
# nums = [9, 4, 20, 3, 10, 5];
# k = 33;
# s=0;
# c=0;
# d=dict()
# d[0]=1;
# for index,number in enumerate(nums):
#     s+=number;
#     if((s-k) in d):
#         d[s]=1;
#         print(s,end=' ');
#         c+=1;
#     else:
#         d[s]=1;
#
# print(d)
# print(c)

#
# [0,0,0,0,0,0,0,0,0,0]
# 0
# op:10;
# expected=55


class Solution:
    def subarraySum(self, nums):
        dic = {0:1}
        k=0
        cumsum = [None]*(len(nums)+1)
        cumsum[0] = 0
        count = 0
        for i in range(1,len(nums)+1):
            cumsum[i] = cumsum[i-1] + nums[i-1]
            if cumsum[i]-k in dic:
                count += dic[cumsum[i]-k]
            if cumsum[i] in dic:
                dic[cumsum[i]] += 1
            else:
                dic[cumsum[i]] = 1
            print(count)
        return count




s=Solution().subarraySum([0,0,0,0,0,0,0,0,0,0]);
print(s)



















