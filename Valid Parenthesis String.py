class Valid_Parenthesis_String:
    def checkValidString(self,s):
        s='()*))*(';
        stack=[];
        star=[];
        if(len(s)==0 or s=='*'):
            return(True);
        for i in range(0,len(s)):
            if(s[i]=='('):
                stack.append(i);
            elif(s[i]==')' and len(stack)>0):
                stack.pop();
            elif(s[i]=='*'):
                star.append(i);
            elif(s[i]==')' and len(star)==0 and len(stack)==0):
                return False;
            elif(s[i]==')' and len(star)>0 and star[-1]<i):
                star.pop();
        print(stack);
        print(star);

v=Valid_Parenthesis_String()
print(v.checkValidString(''));











