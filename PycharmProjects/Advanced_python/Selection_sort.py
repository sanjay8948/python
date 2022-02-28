def Selection_sort(nums):
    for i in range(len(nums)-1):
        minpos=i
        for j in range(i,len(nums)):
            if nums[minpos]>nums[j]:
                minpos=j
        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp
    return nums



list1=[1,4,2,8,3,9,7,5,0]
print(Selection_sort(list1))