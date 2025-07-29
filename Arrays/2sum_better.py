"""
🔍 Problem: 2 Sum (Better Approach)

🕒 Time Complexity: O(n)
🧠 Space Complexity: O(n)

💡 Logic:
- For each number in the list, calculate the number you need to reach the target.
- If that number was already seen, return the pair.
- Otherwise, store the current number for future lookup.
"""


nums = [2, 6, 5, 8, 1]
target = 14


def better_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target-num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []


result = better_sum(nums, target)
print("indices of the number", result)
