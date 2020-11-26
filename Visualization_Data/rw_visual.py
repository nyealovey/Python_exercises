import matplotlib.pyplot as plt

from Visualization_Data.random_walk import RandomWalk

# 创建一个Randomwalk的实例
while True:

    rw = RandomWalk(1000000)
    rw.fill_walk()
    points_numbers = list(range(rw.num_points))
    plt.scatter(0,0, c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1], c='red',
                edgecolors='none',s=100)
    plt.scatter(rw.x_values, rw.y_values,
                c=points_numbers, cmap=plt.cm.Blues, edgecolor='none', s=5)
    plt.show()

    keep_running = input("是否再来一次(y/n)")
    if keep_running == 'n':
        break
