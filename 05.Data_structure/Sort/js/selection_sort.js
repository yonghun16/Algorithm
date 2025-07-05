/*-----------------------------------------------------
Sub  : 선택정렬
Memo
 - 1. 각 단계에서 가장 작은 숸소를 선택한다.
 - 2. 현재까지 처리되지 않은 원소들 중 가장 앞의 원소와 위치를 교체한다.
 - 3. 매 단계에서 가장 작은 것을 선택하는 데에 약 N번의 연산이 필요하다.
 - 4. 결과적으로 N개의 단계를 거친다는 점에서 최악의 경우 O(N^2)의 시간 복잡도를 가진다
-----------------------------------------------------*/

// 선택 정렬 함수
const selectionSort = (arr) => {
  for (let i = 0; i < arr.length - 1; i++) {
    let min = i;  // 가장 작은 원소의 인덱스
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[min]) {
        min = j;
      }
    }
    if (min !== i) {
      const temp = arr[i];
      arr[i] = arr[min];
      arr[min] = temp;
    }
  }
  return arr;
}


const arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
console.log(selectionSort(arr))
