import java.util.*;

class Solution {
    public int solution(int n) {
        ArrayList <Integer> answer = new ArrayList<>();
        
        for (int i = 1; i < n; i++) {
            if (n % i == 1) {
                answer.add(i);
            }
        }
        
        int a = Collections.min(answer);
        

        
        return a;
    }
}