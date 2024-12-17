import sys

def process_expression(expression):
    stack = []

    for i in range(len(expression)):
        if expression[i] == ')':
            nums = []
            while stack[-1] != '(':
                n = stack.pop()
                try:
                    nums.append(int(n))
                except ValueError:
                    op = n
                    if op == '+':
                        summ = sum(nums)
                        nums = []
                        nums.append(summ)
                    elif op == '-':
                        difference = nums.pop()
                        while nums:
                            difference -= nums.pop()
                        nums.append(difference)
                    elif op == '*':
                        product = nums.pop()
                        while nums:
                            product *= nums.pop()
                        nums.append(product)
                    elif op == '/':
                        quotient = nums.pop()
                        while nums:
                            quotient /= nums.pop()
                        nums.append(quotient)
            stack.pop()
            if nums:
                stack.append(nums[0])
        else:
            stack.append(expression[i])

    return int(stack[0])


def main(stream=sys.stdin):
    for line in stream:
        expression = ''.join(line.strip().split())
        print(process_expression(expression))

if __name__ == "__main__":
    main()
