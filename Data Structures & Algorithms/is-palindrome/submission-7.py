class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        index = 0
        right = (len(s)-1)
        while (index < right):
            print(s[index], s[right])
            if s[index].lower().isalnum() and s[right].lower().isalnum():
                if s[index].lower() != s[right].lower():
                    return False;
                index += 1
                right -= 1
            elif not s[index].isalnum():
                index += 1
            else:
                right -= 1
            
        return True;

