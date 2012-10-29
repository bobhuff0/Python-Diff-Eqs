# QUIZ
#
# In the seir_model function below,
# solve the SEIR model using the
# Forward Euler Method.

from udacityplots import *

h = .25 # days
transmission_coeff = 5e-9 # 1 / day person
latency_time = 1. # days
infectious_time = 5. # days

end_time = 60.0 # days
num_steps = int(end_time / h)
times = h * numpy.array(range(num_steps + 1))

def seir_model():

    s = numpy.zeros(num_steps + 1)
    e = numpy.zeros(num_steps + 1)
    i = numpy.zeros(num_steps + 1)
    r = numpy.zeros(num_steps + 1)

    s[0] = 1e8 - 1e6 - 1e5
    e[0] = 0.
    i[0] = 1e5
    r[0] = 1e6

    for step in range(num_steps):
        s2e = h * transmission_coeff * s[step] * i[step]
        e2i = h/latency_time * e[step]
        i2r = h/infectious_time * i[step]
        s[step+1] = s[step] - s2e
        e[step+1] = e[step] + s2e - e2i
        i[step+1] = i[step] + e2i - i2r
        r[step+1] = r[step] + i2r

    return s, e, i, r

s, e, i, r = seir_model()

@show_plot
def plot_me():
    s_plot = matplotlib.pyplot.plot(times, s)
    e_plot = matplotlib.pyplot.plot(times, e)
    i_plot = matplotlib.pyplot.plot(times, i)
    r_plot = matplotlib.pyplot.plot(times, r)
    matplotlib.pyplot.figlegend((s_plot, e_plot, i_plot, r_plot), ('S', 'E', 'I', 'R'), 'upper right')

    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Time in days')
    axes.set_ylabel('Number of persons')
    matplotlib.pyplot.xlim(xmin = 0.)
    matplotlib.pyplot.ylim(ymin = 0.)

plot_me()


