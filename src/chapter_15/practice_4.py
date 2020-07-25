import matplotlib.pyplot as plt
from random import choice

class RandomWalk():

    def __init__(self,  num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_or_y = choice([1, 2])
            x_step = 0
            y_step = 0
            if x_or_y == 1:
                x_step = choice([1, -1])
            elif x_or_y == 2:
                y_step = choice([1, -1])

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)



while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    plt.scatter(rw.x_values[0],  rw.y_values[0],
                c='green', edgecolors='none', s=80)
    plt.scatter(rw.x_values[-1], rw.y_values[-1],
                c='red',   edgecolors='none', s=80)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
