```
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

```

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            start = [1] * (i+1)
            res.append(start)
            for j in range(1,i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res
