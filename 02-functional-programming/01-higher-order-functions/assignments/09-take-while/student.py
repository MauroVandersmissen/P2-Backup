def take_while(xs,condition):
    lst1=[]
    lst2=[]
    triggered=False
    for i in range(len(xs)):
        if condition(xs[i]) and not triggered:
            lst1.append(xs[i])
        else:
            lst2.append(xs[i])
            triggered=True
    return (lst1,lst2)

def is_negative(x):
    return x<0

print(take_while([-4, -2, 0, -1, 4, 6],is_negative))