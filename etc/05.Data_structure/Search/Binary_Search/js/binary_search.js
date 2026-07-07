const bSearch = (arr, target) => {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);

    if (arr[mid] === target) {
      return mid;
    } else {
      if (target < arr[mid]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }
  }

  return -1;
};

arr1 = [1, 3, 5, 7, 9];

idx = bSearch(arr1, 7);
if (idx === -1) {
  console.log("찾는 값이 없습니다.");
} else {
  console.log(idx);
}

idx = bSearch(arr1, 4);
if (idx === -1) {
  console.log("찾는 값이 없습니다.");
} else {
  console.log(idx);
}
