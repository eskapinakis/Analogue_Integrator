
# values are pairs of the form (x,f(x))
# the integral has pairs of the form [x,F(x)]
def integrate(values_of_f, step=1):
    k = 0
    integral_values = []
    for m in values_of_f:
        integral_values.append([m[0], k])
        k += m[1]*step
    return integral_values


"""

step = 0.01


def f(u):
    return math.sin(u)


A = [[a, f(a)] for a in np.arange(0, 10, step)]
B = Integrator.integrate(A, step)


plt.plot([v[0] for v in A], [v[1] for v in A], label='f(x)')
plt.plot([v[0] for v in A], [v[1] for v in B], label='F(x)')
plt.legend()
plt.show()

"""
