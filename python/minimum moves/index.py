#  minimumMoves

class Solution:
    def minimumMoves(self, arr1, arr2):
        
        """
        complete the 'minimumMoves' functiom below

        The function is expected to return an Integer.
        The function accepts following parameters:
        1. INTEGER_ARRAY arr1
        2. INTEGER_ARRAY arr2
        """
        count = 0
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                count += 1
        return count


if __name__ == '__main__':
    arr1 = [123, 543]
    arr2 = [321, 279]
    result = Solution().minimumMoves(arr1, arr2)
    print(result)
        