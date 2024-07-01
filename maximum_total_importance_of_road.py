class Solution:
    def maximumImportance(self, n, roads) :
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        
        cities = list(range(n))
        cities.sort(key=lambda x: degree[x], reverse=True)
        
        values = [0] * n
        current_value = n
        for city in cities:
            values[city] = current_value
            current_value -= 1
        
        total_importance = 0
        for a, b in roads:
            total_importance += values[a] + values[b]
            
            
        return total_importance