// 병합 정렬

const mergeSort = (arr) => {
  // 배열이 1개 이하이면 이미 정렬된 상태
  if (arr.length <= 1) return arr;

  const mid = Math.floor(arr.length / 2);
  const left = arr.slice(0, mid);
  const right = arr.slice(mid);

  // 재귀적으로 정렬한 후 병합
  return merge(mergeSort(left), mergeSort(right));
}

const merge = (left, right) => {
  const result = [];

  let i = 0;
  let j = 0;

  // 두 배열을 오름차순으로 병합
  while (i < left.length && j < right.length) {
    if (left[i] < right[j]) {
      result.push(left[i++]);
    } else {
      result.push(right[j++]);
    }
  }

  // 남은 요소 추가
  return [...result, ...left.slice(i), ...right.slice(j)];
}

// 테스트: 길이 10의 배열
const numbers = [23, 5, 89, 12, 45, 7, 3, 38, 19, 56];

const sorted = mergeSort(numbers);

console.log(sorted);
