class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = {}
        invertFreq = [[] for i in range(len(nums)+ 1)]
        
        for n in nums:
            numFreq[n] = numFreq.get(n, 0) + 1
        
        for n,c in numFreq.items():
            invertFreq[c].append(n)
            
        res = []
        for i in range(len(invertFreq)-1, -1, -1):
            for n in invertFreq[i]:
                res.append(n)
                
                if len(res) == k:
                    return res
        
        return res
        
        
        
        