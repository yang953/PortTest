import os
a = [
    {"yoyo1": "123456"},
    {"yoyo2": "123456"},
    {"yoyo3": "123456"},
]

h = open(r'H:\Python\PortTest\1.txt',mode="w")

for i in a:
    for k in i.keys():
        h.write(k+",")
        for v in i.values():
            h.write(v+"\n")

h.close()