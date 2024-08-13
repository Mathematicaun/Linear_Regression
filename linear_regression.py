import numpy as np  # Import NumPy library for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib library for plotting

# Set step size for data points
step = 1/2
# Number of data points
cardinality = 20
# Unused variable (can be removed)
Range = 2

class summation:
    def __init__(self, a1, a2):
        """
        Initializes the summation class.

        Args:
            a1: First array for summation.
            a2: Second array for summation.
        """
        self.a = a1  # Store the first array
        self.b = a2  # Store the second array

    def sum_s(self):
        """Calculates the sum of the product of corresponding elements in a and b."""
        sum1 = 0
        for i in range(cardinality):
            sum1 += self.a[i]*self.b[i]
        return sum1

    def sum_d(self):
        """Calculates the square of the sum of elements in a and b."""
        def sub_sum_d_():
            """Calculates the sum of elements in a."""
            sub_sum_d_1 = 0
            for i in range(cardinality):
                sub_sum_d_1 += self.a[i]
            return sub_sum_d_1

        def sub_sum_d__():
            """Calculates the sum of elements in b."""
            sub_sum_d__1 = 0
            for i in range(cardinality):
                sub_sum_d__1 += self.b[i]
            return sub_sum_d__1

        return sub_sum_d_() * sub_sum_d__()  # Return the product of the sums

def sum(x):
    """Calculates the sum of elements in an array."""
    l = 0
    for i in range(cardinality):
        l += x[i]
    return l

# Generate random data
x = np.array([np.random.rand()*.7 + (1/50)*_ for _ in range(cardinality)])
y = np.arange(0, step*cardinality, step)

# Create a summation object
operator = summation(x, y)

# Plotting setup
fig = plt.figure()
ax = fig.add_subplot()
fig.set_facecolor('#191724')
ax.set(ylim=[0, 1], xlim=[-5, 15])
ax.set_facecolor('#191724')

# Plot data points
ax.plot(y, x, color='#9ccfd8')
ax.scatter(y, x, marker='.', color='#e27aa4')

# Calculate regression line coefficients
m_min = (cardinality*operator.sum_s() - operator.sum_d())/(cardinality*sum(y**2)-(sum(x))**2)
c_min = (sum(x)-m_min*sum(y))/cardinality

# Plot the regression line
k = np.linspace(-3, 13)
ax.plot(k, m_min*k+c_min, color=[1/2, 1/4, 1/8, 1][::-1], label='regression line')
Legend = plt.legend(frameon=False, loc='best')
for _ in Legend.get_texts():
    _.set_color('white')

# Plot customization
plt.grid(color='gray', alpha=.15)
ax.set_xlabel('$\\text{x data point}$', color='white')
ax.set_ylabel('$\\text{y data point}$', color='white')
ax.set_xticklabels(np.arange(0, step*cardinality, step), color='gray')

spiness = ['bottom', 'top', 'left', 'right']

for _ in spiness:
    if _ == spiness[0] or _ == spiness[2]:
        ax.spines[_].set(color=[1/2, 1/4, 1/8, 1][::-1], alpha=.5)
    else:
        ax.spines[_].set(visible=False)
#fig.savefig('data_points.png', dpi=500)
plt.show()
