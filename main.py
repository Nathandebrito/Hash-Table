import csv
import time

class Nodo:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo_nodo = None

class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def funcao_hash(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self.funcao_hash(chave)
        if self.tabela[indice] is None:
            self.tabela[indice] = [Nodo(chave, valor)]
        else:
            self.tabela[indice].append(Nodo(chave, valor))

    def buscar(self, chave):
        indice = self.funcao_hash(chave)
        lista_encadeada = self.tabela[indice]
        testes_realizados = 1
        if lista_encadeada is not None:
            for nodo in lista_encadeada:
                if nodo.chave == chave:
                    return nodo.valor, testes_realizados
                testes_realizados += 1
        return None, testes_realizados

def carregar_dados(tabela, arquivo):
    with open(arquivo, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for linha in reader:
            sofifa_id, nome, posicoes = linha
            tabela.inserir(sofifa_id, (nome, posicoes))

def carregar_consultas(arquivo):
    with open(arquivo, "r") as f:
        consultas = [linha.strip() for linha in f.readlines()]
    return consultas

def executar_experimento(tamanho_tabela, arquivo_dados, arquivo_consultas):
    tabela = TabelaHash(tamanho_tabela)
    
    # Carregar dados e medir tempo
    inicio_construcao = time.time()
    carregar_dados(tabela, arquivo_dados)
    fim_construcao = time.time()
    tempo_construcao = fim_construcao - inicio_construcao

    # Calcular estatísticas da tabela
    ocupadas = sum(1 for bucket in tabela.tabela if bucket is not None)
    max_lista = max(len(bucket) for bucket in tabela.tabela if bucket is not None)
    media_lista = sum(len(bucket) for bucket in tabela.tabela if bucket is not None) / ocupadas

    # Carregar consultas e medir tempo
    consultas = carregar_consultas(arquivo_consultas)
    inicio_consultas = time.time()
    resultados_consultas = []
    max_testes = 0
    total_testes = 0

    for consulta in consultas:
        resultado, testes = tabela.buscar(consulta)
        total_testes += testes
        if testes > max_testes:
            max_testes = testes
        if resultado:
            resultados_consultas.append(f"{consulta} {resultado[0]}")
        else:
            resultados_consultas.append(f"{consulta} NAO ENCONTRADO")
    
    fim_consultas = time.time()
    tempo_consultas = fim_consultas - inicio_consultas
    media_testes = total_testes / len(consultas)

    # Escrever resultados
    nome_arquivo = f"experimento{tamanho_tabela}.txt"
    with open(nome_arquivo, "w") as f:
        f.write("PARTE1: ESTATISTICAS DA TABELA HASH\n")
        f.write(f"TEMPO DE CONSTRUCAO DA TABELA {tempo_construcao * 1000:.0f} MILISEGUNDOS\n")
        f.write(f"TAXA DE OCUPACAO {ocupadas}/{tabela.tamanho}\n")
        f.write(f"TAMANHO MAXIMO DE LISTA {max_lista}\n")
        f.write(f"TAMANHO MEDIO DE LISTA {media_lista:.2f}\n")
        f.write("\nPARTE 2: ESTATISTICAS DAS CONSULTAS\n")
        f.write(f"TEMPO PARA REALIZACAO DE TODAS CONSULTAS {tempo_consultas * 1000:.0f} MILISEGUNDOS\n")
        for resultado in resultados_consultas:
            f.write(f"{resultado}\n")
        f.write(f"MAXIMO NUMERO DE TESTES POR NOME ENCONTRADO {max_testes}\n")
        f.write(f"MEDIA NUMERO DE TESTES POR NOME ENCONTRADO {media_testes:.2f}\n")

# Executar experimentos
tamanhos_tabela = [997, 1999, 3989, 7993]
arquivo_dados = "players-fifa.csv"
arquivo_consultas = "consultas.csv"

for tamanho in tamanhos_tabela:
    executar_experimento(tamanho, arquivo_dados, arquivo_consultas)
