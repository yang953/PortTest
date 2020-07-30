# nums = [1,2,7,8,12,14,9,9,10,3,9]
#
# b = [(index,value) for index,value in enumerate(nums)]
#
# print(b[0][1])
    # list_num = []
    # list_num.append(index)
    # list_num.append(value)
    # b = b+list_num
    # print(list_num)
    # print(b)
def towSum(nums,target):
    index_list = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                index_list.append(i)
                index_list.append(j)
    print(list(set(index_list)))


# def tow_num(num_list,target):
#     # 获取列表中所有数字的数组下标，并与数字成字典
#     index_1 = [[index_1,value_1] for index_1,value_1 in enumerate(num_list)]
#     list_sum = []
#     for i in index_1:
#         for j in index_1:
#             if j!=i :
#                 if i[0][1] + j[0][1] == target:
#                     print(i,j)
#
#
#             # print(i,j)
#
#
#
if __name__=="__main__":
    towSum([1,2,3,6,12,52,3,12,4,5],9)