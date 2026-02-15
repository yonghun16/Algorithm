// 사용자는 이제 types/나 core/ 폴더 깊숙이 들어갈 필요 없이 **index.ts**만 바라봅니다.
// 깔끔하게 한 곳에서 모두 import 가능

import { IStack, createStack } from "./index";

const stack: IStack<string> = createStack<string>();

stack.push("TypeScript");
stack.push("Barrel Pattern");

console.log(`현재 크기: ${stack.size}`); // 2
console.log(`꺼낸 아이템: ${stack.pop()}`); // Barrel Pattern
