
class Solution:
    def footballScores(teamA, teamB):
        res = []

        teamA.sort()

        for i in range(len(teamB)):
            right = len(teamA) - 1
            left = 0

            while left <= right:
                mid = (left + right) // 2
                if teamA[mid] > teamB[i]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            res.append(left)


        return res


if __name__ == '__main__':
    teamA = [1, 2, 3]
    teamB = [2,4]
    result = Solution.footballScores(teamA, teamB)
    print(result)