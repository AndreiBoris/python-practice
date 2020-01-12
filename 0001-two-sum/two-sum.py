from typing import List

# We are going to want to go through each of these and sum it with all other numbers with a later index to see if they
# add up, storing the indexes as we go

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    answer = None

    currentIndex1 = 0
    currentIndex2 = 0
    for number1 in nums:
      currentIndex2 = currentIndex1 + 1
      allFollowingNumbers = nums[currentIndex2:]
      for number2 in allFollowingNumbers:
        if number1 + number2 == target:
          answer = [currentIndex1, currentIndex2]
          break
        currentIndex2 += 1

      if answer is not None:
        break

      currentIndex1 += 1

    return answer

solver = Solution();

solution = solver.twoSum([1, 2, 3, 4, 5], 5);

print(solution);