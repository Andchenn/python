# 快速排序
def qsort(nums):
    if len(nums) <= 1:
        return nums
    #
    less = []
    greater = []
    base = nums.pop()

    for x in nums:
        if x < base:
            less.append(x)
        else:
            greater.append(x)

    return qsort(less) + [base] + qsort(greater)


if __name__ == '__main__':
    nums = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    print(qsort(nums))
