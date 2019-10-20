ass Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def is_subsequence(sub, string):
            # Base cases
            if sub == '':
                return True
            if sub != '' and string == '':
                return False
            # General case
            if sub[0] == string[0]:
                return is_subsequence(sub[1:], string[1:])
            else:
                return is_subsequence(sub, string[1:])
        
        def longer(w1, w2):
            if len(w1) == len(w2):
                return w1 if w1 < w2 else w2
            return w1 if len(w1) > len(w2) else w2
            
        if d == []:
            return ''
        
        if is_subsequence(d[0], s):
            return longer(d[0], self.findLongestWord(s, d[1:]))
        else:
            return self.findLongestWord(s, d[1:])
        
    
