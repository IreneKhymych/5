import math

def basic_operations(a, b, op):
    a, b = float(a), float(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b if b != 0 else "Ділення на нуль!"
    else:
        return "Невідома операція"

def solve_equation(eq_type, coeffs):
    eq_type = eq_type.lower()

    if eq_type == "лінійне":
        if len(coeffs) != 2:
            raise ValueError("Для лінійного рівняння потрібно 2 коефіцієнти")
        a, b = coeffs
        if a == 0:
            return "Немає розв'язку" if b != 0 else "Безліч розв'язків"
        return f"x = {-b / a}"

    elif eq_type == "quadratic":
        if len(coeffs) != 3:
            raise ValueError("Для квадратного рівняння потрібно 3 коефіцієнти")
        a, b, c = coeffs
        D = b**2 - 4*a*c
        if D < 0:
            return "Немає дійсних коренів"
        elif D == 0:
            x = -b / (2*a)
            return f"x = {x}"
        else:
            x1 = (-b + math.sqrt(D)) / (2*a)
            x2 = (-b - math.sqrt(D)) / (2*a)
            return f"x₁ = {x1}, x₂ = {x2}"

    else:
        raise ValueError(f"Невідомий тип рівняння: {eq_type}")