# Projeto de Circuitos Quânticos com Qiskit ⚛️

Este projeto foi desenvolvido com o objetivo de estudar e praticar a criação de circuitos quânticos utilizando o **Qiskit**, da IBM. A versão utilizada foi a **2.0.2**. O projeto conta com três módulos principais:

- **Sample**: Geração e visualização de circuitos quânticos de exemplo.
- **Simulador**: Execução dos circuitos de forma simulada.
- **Estimator**: Estimativas de resultados a partir da execução dos circuitos.

##  Objetivo

O foco principal deste projeto foi o **aprendizado prático** do funcionamento de circuitos no **IBM Quantum**, utilizando as ferramentas disponibilizadas pelo Qiskit. A ideia é oferecer uma base para testar, simular e estimar comportamentos de circuitos quânticos.

## Tecnologias Utilizadas

- **Linguagem:** Python 
- **Framework:** Qiskit 2.0.2 (versão antiga mas funcional até dia 1 de julho 2025)
- **Acesso à IBM Quantum:** API key via `properties.yaml`

##  Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```b̀ash
python -m venv venv
source venv/bin/activate
venv\Scripts\activate```

### 3. Instale as dependências

```b̀ash
pip install -r requirements.txt
```

### 4. Adicione sua chave de API da IBM Quantum
No arquivo `properties.yaml` na raiz do projeto faça a troca do "TOKEN_ACCESS" pela a sua chave de acesso:

```b̀ash
key:
    ibm:"TOKEN_ACCESS"```

### Observações
- O projeto foi desenvolvido com foco em aprendizado, portanto não é voltado para produção.

- Certifique-se de que sua chave da IBM está ativa e válida.

- Os módulos podem ser adaptados para diferentes experiências com circuitos quânticos.

### Autor
Desenvolvido por José Ismael Palliano Evaldt com o propósito de estudo e prática.
