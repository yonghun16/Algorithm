// 삽입 정렬

const insertionSort = (arr) => {
  for (let i = 1; i < arr.length; i++) {
    for (let j = i; j > 0; j--) {
      if (arr[j] < arr[j - 1]) {
        const temp = arr[j];
        arr[j] = arr[j - 1];
        arr[j - 1] = temp;
      } else {
        break;
      }
    }
  }
  return arr;
};

const arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9];
console.log(insertionSort(arr));
