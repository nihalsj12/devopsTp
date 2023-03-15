def add(x, y):
    """Additionne deux nombres."""
    return x + y

def subtract(x, y):
    """Soustrait deux nombres."""
    return x - y

def multiply(x, y):
    """Multiplie deux nombres."""
    return x * y

def divide(x, y):
    """Divise deux nombres."""
    if y == 0:
        raise ValueError("La division par zéro n'est pas autorisée.")
    return x / y