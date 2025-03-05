"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""
# ==============================first sloution=============================


class SloutionOne:
    def twosum(self, num:list[int], target:int)->list[int]:
        n = len(num)
        for i in range(n):
            for j in range(i+1 , n):
                if num[i] + num[j] ==target:
                    return[i,j]

s1= SloutionOne()
s1v=s1.twosum([2,7,11,15],9)
print(s1v)

# ==============================first sloution=============================


class SloutionTwo:
    def twosum(self, num:list[int], target:int)->list[int]:
        num_to_index = {}
        for i, num in enumerate(num):
            complement = target - num

            if complement in num_to_index:
                return [num_to_index[complement], i]

            num_to_index[num] = i

s2= SloutionTwo()
s2v=s2.twosum([2,7,11,15],9)
print(s2v)
