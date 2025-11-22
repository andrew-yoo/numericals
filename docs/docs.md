---
description: |
    API documentation for modules: numericals, numericals.integrate, numericals.ode, numericals.optimize, numericals.root.

lang: en

classoption: oneside
geometry: margin=1in
papersize: a4

linkcolor: blue
links-as-notes: true
...



# Module `numericals` {#numericals}





## Sub-modules

* [numericals.integrate](#numericals.integrate)
* [numericals.ode](#numericals.ode)
* [numericals.optimize](#numericals.optimize)
* [numericals.root](#numericals.root)







# Module `numericals.integrate` {#numericals.integrate}







## Functions



### Function `gaussian` {#numericals.integrate.gaussian}




>     def gaussian(
>         function: Callable[[float], float],
>         alpha: float,
>         beta: float,
>         order: int
>     ) ‑> float


Numerically integrate a function using Gaussian Quadrature.

###### Parameters

**```function```** :&ensp;<code>Callable</code>
:   The function.


**```alpha```** :&ensp;<code>float</code>
:   The lower limit.


**```beta```** :&ensp;<code>float</code>
:   The upper limit.


**```order```** :&ensp;<code>int</code>
:   The order of the quadrature (i.e., the number of points used).

###### Returns

<code>float</code>
:   An integral approximation.




### Function `midpoint` {#numericals.integrate.midpoint}




>     def midpoint(
>         function: Callable[[float], float],
>         alpha: float,
>         beta: float,
>         n: int = 10000
>     ) ‑> float


Numerically integrate a function using the Midpoint Method.

###### Parameters

**```function```** :&ensp;<code>Callable</code>
:   The function.


**```alpha```** :&ensp;<code>float</code>
:   The lower limit.


**```beta```** :&ensp;<code>float</code>
:   The upper limit.


**```n```** :&ensp;<code>int</code>
:   The number of partitions.

###### Returns

<code>float</code>
:   An integral approximation.




### Function `monte_carlo` {#numericals.integrate.monte_carlo}




>     def monte_carlo(
>         function: Callable[[float], float],
>         alpha: float,
>         beta: float,
>         n: int = 10000
>     ) ‑> float


Numerically integrate a function using Monte Carlo Integration.

###### Parameters

**```function```** :&ensp;<code>Callable</code>
:   The function.


**```alpha```** :&ensp;<code>float</code>
:   The lower limit.


**```beta```** :&ensp;<code>float</code>
:   The upper limit.


**```n```** :&ensp;<code>int</code>
:   The number of random samples.

###### Returns

<code>float</code>
:   An integral approximation.




### Function `simpson` {#numericals.integrate.simpson}




>     def simpson(
>         function: Callable[[float], float],
>         alpha: float,
>         beta: float,
>         n: int = 10000
>     ) ‑> float


Numerically integrate a function using Simpson's Rule.

###### Parameters

**```function```** :&ensp;<code>Callable</code>
:   The function.


**```alpha```** :&ensp;<code>float</code>
:   The lower limit.


**```beta```** :&ensp;<code>float</code>
:   The upper limit.


**```n```** :&ensp;<code>int</code>
:   The number of partitions.

###### Returns

<code>float</code>
:   An integral approximation.




### Function `trapezoidal` {#numericals.integrate.trapezoidal}




>     def trapezoidal(
>         function: Callable[[float], float],
>         alpha: float,
>         beta: float,
>         n: int = 10000
>     ) ‑> float


Numerically integrate a function using the Trapezoidal Rule.

###### Parameters

**```function```** :&ensp;<code>Callable</code>
:   The function.


**```alpha```** :&ensp;<code>float</code>
:   The lower limit.


**```beta```** :&ensp;<code>float</code>
:   The upper limit.


**```n```** :&ensp;<code>int</code>
:   The number of partitions.

###### Returns

<code>float</code>
:   An integral approximation.







# Module `numericals.ode` {#numericals.ode}







## Functions



### Function `euler` {#numericals.ode.euler}




>     def euler(
>         function: Callable[[float], float],
>         alpha: float,
>         beta: float,
>         y0: float,
>         n: int
>     ) ‑> list


Solve ODE initial value problem using Euler's Method.

###### Parameters

**```function```** :&ensp;<code>Callable</code>
:   The function.


**```alpha```** :&ensp;<code>float</code>
:   The lower bound.


**```beta```** :&ensp;<code>float</code>
:   The upper bound.


**```y0```** :&ensp;<code>float</code>
:   The initial value.


**```n```** :&ensp;<code>int</code>
:   The number of partitions.

###### Returns

<code>list</code>
:   A function approximation.




### Function `heun` {#numericals.ode.heun}




>     def heun(
>         function: Callable[[float], float],
>         alpha: float,
>         beta: float,
>         y0: float,
>         n: int
>     ) ‑> list


Solve ODE initial value problem using Heun's Method.

###### Parameters

**```function```** :&ensp;<code>Callable</code>
:   The function.


**```alpha```** :&ensp;<code>float</code>
:   The lower bound.


**```beta```** :&ensp;<code>float</code>
:   The upper bound.


**```y0```** :&ensp;<code>float</code>
:   The initial value.


**```n```** :&ensp;<code>int</code>
:   The number of partitions.

###### Returns

<code>list</code>
:   A function approximation.




### Function `rk4` {#numericals.ode.rk4}




>     def rk4(
>         function: Callable[[float], float],
>         alpha: float,
>         beta: float,
>         y0: float,
>         n: int
>     ) ‑> list


Solve ODE initial value problem using Runge-Kutta 4.

###### Parameters

**```function```** :&ensp;<code>Callable</code>
:   The function.


**```alpha```** :&ensp;<code>float</code>
:   The lower bound.


**```beta```** :&ensp;<code>float</code>
:   The upper bound.


**```y0```** :&ensp;<code>float</code>
:   The initial value.


**```n```** :&ensp;<code>int</code>
:   The number of partitions.

###### Returns

<code>list</code>
:   A function approximation.







# Module `numericals.optimize` {#numericals.optimize}







## Functions



### Function `golden` {#numericals.optimize.golden}




>     def golden(
>         function: Callable[[float], float],
>         alpha: float,
>         beta: float,
>         tolerance: float = 1e-10,
>         max_iterations: int = 10000
>     ) ‑> tuple


Find local minimum using the Golden Section Search.

###### Parameters

**```function```** :&ensp;<code>Callable</code>
:   The function.


**```alpha```** :&ensp;<code>float</code>
:   The lower bound.


**```beta```** :&ensp;<code>float</code>
:   The upper bound.


**```tolerance```** :&ensp;<code>float</code>
:   The tolerance.


**```max_iterations```** :&ensp;<code>int</code>
:   The maximum number of iterations.

###### Returns

<code>tuple</code>
:   Minimizer, local minimum.







# Module `numericals.root` {#numericals.root}







## Functions



### Function `bisection` {#numericals.root.bisection}




>     def bisection(
>         function: Callable[[float], float],
>         alpha: float,
>         beta: float,
>         tolerance: float = 1e-10,
>         max_iterations: int = 10000
>     ) ‑> float


Find root using the Bisection Method.

###### Parameters

**```function```** :&ensp;<code>Callable</code>
:   The function.


**```alpha```** :&ensp;<code>float</code>
:   The lower bound.


**```beta```** :&ensp;<code>float</code>
:   The upper bound.


**```tolerance```** :&ensp;<code>float</code>
:   The tolerance.


**```max_iterations```** :&ensp;<code>int</code>
:   The maximum number of iterations.

###### Returns

<code>float</code>
:   A root approximation.




### Function `illinois` {#numericals.root.illinois}




>     def illinois(
>         function: Callable[[float], float],
>         alpha: float,
>         beta: float,
>         tolerance: float = 1e-10,
>         max_iterations: int = 10000
>     ) ‑> float


Find root using the Illinois Algorithm.

###### Parameters

**```function```** :&ensp;<code>Callable</code>
:   The function.


**```alpha```** :&ensp;<code>float</code>
:   The lower bound.


**```beta```** :&ensp;<code>float</code>
:   The upper bound.


**```tolerance```** :&ensp;<code>float</code>
:   The tolerance.


**```max_iterations```** :&ensp;<code>int</code>
:   The maximum number of iterations.




### Function `newton` {#numericals.root.newton}




>     def newton(
>         function: Callable[[float], float],
>         derivative: Callable[[float], float],
>         x0: float,
>         tolerance: float = 1e-10,
>         max_iterations: int = 10000
>     ) ‑> float


Find root using Newton's Method (also known as the Newton-Raphson Method).

###### Parameters

**```function```** :&ensp;<code>Callable</code>
:   The function.


**```derivative```** :&ensp;<code>Callable</code>
:   The function's first derivative.


**```x0```** :&ensp;<code>float</code>
:   The initial guess.


**```tolerance```** :&ensp;<code>float</code>
:   The tolerance.


**```max_iterations```** :&ensp;<code>int</code>
:   The maximum number of iterations.

###### Returns

    A root approximation.


### Function `regula_falsi` {#numericals.root.regula_falsi}




>     def regula_falsi(
>         function: Callable[[float], float],
>         alpha: float,
>         beta: float,
>         tolerance: float = 1e-10,
>         max_iterations: int = 10000
>     ) ‑> float


Find root using the Regula Falsi Method (also known as the False Position Method).

###### Parameters

**```function```** :&ensp;<code>Callable</code>
:   The function.


**```alpha```** :&ensp;<code>float</code>
:   The lower bound.


**```beta```** :&ensp;<code>float</code>
:   The upper bound.


**```tolerance```** :&ensp;<code>float</code>
:   The tolerance.


**```max_iterations```** :&ensp;<code>int</code>
:   The maximum number of iterations.




### Function `secant` {#numericals.root.secant}




>     def secant(
>         function: Callable[[float], float],
>         x0: float,
>         x1: float,
>         tolerance: float = 1e-10,
>         max_iterations: int = 10000
>     ) ‑> float


Find root using the Secant Method.

###### Parameters

**```function```** :&ensp;<code>Callable</code>
:   The function.


**```x0```** :&ensp;<code>float</code>
:   The first initial guess.


**```x1```** :&ensp;<code>float</code>
:   The second initial guess.


**```tolerance```** :&ensp;<code>float</code>
:   The tolerance.


**```max_iterations```** :&ensp;<code>int</code>
:   The maximum number of iterations.

###### Returns

<code>float</code>
:   A root approximation.