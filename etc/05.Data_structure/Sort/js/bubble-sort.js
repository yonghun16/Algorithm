/*-----------------------------------------------------
Sub  : 버블정렬
Tag  : JS, 
Memo
  - 단순히 인접한 두 원소를 확인하여, 정렬이 안 되어 있다면 위치를 서로 변경한다. 
-----------------------------------------------------*/

// 버블정렬 함수
function bubbleSort(arr) {
  const n = arr.length;
  for (let i = 0; i < n - 1; i++) {
    let swapped = false;
    for (let j = 0; j < n - 1 - i; j++) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        swapped = true;
      }
    }
    if (!swapped) break; // 이미 정렬된 경우
  }
  return arr;
}

console.log(bubbleSort([5, 1, 4, 2, 8])); // [1, 2, 4, 5, 8]
