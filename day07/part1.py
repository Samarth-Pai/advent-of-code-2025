with open("input.txt") as f:
    lines = f.read().splitlines()
    
q = set([lines[0].index("S")])
ans = 0
for line in lines[1:]:
    st = set()
    for i in q:
        if line[i] == '^':
            ans += 1
            st.add(i-1)
            st.add(i+1)
        else:
            st.add(i)
    q = st
print(ans)