class Solution:
    def minimumPushes(self, word):
        
        count_varible = {}
        
        for alpha in word:
            if alpha in count_varible:
                count_varible[alpha] = count_varible[alpha] + 1
            else:
                count_varible[alpha] = 1

        count_varible = sorted(count_varible, key=count_varible.get, reverse=True)

        new_words = ""
        for alpha in count_varible:
            new_words +=alpha
        
        mapping = {}
        mapped = []
        counter = 2
        for alpha in new_words:
            if alpha not in mapped:
                if counter not in mapping:
                    mapping[counter] = [alpha]
                else:
                    mapping[counter].append(alpha)
                mapped.append(alpha)
                if counter ==9:
                    counter = 2
                else:
                    counter+=1
        
        total = 0
        
        for alpha in word:
            for button, values in mapping.items():
                if alpha in values:
                    total = total + values.index(alpha) + 1
        return total
        

        