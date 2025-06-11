from config_ibm import Config
from run_circuit import RunCircuit
from circuits import Circuit

def main():

    text = 'Hello world'
    run = RunCircuit(Config())

    # Gera o circuito
    circuit = Circuit.ascii_to_qubits(text)
    print("Circuito gerado:")
    print(circuit)

    # Executa no simulador, estimator ou sample
    result = run.run_estimator(circuit)

    # Imprime o resultado bruto
    print("Resultado da simulação:")
    print(result.result())


if __name__ == "__main__":
    main()