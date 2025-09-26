import math

def f(x):
    return (x**2 - 15) / (math.log(x**2) + 3*x - 7)

# кандидаты на нули — решения уравнения x^2 - 15 = 0
candidates = [math.sqrt(15), -math.sqrt(15)]

roots = []
for x in candidates:
    denom = math.log(x**2) + 3*x - 7
    if abs(denom) > 1e-9:  
        roots.append(x)
