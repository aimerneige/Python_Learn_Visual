import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [i**2 for i in range(1, 1001)]
plt.scatter(x_values, y_values, s=40)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])

plt.show()