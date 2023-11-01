def eval(exp):
    stack=[]
    for i in exp:
        if i in ["+"]:
            operand2= stack.pop()
            operand1= stack.pop()
            stack.append(operand1+operand2)
        else:
            stack.append(int(i))
    return stack.pop()
            