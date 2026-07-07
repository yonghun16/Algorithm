// 이 파일이 프로젝트의 입구입니다. 모든 공개할 기능들을 여기서 다시 내보냅니다.
// types와 core에 흩어진 기능들을 모아서 한꺼번에 export

export * from "./types/stack.types"; // 명세(Interface)를 밖으로 내보냄
export { createStack } from "./core/array-stack"; // 생성 함수를 밖으로 내보냄
