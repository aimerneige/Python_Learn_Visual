import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    plt.scatter(rw.x_values[0],  rw.y_values[0],
                c='green', edgecolors='none', s=20)
    plt.scatter(rw.x_values[-1], rw.y_values[-1],
                c='red',   edgecolors='none', s=20)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
