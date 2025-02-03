l=[10,20,30]
s=set(l)
print(s)

st={5,6,7,8,9}
st.add(10)
print(st)

print(st.pop())
print(st)

st.remove(6)
print(st)

st.discard(7)
print(st)

st.update(l)
print(st)

st.clear()
print(st)