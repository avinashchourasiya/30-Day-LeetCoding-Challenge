c_s=0;
b_s=0;
arr=[-2,-3,-4,-1];
for i in arr:
    c_s+=i;
    if(c_s<0):
        c_s=0;
    if(c_s>b_s):
        b_s=c_s;

if(b_s==0):
    arr.sort(reverse=True);
    print(arr[0]);
else:print(b_s);


