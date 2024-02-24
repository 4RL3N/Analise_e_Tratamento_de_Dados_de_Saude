# Analise_e_Tratamento_de_Dados_de_Saude
Integrando Python, HTML e JavaScript para a Visualização Geográfica dos Dados de Saúde do SIGA Brasil 2018-2022

Este repositório contém o projeto desenvolvido para a disciplina de Contabilidade de Custos e Gerencial, ministrada pelo professor Marcelo Jota Gomes. O projeto visa tratar e analisar dados financeiros relacionados à saúde pública no Brasil, contidos no arquivo “SIGA Brasil_2018-2022_Valores repassados_Estados_Saúde (Mod. Aplic.).xlsx”.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para processamento de dados.
- **HTML**: Estruturação das páginas web.
- **CSS**: Estilização das páginas web.
- **JavaScript**: Funcionalidades interativas no cliente.

## Bibliotecas Python utilizadas

- `os`: Fornece uma maneira portátil de usar funcionalidades dependentes do sistema operacional, e a manipulação de arquivos e diretórios.

- `webbrowser`: Permite exibir documentos web aos usuários.

- `pandas`: Oferece estruturas de dados e ferramentas de análise de dados poderosas e fáceis de usar.

- `GeoPandas`: É um projeto para adicionar suporte para dados geográficos aos objetos pandas. O objetivo do GeoPandas é facilitar o trabalho com dados geoespaciais em Python. Ele combina as capacidades de pandas e shapely, fornecendo operações geoespaciais em pandas e uma interface de alto nível para várias geometrias para shapely.

- `Matplotlib`: É uma biblioteca de plotagem, ela fornece uma API orientada a objetos para incorporar gráficos em aplicativos usando kits de ferramentas de interface gráfica de usuário de uso geral, como Tkinter, wxPython, Qt ou GTK.

- `Geobr`: É um pacote computacional para baixar conjuntos de dados espaciais oficiais do Brasil. O pacote inclui uma ampla gama de dados geoespaciais no formato geopackage (como shapefiles, mas melhor), disponíveis em várias escalas geográficas e para vários anos com atributos harmonizados, projeção e topologia.

- `Contextily`: É um pequeno pacote Python 3 para recuperar mapas de tiles da internet. Ele pode adicionar esses tiles como mapa base para figuras matplotlib ou escrever mapas de tiles em disco em arquivos raster geoespaciais.

- `Rasterio`: É um módulo altamente útil para processamento de raster que pode se usar para ler e escrever vários formatos de raster diferentes em Python. Rasterio é baseado em GDAL e Python registra automaticamente todos os drivers GDAL conhecidos para leitura de formatos suportados ao importar o módulo.

- `Mapclassify`: Implementa uma família de esquemas de classificação para mapas de coropletas. Seu foco está na determinação do número de classes e na atribuição de observações a essas classes.

- `Pygeos`: É uma biblioteca C/Python com funções de geometria vetorizadas. As operações de geometria são feitas na biblioteca de geometria de código aberto GEOS. Pygeos envolve essas operações em ufuncs NumPy, proporcionando uma melhoria de desempenho ao operar em arrays de geometrias.

- `Rtree`: É um wrapper Python ctypes de libspatialindex que fornece uma série de recursos avançados de indexação espacial para o usuário Python.

- `Mplleaflet`: É uma biblioteca Python que converte um plot matplotlib em uma página da web contendo um mapa Leaflet panorâmico e zoomável. Ele também pode incorporar o mapa Leaflet em um notebook IPython.

- `Folium`: É uma biblioteca de visualização de dados poderosa em Python que foi construída principalmente para ajudar as pessoas a visualizar dados geoespaciais. Com Folium, é possível criar um mapa de qualquer local no mundo.

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
