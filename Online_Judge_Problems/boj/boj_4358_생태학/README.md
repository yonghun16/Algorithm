# 생태학

## 1. 현상(문제상황) 
### 문제
생태학에서 나무의 분포도를 측정하는 것은 중요하다. 그러므로 당신은 미국 전역의 나무들이 주어졌을 때, 각 종이 전체에서 몇 %를 차지하는지 구하는 프로그램을 만들어야 한다.

### 입력
프로그램은 여러 줄로 이루어져 있으며, 한 줄에 하나의 나무 종 이름이 주어진다. 어떤 종 이름도 30글자를 넘지 않으며, 입력에는 최대 10,000개의 종이 주어지고 최대 1,000,000그루의 나무가 주어진다.

### 출력
주어진 각 종의 이름을 사전순으로 출력하고, 그 종이 차지하는 비율을 백분율로 소수점 4째자리까지 반올림해 함께 출력한다.

## 예제
### input1
```text
Red Alder
Ash
Aspen
Basswood
Ash
Beech
Yellow Birch
Ash
Cherry
Cottonwood
Ash
Cypress
Red Elm
Gum
Hackberry
White Oak
Hickory
Pecan
Hard Maple
White Oak
Soft Maple
Red Oak
Red Oak
White Oak
Poplan
Sassafras
Sycamore
Black Walnut
Willow
```

### output1
```text
Ash 13.7931
Aspen 3.4483
Basswood 3.4483
Beech 3.4483
Black Walnut 3.4483
Cherry 3.4483
Cottonwood 3.4483
Cypress 3.4483
Gum 3.4483
Hackberry 3.4483
Hard Maple 3.4483
Hickory 3.4483
Pecan 3.4483
Poplan 3.4483
Red Alder 3.4483
Red Elm 3.4483
Red Oak 6.8966
Sassafras 3.4483
Soft Maple 3.4483
Sycamore 3.4483
White Oak 10.3448
Willow 3.4483
Yellow Birch 3.4483
```

## 2. 문제정의
- 입력에서 중복해서 들어오는 "나무 종"이 "전체 받은 나무 종" 중 얼만큼 차지하는지 구하기. 

## 3. 계획 
### Front-end
- Data를 정제하여 JSON형식으로 자료를 줘야 한다.
- input Data를 배열로 입력받는다.
- (treeMap 객체) : Map자료구조를 정의한다.
- Map에 key는 "나무 종", value는 "등장 횟수"로 저장한다.
- if (treeMap.has(tree)) {}를 사용하여 만약 이미 tree(나무 종)이 있으면, 기존의 tree key의 value에 +1을 해주고,
- 만약 없다면, 기본값으로 1을 준다.
- 완성된 map을 JSON으로 변환하기 위해 object로 변환한다.
- (total Trees 객체) :문제를 풀기 위해선 "전체 받은 나무 종"의 수도 필요하니, 이 정보도 object로 만든다.
- total Trees 객체와 treeMap 객체를 합쳐 JSON으로 만들고 전송한다.

### Back-end
- JSON형식으로 받은 Data를 object로 변환한다.
- totalTrees 변수에 "전체 나무 종"의 수를 넣는다.
- treeMapBackend 객체를 분리하고, "나무 종"을 사전 순으로 정렬하고 이름만 배열에 저장한다.
- 정렬된 배열을 순환문을 돌리고, Map.get(treeName)을 사용하여 "등장 횟수"를 출력한다.
- (등장횟수/전체 나무 종 수)*100.toFiexed(4)를 적용하여 출력형식을 구현한다.
- result 배열에 차곡차곡 적재한 뒤 배열을 출력한다. -> console.log(result.join('\n'));

## 4. 수행
### (FE)Map 자료형에 데이터 적재
```js
for (const tree of trees) {
  if (treeMap.has(tree)) {
    treeMap.set(tree, treeMap.get(tree) + 1);  // 이미 키가 존재하면, 기존 값에 1을 더해 다시 저장
  } else {
    treeMap.set(tree, 1);   // 키가 존재하지 않으면, 1로 새로 추가
  }
}
```
### (FE)데이터 JSON 변환
```js
// Map -> Object
const treeObject = Object.fromEntries(treeMap);

// 전송할 데이터 셋팅
const data = [
  { "Total Trees": totalTrees },
  treeObject
]
```

### (BE) 데이터 추출
```js
// JSON -> Array[Object]
const receivedData = JSON.parse(dataJSON);
// console.log("전송받은 데이터", receivedData);

const totalTreesBackend = receivedData[0]["Total Trees"];
const treeMapBackend = new Map(Object.entries(receivedData[1]));
```

### (BE)데이터 문제의 형태로 출력
```js
// 나무 이름만 정렬
const sortedTreeNames = Array.from(treeMapBackend.keys()).sort();

const result = [];
for (const name of sortedTreeNames) {
  const count = treeMapBackend.get(name);
  const percentage = ((count / totalTreesBackend) * 100).toFixed(4);

  result.push(`${name} ${percentage}`);
}

console.log(result.join('\n'));
```

## 5. 평가(나아진 점, 개선해야할 점 등... )
- 구현 완료
