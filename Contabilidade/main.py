import os
import pandas as pd
from get_files import caminho

class ObjetoAno:
    def __init__(self, ano):
        self.ano = ano
        self.qtd_linhas = 0
        self.soma_empenhado = 0
        self.soma_liquidado = 0
        self.soma_pago = 0
        self.soma_rp_pago = 0
        self.soma_despesa_executada = 0
        self.media_empenhado = 0
        self.max_empenhado = 0

def processar_arquivos_na_pasta(pasta_entrada):
    # Dicionário para armazenar objetos ano por estado
    estados = {}

    # Listar todos os arquivos XLSX na pasta de entrada
    arquivos_xlsx = [arquivo for arquivo in os.listdir(pasta_entrada) if arquivo.endswith(".xlsx")]

    for arquivo in arquivos_xlsx:
        # Caminho completo para o arquivo de entrada
        caminho_entrada = os.path.join(pasta_entrada, arquivo)

        # Carregar a planilha
        df = pd.read_excel(caminho_entrada)

        # Iterar sobre as linhas do DataFrame
        for _, linha in df.iterrows():
            uf = linha['UF']
            regiao = linha['Região']
            ano = int(linha['Ano'])

            # Caso o estado ainda não foi encontrado, criar um novo objeto para ele
            if uf not in estados:
                estados[uf] = {'região': regiao, 'anos': {}}

            # Se o ano ainda não foi encontrado, criar um novo objeto para ele
            if ano not in estados[uf]['anos']:
                estados[uf]['anos'][ano] = ObjetoAno(ano)

            # Atualizar os atributos do objeto ano
            obj_ano = estados[uf]['anos'][ano]
            obj_ano.qtd_linhas += 1
            obj_ano.soma_empenhado += linha['Empenhado']
            obj_ano.soma_liquidado += linha['Liquidado']
            obj_ano.soma_pago += linha['Pago']
            obj_ano.soma_rp_pago += linha['RP Pago']
            obj_ano.soma_despesa_executada += linha['Despesa Executada']

            # Calcular média e máximo do empenhado
            obj_ano.media_empenhado = obj_ano.soma_empenhado / obj_ano.qtd_linhas
            obj_ano.max_empenhado = max(obj_ano.max_empenhado, linha['Empenhado'])

    return estados

# Carrega o caminho da pasta "dados" e processa
estados = processar_arquivos_na_pasta(caminho)

# Exemplo de como acessar os resultados
for uf, info_uf in estados.items():
    print(f"Estado: {uf}, Região: {info_uf['região']}")
    for ano, obj_ano in info_uf['anos'].items():
        print(f"  Ano: {ano}")
        print(f"    Qtd Ações: {obj_ano.qtd_linhas}")
        print(f"    Soma Empenhado: {obj_ano.soma_empenhado}")
        print(f"    Soma Liquidado: {obj_ano.soma_liquidado}")
        print(f"    Soma Pago: {obj_ano.soma_pago}")
        print(f"    Soma RP Pago: {obj_ano.soma_rp_pago}")
        print(f"    Soma Despesa Executada: {obj_ano.soma_despesa_executada}")
        print(f"    Média Empenhado: {obj_ano.media_empenhado}")
        print(f"    Máximo Empenhado: {obj_ano.max_empenhado}")
        print()
