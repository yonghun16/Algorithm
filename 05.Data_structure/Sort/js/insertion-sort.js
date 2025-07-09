// 삽입 정렬


// 미는 방식 
function insertionSort(arr) {
  const n = arr.length;
  for (let i = 1; i < n; i++) {
    let key = arr[i];
    let j = i - 1;
    while (j >= 0 && arr[j] > key) {
      arr[j + 1] = arr[j];  // 한 칸 밀기
      j--;
    }
    arr[j + 1] = key;  // 삽입 위치 : key보다 작은 값을 처음 만난 지점 다음
  }
  return arr;
}

// // 교환하는 방식
// const insertionSort = (arr) => {
//   for (let i = 1; i < arr.length; i++) {
//     for (let j = i; j > 0; j--) {
//       if (arr[j] < arr[j - 1]) {
//         const temp = arr[j];
//         arr[j] = arr[j - 1];
//         arr[j - 1] = temp;
//       } else {
//         break;
//       }
//     }
//   }
//   return arr;
// };

const arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9];
console.log(insertionSort(arr));
