class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums) 
        enum = list(enumerate(nums))

        def merge_sort(arr):
            if len(arr) < 2:
                return arr
            mid = len(arr)//2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)
        
        def merge(left, right):
            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    merged.append(left[i])
                    res[left[i][0]] += j
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            
            while i < len(left):
                merged.append(left[i])
                res[left[i][0]] += j
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1
            
            return merged
        
        merge_sort(enum)
        return res