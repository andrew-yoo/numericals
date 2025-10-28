def bisection(function, alpha, beta, tolerance=10*-10, max_iterations=10_000):
    if function(alpha) == 0:
        return alpha
    if function(beta) == 0:
        return beta
    if function(alpha) * function(beta) > 0:
        raise ValueError

    for _ in range(max_iterations):
        midpoint = (alpha + beta) * 0.5
        fm = function(midpoint)
        if (abs(beta - alpha) * 0.5 < tolerance) or (fm == 0):
            return midpoint
        if fm * function(alpha) < 0:
            beta = midpoint
        else:
            alpha = midpoint

    return (alpha + beta) * 0.5