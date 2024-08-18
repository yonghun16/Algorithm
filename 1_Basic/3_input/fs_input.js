/* fs를 이용해 파일 전체를 읽어 들여 처리하기 */

const fs = require('fs')
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n')
const inputVal = inputData[0].split(' ').map(Number)

main(inputVal)


function main(inputVal) {
  console.log(inputVal)
}
