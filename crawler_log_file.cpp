#include <iostream>
#include <vector>
#include <string>

class Solution {
public:
    int minOperations(std::vector<std::string>& logs) {
        int res = 0;

        for (const std::string& log : logs) {
            if (log == "../") {
                if (res > 0) {
                    res--;
                }
            } else if (log != "./") {
                res++;
            }
        }

        return res;
    }
};

int main() {
    Solution solution;
    std::vector<std::string> logs = {"d1/", "d2/", "../", "d21/", "./"};
    int result = solution.minOperations(logs);
    std::cout << "Minimum operations: " << result << std::endl;
    return 0;
}
