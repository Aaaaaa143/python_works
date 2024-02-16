words="pneumonoultramicroscopicsilicovolcanoconiosis"
v_count=0
c_count=0
for ch in words:
    if ch.startswith("a") or ch.startswith("e") or ch.startswith("i") or ch.startswith("o") or ch.startswith("u"):
        v_count+=1
    elif ch.isalpha():
        c_count+=1
print(f"vowels count= {v_count} and consonents count={c_count}") 