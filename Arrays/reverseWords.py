class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = s.strip()
        words = s.split()
        reversed_s = words[::-1]

        return ' '.join(reversed_s)