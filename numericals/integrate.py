import random


def trapezoidal(function, alpha, beta, n=10_000):
    delta = (beta - alpha) / n
    sum = 0.5 * (function(alpha) + function(beta))
    for i in range(1, n):
        sum += function(alpha + i * delta)
    return delta * sum


def midpoint(function, alpha, beta, n=10_000):
    delta = (beta - alpha) / n
    sum = 0
    for i in range(n):
        sum += function(alpha + (i + 0.5) * delta)
    return delta * sum


def simpson(function, alpha, beta, n=10_000):
    h = (beta - alpha) / n
    sum = function(alpha) + function(beta)

    for i in range(1, n, 2):
        sum += 4 * function(alpha + i * h)

    for i in range(2, n - 1, 2):
        sum += 2 * function(alpha + i * h)

    return sum * (h / 3)


def monte_carlo(function, alpha, beta, n=10_000):
    width = beta - alpha
    total = 0
    for _ in range(n):
        r = random.random()
        x = alpha + r * width
        total += function(x)
    average = total / n
    return average * width
