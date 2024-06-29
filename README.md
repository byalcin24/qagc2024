# qagc2024

## Setup

Tested with Python 3.10.11

Follow these steps to set up the project:

1. **Set up the virtual environment and install dependencies**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run the project**
   ```bash
   jupyter notebook app/src/bencmark_vqe_upd.ipynb
   ```
#
##### Several parts of this project were inspired from the Official Qiskit Repository and IBM Quantum Tutorials, including but not limited to:
* https://qiskit-community.github.io/qiskit-algorithms/stubs/qiskit_algorithms.AdaptVQE.html <br>
* https://docs.quantum.ibm.com/api/qiskit/0.40/qiskit.algorithms.optimizers.QNSPSA <br>
* https://docs.quantum.ibm.com/api/qiskit/0.40/qiskit.algorithms.minimum_eigensolvers.AdaptVQE <br>
* https://learning.quantum.ibm.com/tutorial/variational-quantum-eigensolver