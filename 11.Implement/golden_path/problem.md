# 골든 패스 알고리즘 (Golden Path Algorithm)
인영은 자신이 만든 '음료 주문 앱'의 사용자 경험을 개선하고자 합니다. 이를 위해 사용자들이 앱에 접속해서 음료를 구매하기까지의 페이지 이동 경로 데이터를 분석하여, 각 음료별로 가장 인기 있는 구매 경로인 골든 패스(Golden Path) 를 찾아내려고 합니다.

__골든 패스(Golden Path)__ 란, 구매에 성공한 경로들을 '경로 정제 규칙'에 따라 정제했을 때, 음료별로 가장 많이 등장하는 경로를 의미합니다.



## 📜 규칙

#### 1. 분석 대상 경로 (구매 성공 경로)
분석 대상은 경로의 가장 마지막이 <code>payment</code>로 끝나는 '구매 성공' 로그에 한정됩니다. <code>payment</code>로 끝나지 않은 로그는 분석에서 완전히 무시합니다.

#### 2. 구매 음료 식별 및 경로 분리
하나의 '구매 성공' 로그는 여러 개의 구매 건을 포함할 수 있습니다. 구매 건은 다음 규칙에 따라 식별하고 분리합니다.

- <code>cart</code>는 바로 직전에 나온 하나의 상품을 장바구니에 담는 행위입니다.
- 로그에 <code>cart</code>가 여러 번 등장하면, 여러 개의 상품이 구매된 것으로 간주합니다.
- 각 구매 건에 대한 __'정제 전 경로'__ 는, 해당 상품이 <code>cart</code>에 담긴 시점까지의 원본 로그 전체에 payment를 덧붙여 생성합니다.
- 상품 식별: start, cart, payment나 menu-로 시작하는 페이지가 아닌, 고유한 상품명(예: cafe-latte)을 가집니다. 상품 목록은 아래 <code>menuData</code> 객체로 주어집니다.
  ```text
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
  ```

#### 3. 경로 정제 규칙
'정제 전 경로'에서 불필요한 탐색 과정을 제거하여 최종 경로를 만듭니다.

- 정제란, 경로 내에서 __'특정 상품 페이지에 방문했지만 <code>cart</code>에 담지 않고 다른 행동으로 넘어간 기록'__을 제거하는 과정입니다.
- 규칙: 경로에서 <code>(페이지 A) -> (상품 B)</code> 패턴을 발견했을 때, 그 바로 뒤에 <code>cart</code>가 오지 않는다면, <code>(페이지 A) -> (상품 B)</code> 부분을 경로에서 제거합니다.
  - 여기서 <code>상품 B</code>는 <code>menuData</code>에 존재하는 음료/디저트입니다.
  - <code>페이지 A</code>는 <code>search</code>와 같이 상품이 아닌 모든 페이지를 의미할 수 있습니다.


## ⚙️ 처리 과정 예시

아래와 같은 하나의 복잡한 경로 데이터가 주어졌을 때의 처리 과정을 살펴봅시다.

#### 원본 경로
> <code>start -> menu-coffee -> ice-americano -> menu-coffee -> cafe-latte -> cart -> menu-ade -> strawberry-ade -> cart -> payment</code>

#### 1단계: 구매 성공 및 구매 상품 식별
경로가 <code>payment</code>로 끝나므로 '구매 성공'입니다. 경로 내에 <code>cart</code>가 3번 등장하며, 각 <code>cart</code> 직전의 상품인 <code>cafe-latte와 strawberry-ade</code>가 최종 구매 상품입니다.

#### 2단계: 구매 건별 '정제 전 경로' 분리
각 상품이 <code>cart</code>에 담긴 시점까지의 원본 로그를 잘라내어 2개의 '정제 전 경로'를 생성합니다.

- <code>cafe-latte</code>의 정제 전 경로: (첫 번째 cart까지의 경로 + payment)
  - <code>start -> menu-coffee -> ice-americano -> menu-coffee -> cafe-latte -> cart -> payment</code>

- <code>strawberry-ade</code>의 정제 전 경로: (두 번째 cart까지의 경로 + payment)
  - <code>start -> menu-coffee -> ice-americano -> menu-coffee -> cafe-latte -> cart -> menu-ade -> strawberry-ade -> cart -> payment</code>

#### 3단계: 각 경로 정제
'경로 정제 규칙'에 따라 각 경로에서 불필요한 탐색 부분을 제거합니다.

- <code>cafe-latte</code> 경로 정제:
  - 정제 전 경로: <code>start -> menu-coffee -> ice-americano -> menu-coffee -> cafe-latte -> cart -> payment</code>
  - <code>... -> menu-coffee -> ice-americano</code> 다음에 cart가 오지 않았으므로 이 부분을 제거합니다.
  - 정제 후 경로: <code>start -> menu-coffee -> cafe-latte -> cart -> payment</code>

