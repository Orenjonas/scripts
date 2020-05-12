from sympy import symbols
from sympy.plotting import plot
import sympy as sp
import numpy as np

sp.init_printing(use_latex=True)
x = symbols('x')
# print(sp.expand(((2*x+1)*(2*x-1)**2)))

sympy.integrate

# from sympy.polys.specialpolys import interpolating_poly
# from sympy.polys.polyfuncs import interpolate

# def f(x, k):
#     return sp.pi/2 + sum([(-4)/((2*n-1)**2*np.pi) * sp.cos((2*n-1)*x) for n in range(1, k+1)])

sp.plot(sp.log(x**2))

# def gauss(x, sigma, pi, mu):
#     return 1/(sigma*sp.sqrt(2*pi)) * sp.exp(-0.5*(((x-mu)/sigma))**2)

# pi=2
# mu=1
# sigma=0.2

# sp.plot(gauss(x, sigma, pi, mu), sp.log(gauss(x, sigma, pi, mu)), ylim= (-2.5, 5))


# # n = 3
# # xvals = np.linspace(-1, 1, n)
# # points = [(x, f(x)) for x in xvals]


# # k = 0
# # p = plot(sp.Abs(x), (x, -1,1), ylim=[-1,1], show=False, line_color=(k, 0, 0))
# # for k in range(1, 10):
# #     p2 = plot(f(x,k), (x, -1,1), ylim=[-1,1], show=False, line_color=(1/k, 0, 0))
# #     p.append(p2[0])
# # #     # xvals = np.linspace(-1, 1, n)
# #     # points = [(x, f(x)) for x in xvals]
# #     # plot(interpolate(points, x), (x, -1,1))#, show=False)
# #     # p.append(p0[0])
# # p.show()

# # print(sp.diff("x**3"))

# ## PLOT MULTIPLE FUNCTIONS
# # p1 = plot(abs(x), x*x, 7/3*x*x - 3/4*x**4, (x, -1.0, 1.0))


## 3D PLOTTING
# # from sympy.plotting import plot3d
x, y = symbols('x y')
# plot3d(x*y, (x, -5, 5), (y, -5, 5))

# # # IMPLICIT
# # from sympy import plot_implicit, cos, sin, symbols, Eq, And
# # x, y = symbols('x y')
# # p1 = plot_implicit(Eq(x**2 + y**2, 5))

# # p3 = plot_implicit(Eq(x**2 + y**2, 5),
# #         (x, -4, 4), (y, -4, 4), depth = 2)

# # # PLOTTING USING BOOLEAN CONJUNCTIONS.
# # p6 = plot_implicit(y > x**2)
# # p7 = plot_implicit(And(y > x, y > -x))
# # p8 = plot_implicit(y - 1, y_var=y)
# # p9 = plot_implicit(x - 1, x_var=x)

import numpy as np
import sympy as sp

def expr():
    x, y =sp.symbols('x y')
    def fn(x):
        if x <= 0.5:
            return 1
        else:
            return 2
    return fn, x


f, x = expr()
sp.plot(f, (x,0,1))
