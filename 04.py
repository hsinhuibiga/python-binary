#Two Sum

###

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

###

class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        numMap = {} # 初始化字典
        for i in range(len(nums)):
            if numMap.__contains__(target-nums[i]): # 尋找到配對(key值要是target減去當前value)，將其indices進行回傳
                return [numMap.get(target-nums[i]), i]
            else:
                numMap[nums[i]] = i #否則將(num, index)的key/value對放入字典中