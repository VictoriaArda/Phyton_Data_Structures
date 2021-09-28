# Time : 0(n) // Space : 0(n)

def twoNumberSum (array , targetSum):
    nums ={}
    for num in array:
        if targetSum- num in nums:
            return [targetSum-num ,num] 
        else:
            nums[num]= True 
    return[]  

##################################################
