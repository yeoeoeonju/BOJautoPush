class Solution {

    // 주어진 네 개의 점이 이루는 두 직선이 평행한지 확인하는 메소드
    public int solution(int[][] dots) {
        // 첫 번째와 두 번째 점, 세 번째와 네 번째 점을 이은 직선의 기울기를 비교
        if (gradient(dots[0], dots[1]) == gradient(dots[2], dots[3])) 
            return 1;
        // 첫 번째와 세 번째 점, 두 번째와 네 번째 점을 이은 직선의 기울기를 비교
        else if (gradient(dots[0], dots[2]) == gradient(dots[1], dots[3])) 
            return 1;
        // 첫 번째와 네 번째 점, 두 번째와 세 번째 점을 이은 직선의 기울기를 비교
        else if (gradient(dots[0], dots[3]) == gradient(dots[1], dots[2])) 
            return 1;
        
        // 어떤 경우에도 평행하지 않은 경우 0 반환
        return 0;
    }
    
    // 두 점 간의 기울기를 계산하는 메소드
    public double gradient(int[] arr1, int[] arr2) {
        // 기울기 = (y2 - y1) / (x2 - x1)
        return (arr2[1] - arr1[1]) * 1.0 / (arr2[0] - arr1[0]);
    }
}
