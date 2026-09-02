class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []
        for i in tokens:
            if i not in ["+", "*", "-", "/"]:
                my_stack.append(i)
            elif i == "+":
                num1 = my_stack.pop()
                num2 = my_stack.pop()
                my_stack.append(int(num2) + int(num1))
            elif i == "-":
                num1 = my_stack.pop()
                num2 = my_stack.pop()
                my_stack.append(int(num2) - int(num1))
            elif i == "*":
                num1 = my_stack.pop()
                num2 = my_stack.pop()
                my_stack.append(int(num2) * int(num1))
            elif i == "/":
                num1 = my_stack.pop()
                num2 = my_stack.pop()
                my_stack.append(int(num2) / int(num1))

        return int(my_stack[0])