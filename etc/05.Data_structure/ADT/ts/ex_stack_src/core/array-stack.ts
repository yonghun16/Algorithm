// 실제 로직을 구현합니다.
// 외부에서 직접 클래스를 인스턴스화하지 못하도록 팩토리 함수를 제공하는 것이 포인트입니다.

import { IStack } from "../types/stack.types";

// implements IStack: "나는 IStack의 규칙을 완벽히 지키겠다"는 선언
class ArrayStack<T> implements IStack<T> {
  // #items: 클래스 내부에서만 쓰는 진짜 저장소.
  // '#'은 외부에서 절대로 이 변수를 직접 건드리지 못하게 막는 방어막입니다.
  #items: T[] = [];

  push(item: T): void {
    this.#items.push(item);
  }
  pop(): T | undefined {
    return this.#items.pop();
  }
  peek(): T | undefined {
    return this.#items[this.#items.length - 1];
  }
  // get size(): 외부에서 stack.size라고 부르면 실행되는 함수입니다.
  // 실제로는 함수지만 사용자에게는 변수(프로퍼티)처럼 보입니다.
  get size(): number {
    return this.#items.length;
  }
}

// 오직 팩토리 함수만 내보내서 구현체(ArrayStack)를 은닉합니다.
export const createStack = <T>(): IStack<T> => new ArrayStack<T>();
