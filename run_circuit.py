from qiskit.quantum_info import SparsePauliOp
from qiskit_ibm_runtime import (
    SamplerV2 as Sampler,
    EstimatorV2 as Estimator,
)
from config_ibm import Config

"""Classe que vai setar e rodar os modelos de excução.
    *Sample: Mede um circuito e retorna probabilidades (quase-distribuições) dos diferentes resultados possíveis (bitstrings).
    *Estimator: Calcula o valor esperado (expected value) de um operador (geralmente um Hamiltoniano) dado um circuito.
    *Simulador: Executa circuitos quanticamente, mas no seu computador (clássico), em vez de usar um backend quântico real.
"""
class RunCircuit:

    def __init__(self, sample: Config):
        self.sample = sample

    def set_sample(self):
        return Sampler(mode=self.sample.set_backend())

    def set_estimator(self):
        return Estimator(mode=self.sample.set_backend())

    def set_simulator(self):
        return Sampler(mode=self.sample.set_simulator())

    def run_sample(self, job):
        return self.set_sample().run([job])

    def run_estimator(self, job):
        observable = SparsePauliOp("X" * job.num_qubits)
        return self.set_estimator().run([(job, observable)])

    def run_simulator(self, job):
        return self.set_simulator().run([job], shots=1024)