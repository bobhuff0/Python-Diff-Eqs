# QUIZ
#
# Add the model for heat_conduction along
# a wire to the function heat_conduction
# below.

from udacityplots import *

ambient_temperature = 300. # K
flame_temperature = 1000. # K
coefficient = 10. # 1 / s
dx = 0.001 # m
size = 100 # grid units
positions = dx * numpy.arange(size) # m
h = 0.01 # s
end_time = 10.0 # s
num_steps = int(end_time / h)

# This is used to keep track of the data that we want to plot.
data = []

def heat_conduction():
    temperatures_old = ambient_temperature * numpy.ones(size) # K
    for i in range(4 * size / 10, 5 * size / 10):
        temperatures_old[i] = flame_temperature
    temperatures_new = numpy.copy(temperatures_old) # K

    for step in range(num_steps):
        if step % 100 == 0:
            data.append(([pos for pos in positions],
                          [temp for temp in temperatures_old]))
        for i in range(1, size - 1):
            ###Your code here.

        # Switch values of temperatures_new and temperatures_old
        # for the next iteration of the for loop.
        temperatures_new, temperatures_old = temperatures_old, temperatures_new

    return temperatures_old

temperatures = heat_conduction()

@show_plot
def plot_me():
    for (pos, temp) in data:
        matplotlib.pyplot.plot(pos, temp)
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Position in m')
    axes.set_ylabel('Temperature in K')

plot_me()
