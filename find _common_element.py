class Solution:
    def intersect(self, num1, num2):
        num1.sort()
        num2.sort()

        index1 = 0
        index2 = 0

        result = []

        if num1 and num2:
            while index1 != len(num1) and index2 != len(num2):
                if num1[index1] < num2[index2]:
                    index1 += 1
                elif num1[index1] > num2[index2]:
                    index2 += 1
                elif num1[index1] == num2[index2]:
                    result.append(num1[index1])
                    index2 += 1
                    index1 += 1

        return result