class Solution {
public:
    double average(vector<int>& salary) {
        sort(salary.begin(), salary.end());
        double sum, average;
        for(int i = 1; i < salary.size()-1; i++){
            sum = sum + salary[i];
        }
        average = sum/(salary.size()-2);
        return average;       
    }
};