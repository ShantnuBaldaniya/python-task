def can_partition(nums) :
    total = sum(nums)


    if total % 2 != 0:
        return False

    target = total // 2
    possible = {0}   

    for num in nums:
        new_sums = set()
        for s in possible:
            new_sums.add(s + num)
        possible |= new_sums

    return target in possible
result=can_partition([1,2,3,6])
print(result)

