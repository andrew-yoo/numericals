import pytest
from numericals import ode

import math

f1 = lambda x, y: y
f1_solution = lambda x: math.e**x

f2 = lambda x, y: (6 * x) - (3 * y) + 5
f2_solution = lambda x: 2 * math.e ** (-3 * x) + 2 * x + 1


def test_euler():
    f1_euler = ode.euler(f1, 0, 1, 1, 10_000)
    f1_actual = [f1_solution(i / 10_000) for i in range(10_000)]

    assert f1_euler[1] == pytest.approx(f1_actual, abs=1e-3)

    f2_euler = ode.euler(f2, 0, 5, 3, 10_000)
    f2_actual = [f2_solution(i / 2_000) for i in range(10_000)]

    assert f2_euler[1] == pytest.approx(f2_actual, abs=1e-3)


def test_heun():
    f1_heun = ode.heun(f1, 0, 1, 1, 10_000)
    f1_actual = [f1_solution(i / 10_000) for i in range(10_000)]

    assert f1_heun[1] == pytest.approx(f1_actual, abs=1e-3)

    f2_heun = ode.heun(f2, 0, 5, 3, 10_000)
    f2_actual = [f2_solution(i / 2_000) for i in range(10_000)]

    assert f2_heun[1] == pytest.approx(f2_actual, abs=1e-3)


def test_rk4():
    f1_rk4 = ode.rk4(f1, 0, 1, 1, 10_000)
    f1_actual = [f1_solution(i / 10_000) for i in range(10_000)]

    assert f1_rk4[1] == pytest.approx(f1_actual, abs=1e-3)

    f2_rk4 = ode.rk4(f2, 0, 5, 3, 10_000)
    f2_actual = [f2_solution(i / 2_000) for i in range(10_000)]

    assert f2_rk4[1] == pytest.approx(f2_actual, abs=1e-3)
