# coding: utf-8

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
llist = []
for ss in s.split(" "):
    llist.append(len(ss.strip(".")))
print llist
