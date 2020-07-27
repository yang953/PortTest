#
# # a = []
# a = 0
# for i in range(1,1000):
#     s = 0
#     for j in range(1,i):
#         if i%j==0:
#             s = s+j
#             a = a+j
#     # if i==s:
#     #     print(i)
#     print(a,s)

# a = 0
for i in range(1,1001):
    s = 0 # 每次循环重置s值
    for j in range(1,i):
        if i%j==0:
            s = s+j
            # a = a+j
    if i==s:
        print(i)
    # print(a,s,i)