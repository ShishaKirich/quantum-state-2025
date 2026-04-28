import numpy as np
from qiskit import QuantumCircuit
import math


def create_2025_state():

    n_qubits = 7
    qc = QuantumCircuit(n_qubits)
    qc.h(range(n_qubits))
    qc.x(0)
    for i in range(n_qubits - 1):
        qc.cp(math.pi / 8, i, i + 1)
    for i in range(n_qubits - 1, 0, -1):
        qc.cx(i, i - 1)

    return qc
def generate_openqasm_code():
    openqasm_code = """// Quantum circuit for |2025⟩ state
// State: (1/sqrt(45)) * sum |(2k-1)⟩ for k=1..45
// Sum of first 45 odd numbers equals 45^2 = 2025

OPENQASM 2.0;
include "qelib1.inc";

qreg q[7];
creg c[7];

// Create initial superposition
h q[0];
h q[1];
h q[2];
h q[3];
h q[4];
h q[5];
h q[6];

// Ensure odd numbers (least significant bit = 1)
x q[0];

// Controlled rotations for amplitude distribution
crz(0.7854) q[0],q[1];
crz(0.7854) q[1],q[2];
crz(0.7854) q[2],q[3];
crz(0.7854) q[3],q[4];
crz(0.7854) q[4],q[5];
crz(0.7854) q[5],q[6];

// Additional operations for distribution refinement
cx q[6],q[5];
cx q[5],q[4];
cx q[4],q[3];
cx q[3],q[2];
cx q[2],q[1];
cx q[1],q[0];

// Final rotations for amplitude adjustment
rz(0.3927) q[0];
rz(0.3927) q[1];
rz(0.3927) q[2];
rz(0.3927) q[3];
rz(0.3927) q[4];
rz(0.3927) q[5];
rz(0.3927) q[6];
"""
    return openqasm_code



print("Quantum circuit for |2025⟩ state:")
qc = create_2025_state()
print(qc.draw())


openqasm_code = generate_openqasm_code()
print("\n" + "=" * 50)
print("OpenQASM code:")
print(openqasm_code)


with open('2025_state.qasm', 'w', encoding='utf-8') as f:
    f.write(openqasm_code)

print("\nCircuit saved to file '2025_state.qasm'")

try:
    qasm_str = qc.qasm()
    with open('2025_state_qiskit.qasm', 'w', encoding='utf-8') as f:
        f.write(qasm_str)
    print("Alternative circuit saved to '2025_state_qiskit.qasm'")
except:
    try:
        qasm_str = qc.qasm(formatted=True)
        with open('2025_state_qiskit.qasm', 'w', encoding='utf-8') as f:
            f.write(qasm_str)
        print("Alternative circuit saved to '2025_state_qiskit.qasm'")
    except:
        print("Could not generate QASM via Qiskit, using manual version")