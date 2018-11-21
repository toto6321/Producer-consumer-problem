from matplotlib import pyplot


def draw_the_plots(elapsed_times, elapsed_times2=None, se1=None, se2=None):
    if elapsed_times is None:
        return

    # axis X
    x = list(range(1, len(elapsed_times) + 1, 1))

    # plot lines
    pyplot.plot(x, elapsed_times, label="non-busy-waiting", marker='.', linestyle='--', linewidth='1')
    if se1 is not None and elapsed_times2 is None:
        pyplot.errorbar(x, elapsed_times, se1, fmt='none')
        pass
    if elapsed_times2 is not None:
        pyplot.plot(x, elapsed_times2, label="busy-waiting", marker='2', linestyle=':', linewidth='1')

    # plot decoration
    pyplot.title("Performance Analysis")
    pyplot.xlabel("How many times the process C has consumed")
    pyplot.ylabel("The accumulative elapsed time (in nanosecond)")
    pyplot.legend(loc="upper left")
    pyplot.grid()
    pyplot.xlim(0, 11)

    # show the plot
    pyplot.show()


if __name__ == '__main__':
    # data derived from the first 10 times
    busy_waiting = [2701310, 16499266, 16511120, 16534789, 17275356, 14258888, 20473341, 14679081, 20529757, 15098302]

    semaphore = [952062.06, 1404340.32, 1858258.9, 2318424.76, 2777071.88, 3240547.76, 3684200.82, 4175949.00,
                 4675875.82,
                 5166361.92]
    semaphore_se = [202261.71, 208502.52, 221823.45, 225574.13, 233953.98, 243500.53, 252043.84, 309197.04, 434971.52,
                    440096.43]

    # data derived from valid part from the 50 times
    s1 = [952062.06, 1404340.32, 1858258.92, 2318424.76, 2777071.88, 3240547.76, 3684200.82, 4175949.00, 4675875.82,
          5166361.92]
    se1 = [202261.71, 208502.52, 221823.45, 225574.13, 233953.98, 243500.53, 252043.84, 309197.04, 434971.52, 440096.43]
    s2 = [81401899.12, 78595747.00, 96720242.47, 73802317.47, 86406862.33, 113321935.51, 75721500.23, 71811626.84,
          102355011.30, 92631277.79]
    se2 = [80598657.30, 83940348.92, 106958346.35, 88379818.08, 106084843.00, 114382633.24, 102823248.70, 88015500.51,
           100263936.56, 87994272.34]
    draw_the_plots(elapsed_times=s1, se1=se1, elapsed_times2=s2, se2=se2)
    draw_the_plots(elapsed_times=s1, se1=se1)
    draw_the_plots(elapsed_times=s2, se1=se2)
