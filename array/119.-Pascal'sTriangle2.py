```
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

Example:

Input: 3
Output: [1,3,3,1]
```

#利用杨辉三角的公式来做。C(n-1,m) = [m/(n-m+1)]*C(n-1,m-1),第一个和最后一个的值是1，直接循环。

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        value = 1
        for i in range(rowIndex+1):
            res.append(value)
            value = int(value * (rowIndex-i)/(i+1))
        
        return res
