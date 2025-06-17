class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atMostK(nums, k):
            count = 0
            start = 0
            freq = {}
            for end in range(len(nums)):
                if nums[end] in freq:
                    freq[nums[end]] += 1
                else:
                    freq[nums[end]] = 1

                while len(freq) > k:
                    freq[nums[start]] -= 1
                    if freq[nums[start]] == 0:
                        del freq[nums[start]]
                    start += 1
                
                count += end - start + 1
            
            return count


        return atMostK(nums,k) - atMostK(nums, k-1)