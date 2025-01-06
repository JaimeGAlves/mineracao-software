# 🗂️ Mineração de Repositórios Git
#### Este projeto utiliza a biblioteca **GitPython** para analisar commits em um repositório Git e gerar dois relatórios sobre as alterações feitas no código em um período específico. O script permite extrair informações detalhadas sobre os commits e resumidas sobre os arquivos afetados, incluindo estatísticas de inserções e remoções de linhas.

---

## 🖥️ Requisitos:
#### - Python 3.x

---

### 📦 Bibliotecas Python:
- **gitpython**: Para interagir com o repositório Git.
- **datetime**: Para manipulação de datas.

---

## 🚀 Como Usar:

### ⚠️ **É RECOMENDADO CRIAR UM AMBIENTE VIRTUAL**

```bash
python -m venv venv
```

## 🔽 No Windows:

```bash
venv\Scripts\activate
```

## 🐧 No Linux/macOS:

```bash
source venv/bin/activate
```

## Instale as dependências com o comando:

```bash
pip install -r requirements.txt
```

---

## 1️⃣ Configuração do Script:

## Edite o arquivo do script para definir os parâmetros do repositório e o intervalo de datas desejado:

#### diretorio_repositorio: Caminho para o repositório Git local que será analisado.
#### data_inicio: Data de início do intervalo para análise (formato: dd/mm/yyyy).
#### data_fim: Data de fim do intervalo para análise (formato: dd/mm/yyyy).

## Exemplo de configuração no script:

```bash
diretorio_repositorio = "/caminho/para/o/repositorio"
data_inicio = "01/01/2025"
data_fim = "31/12/2025"
```

---

## 2️⃣ Execução:
## Para executar o script, basta rodá-lo em seu terminal ou editor de Python:

```bash
python script_mineracao.py
```
Após a execução, serão gerados dois arquivos de relatório:
relatorio_detalhado.txt: Contém informações detalhadas sobre os commits, como hash, autor, data e arquivos alterados.
relatorio_resumido.txt: Contém um resumo dos arquivos alterados e as estatísticas agregadas de inserções e remoções de linhas.

---

## 3️⃣ Saída dos Relatórios:
## Relatório Detalhado

### Este arquivo contém informações sobre cada commit que ocorreu no repositório durante o intervalo de datas, incluindo:

#### Commit (hash), Autor e e-mail do autor, Data do commit, Arquivos modificados/criados, Linhas adicionadas e removidas para cada arquivo
---
## Relatório Resumido

### Este arquivo contém um resumo:

#### Lista de arquivos alterados/criados durante o período, Total de linhas adicionadas ao repositório, Total de arquivos alterados/criados

---

## 📝 Exemplos de Saída:
relatorio_detalhado.txt:
```bash
Commit: abc12345
Autor: João da Silva <joao@exemplo.com>
Data: 01/01/2020 10:00:00
Arquivos alterados/criados:
  - src/main.py: 10 linhas adicionadas, 2 linhas removidas
  - src/utils.py: 5 linhas adicionadas, 0 linhas removidas
Total de linhas adicionadas no commit: 15
Total de arquivos alterados/criados no commit: 2
```
---
relatorio_resumido.txt:
```bash
Arquivos alterados/criados:
  - src/main.py
  - src/utils.py

Total de linhas adicionadas: 15
Total de arquivos alterados/criados: 2
```
