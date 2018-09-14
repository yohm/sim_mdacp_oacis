import sys,os,subprocess,json,textwrap
import numpy as np

def create_config(outfile):
    if len(sys.argv) != 6:
        sys.stderr.write("usage: python run.py <density> <temperature> <length> <TotalLoop> <seed>\n")
        raise("invalid number of arguments")
    density = float(sys.argv[1])
    temperature = float(sys.argv[2])
    length = float(sys.argv[3])
    total_loop = int(sys.argv[4])
    seed = int(sys.argv[5])
    template = textwrap.dedent('''\
               Mode=Langevin
               InitialVelocity=1.8
               TimeStep=0.005
               UnitLength={2}
               ObserveLoop=100
               TotalLoop={3}
               AimedTemperature={1}
               Density={0}
               HeatbathTau=0.1
               HeatbathGamma=0.1
               HeatbathType=Langevin
               Seed={4}
               ''')
    with open(outfile, 'w') as f:
        f.write(template.format(density,temperature,length,total_loop,seed))

create_config("langevin.cfg")

def run_simulator(cfgfile, dat_file):
    simulator = os.path.abspath(os.path.dirname(__file__)) + "/mdacp/mdacp"
    n_mpi = os.environ['OACIS_MPI_PROCS']
    cmd = ["mpirun", "-n", n_mpi, simulator, cfgfile]
    with open(dat_file, 'w') as f:
        subprocess.check_call(cmd, stdout=f)

run_simulator("langevin.cfg", "timeseries.dat")

dat = np.loadtxt("timeseries.dat", comments='#', delimiter=' ')

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

plot_figs(dat)

def print_json(dat):
    avg_t = np.average(dat[-200:,1])
    avg_p = np.average(dat[-200:,2])
    avg_e = np.average(dat[-200:,3])
    j = {"temperature": avg_t, "pressure": avg_p, "energy": avg_e}
    with open("_output.json", 'w') as f:
        json.dump(j, f)

print_json(dat)

