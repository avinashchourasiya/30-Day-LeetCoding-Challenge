arr=["eat", "tea", "tan", "ate", "nat", "bat"];
d={};

for index,strs in enumerate(arr):
    s=''.join(sorted(strs));
    # print(s);
    if(s in d):
        d[s].append(strs);
        # pass;
    else:
        d[s]=[strs];

print(d)
arr=[]
for k,v in d.items():
    arr.append(v);
print(arr);
