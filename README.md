Este é um projeto de web scraping desenvolvido em Python que realiza a coleta de dados de produtos de guitarra de dois sites populares: musicalle.com.br e megasom.com.br. O objetivo é extrair informações como título, preço e imagem dos produtos e salvar os dados em formato CSV para posterior análise.

Funcionalidades
Utiliza a biblioteca requests_html para fazer o scraping das páginas web e extrair informações relevantes dos produtos usando seletores CSS.
Implementa tratamento de erros para lidar com exceções que possam ocorrer durante o processo de scraping.
Registra eventos importantes e detalhes do processo de scraping em um arquivo de log (scraping.log).
Apresenta logs em tempo real no console para feedback imediato.
Design modular com módulos separados para o scraping (scrapers.py), manipulação de CSV (csv_utils.py) e o script principal (main.py).
