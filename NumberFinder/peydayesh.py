
def find(num1, num2, num3):
    nums = [1,2,3,4] 
    
    nums.remove(num1)
    nums.remove(num2)
    nums.remove(num3)

    result = int(nums[0])
    return result

print(find(1, 4, 3))
