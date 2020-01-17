```
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

[示例] 1:

输入: 4
输出: 2

[示例] 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
```

#二分法。一个数的平方根小于或等于它的一半。不断二分。

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left = 1
        right = x // 2

        while left < right:
            # 有一个“+1”是为了避免最后left、right只有2个元素时陷入死循环
            # 看了大佬的方法，中位数取法有一种“右移的方法”。。
            # mid = (left + right + 1) >> 1
            mid = (left + right + 1) // 2
            square = mid * mid

            if square > x:
                right = mid - 1
            else:
                left = mid
        return left
