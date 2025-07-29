"""
🔍 Problem: 2 Sum (Brute Force Approach)
- Check every pair of numbers in the array
- If their sum equals the target, return their indices

🕒 Time Complexity: O(n^2)
🧠 Space Complexity: O(1)
"""


array = [2, 6, 5, 8, 1]
target = 14
n = len(array)
for i in range(n):
    for j in range(i+1, n):
        if (array[i]+array[j] == target):
            print("yes", i, j)
            exit()
else:
    print("no")
