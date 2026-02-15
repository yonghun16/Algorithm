// 스택이 가져야 할 규격을 정의합니다.

export interface IStack<T> {
  push(item: T): void; // T 타입 데이터를 받고, 반환값은 없음(void)
  pop(): T | undefined; // 데이터를 꺼내는데, 비어있을 수도 있으니 undefined 허용
  peek(): T | undefined; // 맨 위를 구경만 함
  readonly size: number; // 크기는 읽기만 가능하고 수정은 불가(readonly)
}
