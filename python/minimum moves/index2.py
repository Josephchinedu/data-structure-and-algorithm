
class Solution:
    def minimumMoves(self, arr1, arr2):
        count = 0
        _arr1 = "".join([str(i) for i in arr1])
        _arr2 = "".join([str(i) for i in arr2])

        # _arr1 = arr1
        # _arr2 = arr2

        for i in range(len(_arr1)):
            diff = abs(int(_arr1[i]) - int(_arr2[i]))
            count += diff

        return count

if __name__ == '__main__':
    arr1 = [123, 543]
    arr2 = [321, 279]
    result = Solution().minimumMoves(arr1, arr2)
    print(result)