# 引入舍伍德算法消除快速排序中输入数据对时间复杂度的影响
import random


def quickSort(left, right, list):
    if(left < right):
        randomLeft = left                                           # 随机产生一个范围在当前列表内的整数
        randomBase = random.randint(left, right)

        randomTemp = list[randomLeft]                        # 将随机选出的元素交换至最左侧设为基准数
        list[randomLeft] = list[randomBase]
        list[randomBase] = randomTemp

        mid = partition(left, right, list)                                # 进行排序运算，找出当前轮次基准数的位置
        quickSort(left, mid-1, list)                                      # 分治
        quickSort(mid+1, right, list)


def partition(l, r, list):                                                # 快速排序
    i = l
    j = r
    averageLocation = len(list[l]) - 1
    temp = list[l][averageLocation]

    while i!=j:                                                     # 找出比基准数小和大的数，分别排至基准数左右
        while list[j][averageLocation] <= temp and j > i:
            j -= 1
        while list[i][averageLocation] >= temp and i < j:
            i += 1
        temp2 = list[i]
        list[i] = list[j]
        list[j] = temp2

    temp3 = list[l]                                          # 将位于列表最左侧的基准数交换至其应该在的位置
    list[l] = list[i]
    list[i] =temp3
    return i