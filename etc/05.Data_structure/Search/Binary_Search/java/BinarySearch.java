public class BinarySearch {

  public static int BSearch(int[] ar, int len, int target) {
    int first = 0; // 탐색 대상의 시작 인덱스
    int last = len - 1; // 탐색 대상의 마지막 인덱스
    int mid;

    while (first <= last) {
      mid = (first + last) / 2; // 중앙 인덱스 계산

      if (target == ar[mid]) { // 중앙값이 타겟과 같다면
        return mid;
      } else {
        if (target < ar[mid]) // 타겟이 더 작다면 왼쪽 반 탐색
        last = mid - 1;
        else // 타겟이 더 크다면 오른쪽 반 탐색
        first = mid + 1;
      }
    }
    return -1; // 탐색 실패 시 -1 반환
  }

  public static void main(String[] args) {
    int[] arr = {1, 3, 5, 7, 9};
    int idx;

    idx = BSearch(arr, arr.length, 7);
    if (idx == -1) System.out.println("탐색 실패");
    else System.out.println("타겟 저장 인덱스: " + idx);

    idx = BSearch(arr, arr.length, 4);
    if (idx == -1) System.out.println("탐색 실패");
    else System.out.println("타겟 저장 인덱스: " + idx);
  }
}
