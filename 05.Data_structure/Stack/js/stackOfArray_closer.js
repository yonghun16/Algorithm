// 함수 기반으로 캡슐화(클로저 활용)

// 클로저 = 클로저는 함수 선언 시점의 환경을 기억하는 것
//          ( 함수 + 함수가 선언될 당시의 스코프(scope)를 기억하는 기능 )

// •	stack.items처럼 외부에서 접근 시도하면 undefined
// •	하지만 push, pop, peek 등 메서드를 통해서만 items에 접근 가능

// 특징             클래스(Class)             클로저(Closure)
// -------------------------------------------------------------------------------------
// 상태 저장        객체 프로퍼티             함수 내부 변수
// 외부 접근 제어   private / convention      함수 스코프(외부 접근 불가)
// 메서드           클래스 내부 메서드        함수가 반환하는 객체 메서드
// 상속/다형성      가능                      직접적으로 불가능
// 장점             구조적, 상속 가능         간단, 외부에서 안전하게 상태 보호 가능
// 단점             문법이 비교적 복잡        상속/다형성 구현 어려움

const createStack = () => {
  const items = [];

  return {
    push(element) {
      items.push(element);
    },
    pop() {
      return items.length === 0 ? null : items.pop();
    },
    peek() {
      return items.length === 0 ? null : items[items.length - 1];
    },
    isEmpty() {
      return items.length === 0;
    },
    size() {
      return items.length;
    },
    clear() {
      items.length = 0; // items=[] 으로 하면 클로저 안에서 참조하던 기존 배열과 연결이 끊김
    },
    print() {
      console.log(items.join(' <- '));
    }
  };
};

// 사용 예시
const stack = createStack();

stack.push(10);
stack.push(20);
stack.push(30);

stack.print();        // 10 <- 20 <- 30

console.log(stack.pop());   // 30
console.log(stack.peek());  // 20
console.log(stack.size());  // 2
console.log(stack.isEmpty()); // false

stack.clear();
console.log(stack.isEmpty()); // true
