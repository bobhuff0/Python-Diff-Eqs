# QUIZ
# 
# Modify the harvest function below to 
# demonstrate ramping up the rate at 
# which fish are harvested.

from udacityplots import *

harvest_rates = [1e3,4e3,10e3] # tons / year

maximum_growth_rate = 0.5 # 1 / year
carrying_capacity = 2e6 # tons
maximum_harvest_rate = 0.8 * 2.5e5 # tons / year
ramp_start = 4. # years
ramp_end = 6. # years

end_time = 10. # years
h = 0.1 # years
num_steps = int(end_time / h)
times = h * numpy.array(range(num_steps + 1))


def harvest():
    fish = numpy.zeros(num_steps + 1) # tons
    fish[0] = 2e5

    is_extinct = False

    for hr in harvest_rates:
        for step in range(num_steps):


            if is_extinct:
                fish_next_step = 0.
            else:
                fish_next_step = fish[step] + h * (maximum_growth_rate * (1. - fish[step] / carrying_capacity) * fish[step] - hr)
                if fish_next_step <= 0.:
                    is_extinct = True
                    fish_next_step = 0.
            fish[step + 1] = fish_next_step

    matplotlib.pyplot.plot(times, fish)
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Time in years')
    axes.set_ylabel('Amount of fish in tons')

    return fish

fish = harvest()

