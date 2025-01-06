from git import Repo
from datetime import datetime

def analisar_repositorio(diretorio_repositorio, data_inicio, data_fim):
    
    repositorio = Repo(diretorio_repositorio)

    data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")
    data_fim = datetime.strptime(data_fim, "%d/%m/%Y")

    branches = [branch.name for branch in repositorio.branches]

    relatorio_detalhado = []
    arquivos_resumo = set()
    total_insercoes = 0

    for branch in branches:
        
        repositorio.git.checkout(branch)

        for commit in repositorio.iter_commits(branch):
            
            data_commit = datetime.fromtimestamp(commit.committed_date)

            if data_inicio <= data_commit <= data_fim:
                
                informacoes_commit = []
                informacoes_commit.append(f"Commit: {commit.hexsha}")
                informacoes_commit.append(f"Autor: {commit.author.name} <{commit.author.email}>")
                informacoes_commit.append(f"Data: {data_commit.strftime('%d/%m/%Y %H:%M:%S')}")

                estatisticas = commit.stats
                total_adicoes = estatisticas.total['insertions']
                total_arquivos = estatisticas.total['files']
                arquivos_modificados = estatisticas.files

                informacoes_commit.append("Arquivos alterados/criados:")
                
                for diretorio_arquivo, alteracoes in arquivos_modificados.items():
                    
                    informacoes_commit.append(f"  - {diretorio_arquivo}: {alteracoes['insertions']} linhas adicionadas, {alteracoes['deletions']} linhas removidas")
                    arquivos_resumo.add(diretorio_arquivo)
                    total_arquivos += 1
                    total_insercoes += alteracoes['insertions']

                informacoes_commit.append(f"Total de linhas adicionadas no commit: {total_adicoes}")
                informacoes_commit.append(f"Total de arquivos alterados/criados no commit: {total_arquivos}\n")
                relatorio_detalhado.append("\n".join(informacoes_commit))

    with open("relatorio_detalhado.txt", "w", encoding="utf-8") as arquivo_detalhado:
        
        arquivo_detalhado.write("\n".join(relatorio_detalhado))

    with open("relatorio_resumido.txt", "w", encoding="utf-8") as arquivo_resumo:
        
        arquivo_resumo.write("Arquivos alterados/criados:\n\n")
        arquivo_resumo.write("\n".join(sorted(arquivos_resumo)))
        arquivo_resumo.write(f"\n\nTotal de linhas adicionadas: {total_insercoes}\n")
        arquivo_resumo.write(f"Total de arquivos alterados/criados: {len(arquivos_resumo)}\n")

if __name__ == "__main__":
    
    diretorio_repositorio = "caminho/para/o/repositorio"
    data_inicio = "00/00/0000"
    data_fim = "00/00/0000"

    analisar_repositorio(diretorio_repositorio, data_inicio, data_fim)