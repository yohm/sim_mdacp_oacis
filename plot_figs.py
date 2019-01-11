import sys
import numpy as np

def plot_figs(dat):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    plt.xlabel("t")
    plt.ylabel("temperature")
    plt.plot( dat[:,0], dat[:,1], 'o-')
    plt.savefig("temperature_t.png")
    plt.clf()

    plt.xlabel("t")
    plt.ylabel("pressure")
    plt.plot( dat[:,0], dat[:,2], 'o-')
    plt.savefig("pressure_t.png")
    plt.clf()

    plt.xlabel("t")
    plt.ylabel("energy")
    plt.plot( dat[:,0], dat[:,3], 'o-')
    plt.savefig("energy_t.png")
    plt.clf()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write("[Error] wrong number of argument\n")
        sys.stderr.write("  Usage: python plot_figs.py timeseries.dat\n")
        raise Exception("wrong number of arguments")
    fname = sys.argv[1]
    dat = np.loadtxt(fname, comments='#', delimiter=' ')
    plot_figs(dat)

