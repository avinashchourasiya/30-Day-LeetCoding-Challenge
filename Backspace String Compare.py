s=list(input());
t=list(input());
s_arr=[];
s_arr2=[];

for i in range(len(s)):
    if(s[i]=='#'):
        if(len(s_arr) > 0):
            s_arr.pop(-1);
    else:
        s_arr.append(s[i]);

for i in range(len(t)):
    if(t[i]=='#'):
        if(len(s_arr2) > 0):
            s_arr2.pop(-1);
    else:
        s_arr2.append(t[i]);

print(s_arr==s_arr2);








