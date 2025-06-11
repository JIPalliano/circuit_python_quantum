from qiskit import QuantumCircuit

"""Classe que contém os circuitos."""
class Circuit:

    @staticmethod
    def ascii_to_qubits(text):
        """Converte uma string em um circuito quântico, com 7 qubits por text."""
        n_qubits = 7 * len(text)
        #variavel que vai separar os qubits e bits da maquina classica
        circuit = QuantumCircuit(n_qubits, n_qubits)

        print(f"🧾 Convertendo '{text}' para binário e aplicando X gates:")
        for i, char in enumerate(text):
            ascii_bin = format(ord(char), '07b')
            print(f"  '{char}' -> {ascii_bin}")
            offset = i * 7  # deslocamento dos qubits para cada text

            for j, bit in enumerate(ascii_bin):
                if bit == '1':
                    circuit.x(offset + j)  # aplica X nos qubits que representam '1'

        circuit.measure(range(n_qubits), range(n_qubits))
        return circuit
