class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        index = 0
        words = list(s.lower().replace(" ", ""))
        while (index + 1 <= len(words)/2):
            print(words[index], words[len(words) - index-1])
            if words[index].isalnum() and words[len(words) - index-1].isalnum():
                
                if words[index] != words[len(words) - index-1]:
                    return False;
                index += 1
            elif not words[index].isalnum():
                words.pop(index)
            else:
                words.pop(len(words) - index-1)
            
        return True;

