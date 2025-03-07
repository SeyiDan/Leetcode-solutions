class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the list
        result = []  # Using List to store values without duplicates

        # Loop to iterate through elements up till the 3rd to the last
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for the current element
                continue

            # Initialize pointers
            left = i + 1
            right = len(nums) - 1

            # Condition to find triplets
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # Avoid duplicates for the `left` pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Avoid duplicates for the `right` pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result





