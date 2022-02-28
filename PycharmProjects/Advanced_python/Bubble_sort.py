def Bubble_sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp

    return nums



list1=[1,4,2,8,3,9,7,5,0]
print(Bubble_sort(list1))