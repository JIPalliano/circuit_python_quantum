import yaml
from qiskit_aer import Aer
from qiskit_ibm_runtime import QiskitRuntimeService

class Config:

    backend: str

    """inicializar a chave de acesso via properties.yaml."""
    def __init__(self, path="properties.yaml"):
        try:
            with open(path, 'r') as file:
                config = yaml.safe_load(file)
                if not isinstance(config, dict):
                    raise ValueError("Formato YAML inválido: o elemento raiz deve ser um mapeamento")
                if 'key' not in config or 'ibm' not in config['key']:
                    raise ValueError("Configuração obrigatória ausente: key.ibm")
                self.ibm_key = config['key']['ibm']
        except yaml.YAMLError as e:
            raise ValueError(f"Erro ao interpretar o arquivo YAML: {e}")
        except FileNotFoundError:
            raise FileNotFoundError("Arquivo de configuração não encontrado: {path}")

    #conecta no QiskitRuntimeService
    def connect_ibm(self):
        return QiskitRuntimeService(channel="ibm_quantum", token= self.ibm_key)

    #seta o computador quantico ou simulador que vai fazer os testes
    def set_backend(self):
        return self.connect_ibm().backend(self.backend_available().name)

    def set_simulator(self):
        return Aer.get_backend("qasm_simulator")

    #faz verificação de quais computadores estão disponiveis, removendo o simulador
    def backend_available(self):
        return min(b, key=lambda x: x.status().pending_jobs) if (
            b := self.connect_ibm().backends(simulator=False, operational=True)) else Exception(
            "Nenhum backend disponível no momento.")

    #retorna o valor da chave em string
    def __str__(self):
        return f"IBM Chave: {self.ibm_key}"