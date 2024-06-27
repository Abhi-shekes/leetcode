class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        mapping = {}
        
        for index in range(len(edges)):
            for element in edges[index]:
                if element not in mapping:
                    mapping[element] = 1
                else:
                    mapping[element] = mapping[element] + 1
                    
        return  max(mapping, key=mapping.get)
        