class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        f = 1
        for n in arr:
            if f == n:
                f += 1
            else:
                if n - f < k:
                    k -= n - f
                    f = n+1
                else:
                    return f + k

        return f + k

print(Solution().findKthPositive(arr = [2,3,4,7,11], k = 5))