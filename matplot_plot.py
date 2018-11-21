from matplotlib import pyplot


def draw_the_plots(n_loop=10, elapsed_times=None, elapsed_times2=None, se1=None, se2=None):
    # axis X
    x = list(range(1, n_loop + 1, 1))

    # plot lines
    if elapsed_times is None and elapsed_times2 is None:
        return

    if elapsed_times is not None:
        pyplot.plot(x, elapsed_times, label="non-busy-waiting", marker='.', linestyle='--', linewidth='1', )
        if se1 is not None and elapsed_times2 is None:
            pyplot.errorbar(x, elapsed_times, se1, fmt='none')
            pass

    if elapsed_times2 is not None:
        pyplot.plot(x, elapsed_times2, label="busy-waiting", marker='2', linestyle=':', linewidth='1')
        if elapsed_times is None:
            pyplot.errorbar(x, elapsed_times2, se2, fmt='none')
            pass

    # plot decoration
    pyplot.title("Performance Analyses")
    pyplot.xlabel("How many times the process C has consumed")
    pyplot.ylabel("The accumulative elapsed time (in nanosecond)")
    pyplot.legend(loc="upper left")
    pyplot.grid()
    pyplot.xlim(0, 11)

    # show the plot
    pyplot.show()


if __name__ == '__main__':
    # data derived from the first 10 times
    semaphore = [932120.40, 1370503.30, 1829575.80, 2285561.60, 2734148.30, 3186853.40, 3627303.40, 4106710.20,
                 4555282.00, 5076032.30]
    semaphore_se = [90296.00, 126882.57, 172793.00, 177417.17, 188683.79, 195322.46, 209303.02, 270088.13, 279048.05,
                    271880.42]
    busy_waiting = [51372140.00, 40077296.00, 99761192.70, 102897144.10, 64054388.50, 122244159.40, 97201609.70,
                    66905499.00, 95434656.20, 83018492.20]
    busy_waiting_se = [70754196.43, 73052704.85, 106945463.12, 126149250.17, 114227753.82, 121650495.98, 121620927.78,
                       113231037.71, 90613342.55, 119944286.88]

    # data derived from valid part from the 50 times
    s1 = [952062.06, 1404340.32, 1858258.92, 2318424.76, 2777071.88, 3240547.76, 3684200.82, 4175949.00, 4675875.82,
          5166361.92]
    se1 = [202261.71, 208502.52, 221823.45, 225574.13, 233953.98, 243500.53, 252043.84, 309197.04, 434971.52, 440096.43]
    s2 = [81401899.12, 78595747.00, 96720242.47, 73802317.47, 86406862.33, 113321935.51, 75721500.23, 71811626.84,
          102355011.30, 92631277.79]
    se2 = [80598657.30, 83940348.92, 106958346.35, 88379818.08, 106084843.00, 114382633.24, 102823248.70, 88015500.51,
           100263936.56, 87994272.34]
    draw_the_plots(elapsed_times=semaphore, se1=semaphore_se, elapsed_times2=busy_waiting, se2=busy_waiting_se)
    draw_the_plots(elapsed_times=semaphore, se1=semaphore_se)
    draw_the_plots(elapsed_times2=busy_waiting, se2=busy_waiting_se)

    draw_the_plots(elapsed_times=s1, se1=se1, elapsed_times2=s2, se2=se2)
    draw_the_plots(elapsed_times=s1, se1=se1)
    draw_the_plots(elapsed_times2=s2, se2=se2)
