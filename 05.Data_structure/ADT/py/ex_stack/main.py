from stack import create_stack

# 사용자는 추상화된 인터페이스(Stack)만 보고 코딩함
my_stack = create_stack()
my_stack.push("Apple")
print(my_stack.pop())
