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
