function getMax(arr) {
  return Math.max(...arr);
}

function countingSortByDigit(arr, digit) {
  const output = new Array(arr.length).fill(0);
  const count = new Array(10).fill(0);

  for (let i = 0; i < arr.length; i++) {
    const d = Math.floor(arr[i] / digit) % 10;
    count[d]++;
  }

  for (let i = 1; i < 10; i++) count[i] += count[i - 1];

  for (let i = arr.length - 1; i >= 0; i--) {
    const d = Math.floor(arr[i] / digit) % 10;
    output[count[d] - 1] = arr[i];
    count[d]--;
  }

  for (let i = 0; i < arr.length; i++) arr[i] = output[i];
}

function radixSort(arr) {
  const max = getMax(arr);
  for (let digit = 1; Math.floor(max / digit) > 0; digit *= 10)
    countingSortByDigit(arr, digit);
  return arr;
}

console.log(radixSort([170, 45, 75, 90, 802, 24, 2, 66]));
