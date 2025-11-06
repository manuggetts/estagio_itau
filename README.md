# Análise de pesquisa de atendimento

Este projeto realiza a análise de uma planilha de **Pesquisa de Atendimento** de gerentes de um banco. Ele identifica os gerentes bem e mal avaliados, calcula médias, gera gráficos e salva os resultados em arquivos organizados.

---

## Estrutura do projeto

```text
project_root/
│
├─ venv/
├─ data/
│   └─ Pesquisa de atendimento_Vaga Estágio.xlsx
├─ outputs/
│   └─ Arquivos gerados a partir da análise
├─ main.py
└─ requirements.txt
```

## Dependências

As bibliotecas utilizadas são:
```text
pandas

matplotlib

openpyxl
```

### Instale todas as dependências com:
```text
pip install -r requirements.txt
```

## Como rodar

1. Certifique-se de que a planilha esteja na pasta data/.

2. Ative seu ambiente virtual (opcional, mas recomendado):

#### Windows
```text
venv\Scripts\activate
```
#### Linux/Mac
```text
source venv/bin/activate
```

### Execute o script principal:
```text
python main.py
```
## Funcionalidades

- Leitura dos dados da planilha de reclamações e gerentes.

- Separação dos atendimentos em:

    * Gerentes bem avaliados (nota 6 a 10)

    * Gerentes mal avaliados (nota 1 a 5)

- Cálculo da média de nota por gerente e média geral.

- Geração de gráfico horizontal com médias de cada gerente (outputs/media_por_gerente.png).

- Exportação dos resultados para Excel (outputs/resultados.xlsx) com abas:

    * Média por gerente

    * Bem avaliados

    * Mal avaliados

- Impressão no terminal de resumo geral e detalhes por gerente.

## Resultados esperados

- Gráfico de barras horizontais com a média de cada gerente.

    * <img width="1472" height="704" alt="itau" src="https://github.com/user-attachments/assets/d84549b0-ad30-4624-8d29-5afe5928073e" />

- Planilha resultados.xlsx com abas separadas para análise rápida.

    * <img width="482" height="206" alt="Captura de tela 2025-11-06 051453" src="https://github.com/user-attachments/assets/405b421f-5ac9-4a93-b93c-0ce91887ad2e" />

- Saída no terminal mostrando:

    * Total de atendimentos

    * Média geral das notas
      
    * Média por gerente

    * Gerentes bem avaliados e mal avaliados com justificativas
 
      * <img width="712" height="373" alt="Captura de tela 2025-11-06 052013" src="https://github.com/user-attachments/assets/54c0b73e-cf4e-4b33-a7ad-72209355cfa5" />


### Observações

##### As notas são consideradas bem avaliadas se ≥ 6 e mal avaliadas se ≤ 5.

##### O mapeamento de gerentes é tratado automaticamente pelo código.

##### A pasta outputs/ é criada automaticamente se não existir.
