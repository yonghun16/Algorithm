/*-----------------------------------------------------
Sub  : 버블정렬
Tag  : JS, 
Memo
  - 단순히 인접한 두 원소를 확인하여, 정렬이 안 되어 있다면 위치를 서로 변경한다. 
-----------------------------------------------------*/

// 버블정렬 함수
const bubbleSort = (arr) => {
  for (let i = 0; i < arr.length - 1; i++) {
    for (let j = 0; j < arr.length - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        const temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  return arr;
}

// 테스트
const arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
console.log(bubbleSort(arr))
