class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # count = len(s)
        rev_s = []
        while not s:
            rev_s.append(s.pop())

        for i in len(rev_s):
            s.append(rev_s[i])