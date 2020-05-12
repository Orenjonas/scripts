from sympy import symbols
from sympy.plotting import plot
import numpy as np
import matplotlib

# x = symbols('x')
# # print(sp.expand(((2*x+1)*(2*x-1)**2)))

# # n = 3
# # xvals = np.linspace(-1, 1, n)
# # points = [(x, f(x)) for x in xvals]

# lamd = 2
# def func(x):
#     return (sp.exp(-lamd*x)/(lamd*x))

# a = 0
# b = 2
# x = np.linspace(a, b, 100)
# plt.plot(

# p = plot(sp.Abs(x), (x, -1,1), ylim=[-1,1], show=False)
# for n in range(20,31, 5):
#     xvals = np.linspace(-1, 1, n)
#     points = [(x, f(x)) for x in xvals]
#     plot(interpolate(points, x), (x, -1,1))#, show=False)
#     # p.append(p0[0])
# p.show()

# # print(sp.diff("x**3"))

# ## PLOT MULTIPLE FUNCTIONS
# # p1 = plot(abs(x), x*x, 7/3*x*x - 3/4*x**4, (x, -1.0, 1.0))


# ## 3D PLOTTING
# # from sympy.plotting import plot3d
# # x, y = symbols('x y')
# # plot3d(x*y, (x, -5, 5), (y, -5, 5))

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
