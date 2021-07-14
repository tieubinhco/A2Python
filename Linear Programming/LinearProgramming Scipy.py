# linprog() solves only minimization (not maximization) problems and
# doesn’t allow inequality constraints with the greater than or equal to sign (≥).
# To work around these issues,
# you need to modify your problem before starting optimization:


# MIN -Z = -x-2y
#        2x+y <= 20
#        -4x+5y <= 10
#        x-2y <= 2
#        -x+5y = 15
#        x >= 0
#        y >= 0

from scipy.optimize import linprog
obj = [-1, -2]
#      ─┬  ─┬
#       │   └┤ Coefficient for y
#       └────┤ Coefficient for x

lhs_ineq = [[2,  1],  # Red constraint left side
            [-4,  5],  # Blue constraint left side
            [1, -2]]  # Yellow constraint left side

rhs_ineq = [20,  # Red constraint right side
            10,  # Blue constraint right side
            2]  # Yellow constraint right side

lhs_eq = [[-1, 5]]  # Green constraint left side
rhs_eq = [15]       # Green constraint right side

bnd = [(0, float("inf")),  # Bounds of x
       (0, float("inf"))]  # Bounds of y  #Instead of float("inf"), you can use math.inf, numpy.inf, or scipy.inf.

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, A_eq=lhs_eq,
              b_eq=rhs_eq, bounds=bnd, method="revised simplex")

# # # method = "interior-point" selects the interior-point method. This option is set by default.
# # # method = "revised simplex" selects the revised two-phase simplex method.
# # # method = "simplex" selects the legacy two-phase simplex method.

print(opt)
print(opt.fun)
print(opt.success)
print(opt.x)
