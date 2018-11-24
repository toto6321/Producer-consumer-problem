import pandas
from matplotlib import pyplot


def draw_the_plots(n_loop=10):
    # read from the csv files
    df_non_busy_50_origin = pandas.read_csv("statistics_non-busy-waiting_50.csv", names=list(range(1, n_loop + 1, 1)))
    df_busy_50_origin = pandas.read_csv("statistics_busy-waiting_50.csv", names=list(range(1, n_loop + 1, 1)))

    # data filtering
    df_non_busy_50 = df_non_busy_50_origin[(df_non_busy_50_origin > 0).all(1)]
    df_busy_50 = df_busy_50_origin[(df_busy_50_origin > 0).all(1)]

    # generate mean values and standard derivation
    data1_50 = df_non_busy_50.agg(['mean', 'std'])
    data2_50 = df_busy_50.agg(['mean', 'std'])

    # mean values
    m1_50 = data1_50.iloc[0]
    m1_50.reindex(["non-busy-waiting"], axis=1)
    m2_50 = data2_50.iloc[0]
    m2_50.reindex(["busy-waiting"], axis=1)

    # mean values plots
    df_mean = pandas.concat([m1_50, m2_50], axis=1, keys=["non-busy-waiting", "busy-waiting"])
    df_mean.plot()

    # plot decoration
    pyplot.title("Performance Analysis")
    pyplot.xlabel("How many times the process C has consumed")
    pyplot.ylabel("The accumulative elapsed time (in nanosecond)")
    pyplot.legend(loc="upper left")
    pyplot.grid()
    pyplot.xlim(0, 11)

    pyplot.show()


if __name__ == '__main__':
    draw_the_plots()
