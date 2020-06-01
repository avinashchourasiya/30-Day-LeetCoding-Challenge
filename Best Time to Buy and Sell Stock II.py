arr=[5,11,3,50,60,90];
sell=1;
buy=0;
total_profit=0

for sell in range(len(arr)):
    if(arr[buy]>arr[sell]):
        buy=sell;
    else:
        if(arr[sell]-arr[buy]>0):
            total_profit+=(arr[sell]-arr[buy]);
            buy=sell;

print(total_profit);




# print(best_price);
# print(m);


