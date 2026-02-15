from abc import ABC, abstractmethod


# [명세] C의 헤더 파일 역할
class Stack(ABC):
    @abstractmethod
    def push(self, item):
        pass

    @abstractmethod
    def pop(self):
        pass


# [구현] C의 소스 파일 역할 (Internal 클래스)
class _ArrayStack(Stack):
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop() if self._items else None


# [팩토리 함수] 외부에서 객체를 생성하는 유일한 통로
def create_stack() -> Stack:
    return _ArrayStack()
