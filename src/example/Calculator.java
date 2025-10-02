package example;

public class Calculator {

    public int add(int a, int b) {
        return a + b;
    }

    public int subtract(int a, int b) {
        return a - b;
    }

    public int multiply(int a, int b) {
        int ans=0;
        for(int i = 0; i < b; i++){
            ans += a;
        }
        return ans;
    }

    public String checkPositive(int a) {
        if (a > 0) {
            return "Positive"; // 分岐の一方
        } else {
            return "Not Positive"; // 分岐のもう一方
        }
    }
}