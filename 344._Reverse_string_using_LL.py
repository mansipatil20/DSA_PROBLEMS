class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def revList(left, right):
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            revList(left+1, right-1)
        revList(0,len(s)-1)