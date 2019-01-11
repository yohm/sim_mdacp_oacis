repo_dir = File.expand_path(File.dirname(__FILE__))

localhost = Host.find_by_name("localhost")

sim_params = {
  name: "MDACP_Langevin",
  command: "python #{repo_dir}/run.py",
  support_input_json: false,
  support_omp: true,
  support_mpi: true,
  print_version_command: "cd #{repo_dir} && git describe --always",
  parameter_definitions: [
    {key: "density", type: "Float", default: 0.7, description: ""}, 
    {key: "temperature", type: "Float", default: 0.9, description: "aimed temperature of the heat bath"}, 
    {key: "length", type: "Float", default: 20.0, description: ""}, 
    {key: "total_loop", type: "Integer", default: 50000, description: ""}
  ],
  description: "MDACP Langevin heat bath",
  executable_on: [ localhost ]
}

sim_name = sim_params[:name]
if Simulator.where(name: sim_name).exists?
  puts "simulator #{sim_name} already exists" 
else
  sim = Simulator.create!(sim_params)
end

azr_params = {
  name: "make_plot",
  type: "on_run",
  command: "python #{repo_dir}/plot_figs.py _input/timeseries.dat",
  support_input_json: true,
  support_omp: false,
  support_mpi: false,
  print_version_command: "cd #{repo_dir} && git describe --always",
  files_to_copy: "timeseries.dat",
  auto_run: "first_run_only",
  executable_on: [ localhost ],
  auto_run_submitted_to: localhost
}

azr_name = azr_params[:name]
sim = Simulator.find_by_name(sim_name)
if sim.analyzers.where(name: azr_name).exists?
  puts "analyzer #{azr_name} already exists"
else
  sim.analyzers.create!(azr_params)
end
