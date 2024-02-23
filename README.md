# Analise_e_Tratamento_de_Dados_de_Saude
Integrando Python, HTML e JavaScript para a Visualização Geográfica dos Dados de Saúde do SIGA Brasil 2018-2022

Este repositório contém o projeto desenvolvido para a disciplina de Contabilidade de Custos e Gerencial, ministrada pelo professor Marcelo Jota Gomes. O projeto visa tratar e analisar dados financeiros relacionados à saúde pública no Brasil, contidos no arquivo “SIGA Brasil_2018-2022_Valores repassados_Estados_Saúde (Mod. Aplic.).xlsx”.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para processamento de dados.
- **HTML**: Estruturação das páginas web.
- **CSS**: Estilização das páginas web.
- **JavaScript**: Funcionalidades interativas no cliente.

## Bibliotecas Python

- `os`: Fornece uma maneira portátil de usar funcionalidades dependentes do sistema operacional, e a manipulação de arquivos e diretórios.
- `webbrowser`: Permite exibir documentos web aos usuários.
- `pandas`: Oferece estruturas de dados e ferramentas de análise de dados poderosas e fáceis de usar.

## Especificações do Projeto

O projeto envolve o processamento do arquivo "SIGA Brasil_2018-2022_Valores repassados_Estados_Saúde (Mod. Aplic.).xlsx", que contém dados financeiros detalhados em 22 colunas. As colunas finais são de particular importância, pois incluem os valores EMPENHADO, LIQUIDADO, PAGO, Restos a Pagar Pago (RP Pago) e Despesa Executada.

### Código FUNCIONAL

A sexta coluna, denominada FUNCIONAL, contém um código de 17 dígitos representando a função, subfunção, programa, ação e a Unidade da Federação. Por exemplo, o código `10.302.2015.20B0.0068` refere-se à construção de um CAPS I em Rio Branco - AC.

### Extração de Dados

A equipe desenvolveu um algoritmo para extrair e analisar os dados mensais da planilha, que contém 264.532 linhas de informações do período de 2018 a 2022.

## Colaboradores

Esse projeto foi desenvolvido por:
Alberis Silva
Arlen Filho
Gustavo Diego
Hyan Lucas
