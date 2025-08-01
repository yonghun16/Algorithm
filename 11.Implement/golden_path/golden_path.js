/*-----------------------------------------------------
 Sub   : Golden Path
 Memo  : Map을 활용한 구현
-----------------------------------------------------*/

const TEST_MODE = true;

let input;

if (TEST_MODE) {
  const filePath = require('path').join(__dirname, 'input1.txt');
  input = require('fs').readFileSync(filePath, 'utf-8').trim().split('\n');
} else {
  input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
}



/*----------------------------------
        menu-data (FE, BE 공용)
-----------------------------------*/

const menuData = {
  'menu-new': [
    'mint-choco-latte',
    'pumpkin-spice-latte',
    'black-sesame-latte',
    'salted-caramel-mocha',
  ],
  'menu-coffee': [
    'cafe-latte',
    'ice-americano',
    'vanilla-latte',
    'espresso',
    'caramel-macchiato',
    'cold-brew',
  ],
  'menu-ade': [
    'strawberry-ade',
    'lemon-ade',
    'grapefruit-ade',
    'blueberry-ade',
    'green-grape-ade',
  ],
  'menu-dessert': [
    'cheesecake',
    'chocolate-brownie',
    'tiramisu',
    'macaron',
    'blueberry-muffin',
    'butter-croissant',
  ],
  'menu-tea': [
    'earl-grey-tea',
    'chamomile-tea',
    'green-tea',
    'hibiscus-tea',
    'yuzu-tea',
  ],
};



/*----------------------------------
     front-end Data handling
-----------------------------------*/

const N = parseInt(input[0]);
const rawPaths = input.slice(1);   // 전체 경로들 받기
// const rawPaths = [];
// for (let i = 1; i <= N; i++) {
//   rawPaths.push(input[i]);
// }

const pathHistoryMap = new Map();  // 구매 건별 경로를 저장하는 Map
const allMenuItems = new Set(Object.values(menuData).flat());   // 모든 메뉴 아이템을 빠르게 조회할 수 있도록 Set으로 만듬.

// 현재 단계(step)가 메뉴 아이템이 맞는지 확인하는 함수
function isMenuItem(step) {
  return allMenuItems.has(step);
}

// 선택된 경로(path)에 정제 규칙을 적용하는 함수
function refinePath(path) {
  const result = [];
  for (let i = 0; i < path.length; i++) {
    const currentStep = path[i];
    const prevStep = i > 0 ? path[i - 1] : null;

    // '(페이지 A) -> (상품 B)' 패턴인데 뒤에 'cart'가 없는 경우를 확인
    if (prevStep && isMenuItem(currentStep) && path[i + 1] !== 'cart') {
      result.pop(); // 바로 이전 단계(페이지 A)를 결과에서 제거
      continue;     // 현재 단계(상품 B)는 아예 추가하지 않고 건너뜀
    }
    result.push(currentStep);
  }
  return result;
}

// processing
for (const pathString of rawPaths) {
  const pathArray = pathString.split(' ');

  // payment가 없는 경로는 무시
  if (pathArray[pathArray.length - 1] !== 'payment') {
    continue;
  }

  // 각 구매 건(상품 + cart)을 식별하고 처리
  pathArray.forEach((step, index) => {
    // 현재 단계가 'cart'이고, 바로 앞에 상품이 있는 경우
    if (step === 'cart' && index > 0 && isMenuItem(pathArray[index - 1])) {
      const purchasedItem = pathArray[index - 1];

      // 1. 구매 건별 '정제 전 경로' 생성
      // 현재 cart까지의 원본 경로에 payment를 붙입니다.
      const preRefinementPath = pathArray.slice(0, index + 1);
      preRefinementPath.push('payment');

      // 2. 경로 정제
      // 새로 정의된 규칙에 따라 경로를 정제합니다.
      const refinedPath = refinePath(preRefinementPath);

      // 3. pathHistoryMap에 경로 추가
      if (!pathHistoryMap.has(purchasedItem)) {
        pathHistoryMap.set(purchasedItem, []);
      }
      pathHistoryMap.get(purchasedItem).push(refinedPath);
    }
  });
}

// console.log("완성된 pathHistoryMap", pathHistoryMap);

// Map -> Object
const pathHistoryObject = Object.fromEntries(pathHistoryMap);

// 전송할 데이터 셋팅
const data = [
  { "Total Paths": N },
  pathHistoryObject
]

// Array[Object] -> JSON
const dataJSON = JSON.stringify(data, null, 2);
// console.log("전송할 데이터", dataJSON);



/*----------------------------------
     back-end Data handling
-----------------------------------*/

/* 대충 몽고DB에 적재되는 JSON문서형태
{
  "menuItem": "cafe-latte",
  "pathHistory": [
    {
      "path": ["start", "menu-coffee", "cafe-latte", "cart", "payment"],
      "createdAt": ISODate("2023-05-12T14:00:00.000Z")
    },
    {
      "path": ["start", "menu-recommend", "cafe-latte", "cart", "payment"],
      "createdAt": ISODate("2023-05-13T09:30:00.000Z")
    }
    ...
    ...
  ]
  ...
}
...
...
*/



/*----------------------------------
     front-end Data handling
-----------------------------------*/

// 백엔드에게 요청 데이타를 받고 pathHistoryMap을 변환했다 치고 사용

const sortedMenuItems = [...pathHistoryMap.keys()].sort();  // 메뉴 이름을 알파벳 순으로 정렬
const answer = [];     // 출력 배열

// 정렬된 각 메뉴 순환
for (const menuItem of sortedMenuItems) {
  answer.push(menuItem);     // 메뉴 이름 answer에 삽입

  const paths = pathHistoryMap.get(menuItem); // 해당 메뉴의 모든 경로 배열을 가져옴
  const pathCounts = new Map();

  // 각 경로의 등장 횟수를 계산합니다.
  for (const pathArray of paths) {
    const pathString = pathArray.join(' -> ');
    pathCounts.set(pathString, (pathCounts.get(pathString) || 0) + 1);  // pathCounts.get(pathString)이 없는 경우에는 falsy 가 되어 0으로 적용함.
  }

  // 경로들을 문제의 요구사항(내림차순)에 맞게 정렬합니다.
  const sortedPaths = [...pathCounts].sort((a, b) => {
    const countA = a[1];
    const countB = b[1];

    if (countA !== countB) {
      return countB - countA; // 횟수 내림차순
    } else {
      return a[0].localeCompare(b[0]); // 횟수가 같으면 경로 문자열 오름차순
    }
  });

  // 정렬된 결과를 answer에 삽입.
  for (const [pathString, count] of sortedPaths) {
    answer.push(`${pathString} ${count}`);
  }
}


// 정답 출력
console.log(answer.join('\n'));
