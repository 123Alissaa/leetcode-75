class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res = []
        max_candy = max(candies)
        i = 0
        for candy in candies:
            candies[i] += extraCandies
            if candies[i] >= max_candy:
                res.append(True)
            else:
                res.append(False)
            i += 1
        return res