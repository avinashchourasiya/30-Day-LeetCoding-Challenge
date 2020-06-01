arr=[4,5,1,8,2];
# print(arr);
l=len(arr);
l_r_arr=[1]*l;
r_l_arr=[1]*l;


for i in range(0,len(arr)-1):
    val=arr[i]*l_r_arr[i];
    l_r_arr[i+1]=val;
# print(l_r_arr);

for i in range(l-1,0,-1):
    val=arr[i]*r_l_arr[i];
    r_l_arr[i-1]=val;
# print(r_l_arr);


for i in range(0,l):
    arr[i]=r_l_arr[i]*l_r_arr[i]

print(arr)
