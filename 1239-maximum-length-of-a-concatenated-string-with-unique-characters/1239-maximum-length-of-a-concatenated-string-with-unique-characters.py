class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.max_len = 0
        def comb(ind,a):
            if len("".join(a)) == len(set("".join(a))):
                self.max_len = max(self.max_len,len("".join(a)))
            if ind == len(arr):
                return    
            a.append(arr[ind])
            comb(ind + 1,a)
            a.pop()
            comb(ind + 1,a)
        
        comb_arr = []
        comb(0,[]) 
        print(self.max_len)         
        return self.max_len
        