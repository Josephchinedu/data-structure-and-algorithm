def maxSubArray(nums) -> int:
    current_sum = 0
    max_sum = min(nums)
    print(max_sum)

    for i in range(0, len(nums)):
        current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum

        if current_sum < 0:
            current_sum = 0

    return max_sum


if __name__ == "__main__":
    print(maxSubArray([5, 4, -1, 7, 8]))