- <code>strawberry-ade</code> 경로 정제:
  - 정제 전 경로: <code>start -> menu-coffee -> ice-americano -> menu-coffee -> cafe-latte -> cart -> menu-ade -> strawberry-ade -> cart -> payment</code>
  - 마찬가지로 <code>... -> menu-coffee -> ice-americano</code> 다음에 cart가 오지 않았으므로 제거합니다. (cafe-latte와 strawberry-ade는 각각 cart로 이어지므로 유지됩니다.)
  - 정제 후 경로: <code>start -> menu-coffee -> cafe-latte -> cart -> menu-ade -> strawberry-ade -> cart -> payment</code>

#### 4단계: 집계
위와 같이 처리하여 얻어진 2개의 최종 정제 경로를 각각 cafe-latte와 strawberry-ade의 구매 경로로 카운트합니다.


## 🖥️ 입력과 출력

#### 입력
- 첫 번째 줄에는 경로 데이터의 총개수를 나타내는 정수 N이 주어집니다. (1 <= N <= 1,000)
- 두 번째 줄부터 N개의 줄에 걸쳐 사용자의 행동 경로가 공백으로 구분되어 주어집니다. 각 경로의 길이는 최대 100입니다.

#### 출력
- 분석이 완료된 음료의 이름을 알파벳순으로 먼저 출력합니다.
- 다음 줄부터 해당 음료의 정제된 경로와 등장 횟수를 한 줄에 하나씩 출력합니다.
- 경로들은 __등장 횟수가 많은 순(내림차순)__ 으로 정렬하며, 횟수가 같을 경우 __경로 문자열을 알파벳순(오름차순)__ 으로 정렬합니다.

## 😀 입력과 출력 예시
### 예제 1️⃣
#### 입력
```text
5
start menu-coffee cafe-latte cart payment
start menu-dessert cheesecake menu-coffee cafe-latte cart payment
start search cafe-latte cart payment
start menu-ade lemon-ade cart
start menu-coffee ice-americano cart payment
```
#### 출력
```text
cafe-latte
start -> menu-coffee -> cafe-latte -> cart -> payment 2
start -> search -> cafe-latte -> cart -> payment 1
ice-americano
start -> menu-coffee -> ice-americano -> cart -> payment 1
```

### 예제 2️⃣
#### 입력
```text
25
start menu-coffee cafe-latte cart payment
start menu-coffee ice-americano cart payment
start menu-ade strawberry-ade cart
start menu-new mint-choco-latte cart payment
start menu-coffee cafe-latte menu-coffee cafe-latte cart payment
start menu-coffee ice-americano menu-coffee ice-americano cart payment
start menu-recommend cafe-latte cart payment
start menu-coffee cafe-latte cart menu-coffee cafe-latte cart payment
start menu-ade strawberry-ade cart payment
start search ice-americano
start menu-new mint-choco-latte start menu-new mint-choco-latte cart payment
start menu-coffee cafe-latte cart payment
start menu-coffee cafe-latte cart menu-ade strawberry-ade cart payment
start menu-coffee ice-americano cart
start menu-recommend cafe-latte
start menu-ade strawberry-ade cart menu-ade cart payment
start menu-new mint-choco-latte cart payment
start menu-coffee ice-americano cart payment
start search mint-choco-latte cart payment
start menu-coffee ice-americano cart payment
start menu-coffee cafe-latte cart payment
start menu-ade strawberry-ade cart payment
start menu-coffee ice-americano cart menu-new mint-choco-latte cart payment
start menu-recommend cafe-latte cart payment
start menu-new mint-choco-latte cart
```

#### 출력
```text
cafe-latte
start -> menu-coffee -> cafe-latte -> cart -> payment 6
start -> menu-recommend -> cafe-latte -> cart -> payment 2
start -> menu-coffee -> cafe-latte -> cart -> menu-coffee -> cafe-latte -> cart -> payment 1
ice-americano
start -> menu-coffee -> ice-americano -> cart -> payment 5
mint-choco-latte
start -> menu-new -> mint-choco-latte -> cart -> payment 2
start -> menu-coffee -> ice-americano -> cart -> menu-new -> mint-choco-latte -> cart -> payment 1
start -> search -> mint-choco-latte -> cart -> payment 1
start -> start -> menu-new -> mint-choco-latte -> cart -> payment 1
strawberry-ade
start -> menu-ade -> strawberry-ade -> cart -> payment 3
start -> menu-coffee -> cafe-latte -> cart -> menu-ade -> strawberry-ade -> cart -> payment 1
```
