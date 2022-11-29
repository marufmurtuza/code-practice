class Solution {
public:
    int subtractProductAndSum(int n) {
        int product=1;
        int sum=0;
        while(n){
            product *= n%10;
            sum += n%10;
            n /= 10;
        }
        return (product-sum);     
    }
};