def isbalanced(s):
    stk=[]
    pairs={'}':'{',']':'[',')':'('}
    for val in s:
        if val in '{[(':
            stk.append(val)
        elif val in ']})':
            if not stk or stk[-1]!=pairs[val]:
                return 'not balanced'
            else:
                stk.pop()
                return 'balanced' if len(stk)==0 else 'not balanced'
if __name__=="__main__":
    s=input()
    print(isbalanced(s))
     