
class Solution:
    def lastStoneWeight(self, stones):
        arr=stones
        l=len(arr);
        i=0;
        j=1;
        # print(arr)
        while arr:
            arr.sort(reverse=True);
            #print(arr);
            if(len(arr)==1):
                return(arr[0]);
                #break;
            elif(arr[i]==arr[j]):
                arr.pop(0);
                arr.pop(0);
            elif(arr[j] != arr[i]):
                arr.append(arr[i]-arr[j]);
                arr.pop(j);
                arr.pop(i);
        if(len(arr)==0):
            return(0);
s=Solution();
print(s.lastStoneWeight([2,3]));

