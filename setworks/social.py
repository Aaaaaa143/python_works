all_users=["mammoty","mohanlal","prithvi","asif","dq","fahad","nivin"]
nivin_friends=["asif","dq","fahad"]

# nivins suggestions

st1=set(all_users)
st2=set(nivin_friends)
suggestions=st1.difference(st2)
suggestions.discard ("nivin")
print(suggestions)

dq_friends=["mammoty","asif","fahad","mohanlal"]

#mutual friends of nivin and dq

mutal_friends=st2.intersection(dq_friends)
print(mutal_friends)

