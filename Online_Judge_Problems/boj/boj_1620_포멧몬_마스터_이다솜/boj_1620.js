/* ------------------------------------------------------------
 * Problem   : [BOJ] 나는야 포켓몬 마스터 이다솜 (1620)
 * Link      : https://www.acmicpc.net/problem/1620
 * Level     : 실버 4
 * Language  : JavaScript
 * Tags      : Map, Dictionary, String
 * Memo      : 번호 ↔ 이름 양방향 조회 구현
 * -----------------------------------------------------------*/

// [환경 설정]
const TEST_MODE = true;
let input;

// [입력 처리]
if (TEST_MODE) {
  // 로컬 테스트 (input.txt 파일 읽기)
  const filePath = require("path").join(__dirname, "input.txt");
  input = require("fs").readFileSync(filePath, "utf-8").trim().split("\n");
} else {
  // 제출 환경 (표준 입력)
  input = require("fs").readFileSync(0, "utf-8").trim().split("\n");
}

// [문제 조건 파싱]
// m: 포켓몬 수, n: 문제 수
const [m, n] = input[0].split(" ").map(Number);

// [데이터 구조]
// 번호 → 이름, 이름 → 번호 두 가지 Map을 만들어 빠른 조회 가능
const pokemonDicNumber = new Map();
const pokemonDicName = new Map();

// [사전 구성]
// 1번부터 m번까지 포켓몬 이름 입력
for (let i = 1; i <= m; i++) {
  const name = input[i].trim();
  pokemonDicNumber.set(i, name); // 번호 → 이름
  pokemonDicName.set(name, i); // 이름 → 번호
}

// [질의 처리 & 출력]
// m+1번째 줄부터 n개의 질의가 주어짐
for (let i = m + 1; i <= m + n; i++) {
  const query = input[i].trim();

  // query가 숫자면 번호로 조회
  if (pokemonDicNumber.has(Number(query))) {
    console.log(pokemonDicNumber.get(Number(query)));
  }
  // query가 문자열이면 이름으로 조회
  else {
    console.log(pokemonDicName.get(query));
  }
}
