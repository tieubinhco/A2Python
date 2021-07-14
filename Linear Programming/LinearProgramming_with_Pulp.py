from pulp import LpMaximize, LpMinimize, LpProblem, LpStatus, lpSum, LpVariable, GLPK

# Create the model
model = LpProblem(name="small-problem", sense=LpMinimize)

# Initialize the decision variables
x1 = LpVariable(name="x1", lowBound=0, cat='Continuous') # cat can be Integer of Binary
x2 = LpVariable(name="x2", lowBound=0, cat='Continuous')
x3 = LpVariable(name="x3", lowBound=0, cat='Continuous')
x4 = LpVariable(name="x4", lowBound=0, cat='Continuous')
x5 = LpVariable(name="x5", lowBound=0, cat='Continuous')

# expression = 2 * x + 4 * y
# type(expression)
# constraint = 2 * x + 4 * y >= 8
# type(constraint)

# Add the constraints to the model
model += (-x1 + x2-x3 == 1, "red_constraint")
model += (2*x1 + x2-x4 == 2, "blue_constraint")
model += (x1 <= 3, "yellow_constraint")

# Add the objective function to the model
obj_func = x1 + 2 * x2
model += obj_func

# Solve the problem
status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")
for var in model.variables():
    print(f"{var.name}: {var.value()}")

for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")
