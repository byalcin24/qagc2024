from challange_2024 import problem_hamiltonian

n_qubits = 28

ham = problem_hamiltonian(n_qubits, 1, hamiltonian_directory="app/src/hamiltonian/data")
print(ham)