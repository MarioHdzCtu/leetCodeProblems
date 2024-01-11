nums = [1,2,3,4,5,6,7,8,9,10]

def runningSum(nums: list[int]) -> list[int]:
    """Calculates the running sum of a 1D array

    Args:
        nums (list): The 1D array as a list where len(nums) < 0 && len(nums) > 1000

    Returns:
        list: the running sum for each element
    """
    sum_ = 0
    for idx,n in enumerate(nums):
        sum_ = sum_ + n
        nums[idx] = sum_
    
    return nums

print(runningSum(nums=nums))
