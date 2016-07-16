"""

118. Pascal's Triangle

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""

class Solution(object):

    def generate(self, num_rows):
        result = []
        for i in range(num_rows):
            result.append([])
            for j in range(i + 1):
                if j in (0, i):
                    result[i].append(1)
                else:
                    result[i].append(result[i - 1][j - 1] + result[i - 1][j])
        return result



if __name__ == '__main__':
    num_rows = 5
    result = Solution().generate(num_rows)
    print(result)
