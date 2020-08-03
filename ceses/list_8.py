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


def tow_num(num_list,target):
    # 获取列表中所有数字的数组下标，并与数字成数组
    index_1 = [[index_1,value_1] for index_1,value_1 in enumerate(num_list)]
    list_sum = []
    # list_index = []
    for i in range(len(index_1)):
        for j in range(i+1,len(index_1)):
            if index_1[i][1] + index_1[j][1] == target :
                if index_1[i]  not in list_sum:
                    list_sum.append(index_1[i])
                    if index_1[j] not in list_sum:
                        list_sum.append(index_1[j])
                    # print(list_sum)
    # for x in list_sum:
    #     list_index.append(x[0])
    list_index = [x[0] for x in list_sum]
    c = [list_index[i:i+2] for i in range(0,len(list_index),2)]
    # print(index_1[3] in list_sum)
    # print(list_sum)
    print(c)
    print(list_index)

if __name__=="__main__":
    # towSum([1,2,3,6,12,52,3,12,4,5],9)
    tow_num([1,2,3,6,12,52,3,12,4,5],9)