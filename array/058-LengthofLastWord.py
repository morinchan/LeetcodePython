```
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。

如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、不包含任何空格的 最大子字符串。

 

[示例]1:

输入: "Hello World"
输出: 5

[示例]2:

输入: "a "
输出: 1


```

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s)==0:
            return 0
        str1 = s.split(' ')
        #需要加一个循环，不然如果最后一个空格后没有单词，就会输出0
        for i in reversed(range(len(str1))):
            if len(str1[i])==0:
                continue
            else:
                return len(str1[i])
        return 0
