import matplotlib.pyplot as plt

x_values = [i for i in range(1, 6)]
y_values = [i**3 for i in range(1, 6)]

plt.scatter(x_values, y_values, s=200)

plt.title("Practice", fontsize=24)
plt.xlabel("X Value", fontsize=14)
plt.ylabel("Y Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()