s="xqgwkiqpif"
shift=[[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]
left=0;right=0;rotate=0;
for i in shift:
    if(i[0]==0):
        left+=i[1];
    else:
        right += i[1];

if(left==right):
    print(s);
elif(right>left):
    rotate=(right - left)
    rotate = rotate % len(s);
    print(s[len(s)-rotate:len(s)]+s[0:len(s)-rotate]);
else:
    rotate = (left - right)
    rotate = rotate % len(s);
    s=s[::-1];
    # print(s);
    print((s[len(s) - rotate:len(s)] + s[0:len(s) - rotate])[::-1]);




























