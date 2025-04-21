# Melhores ações

Este repositório contém ferramentas para auxiliar a análise fundamentalista de ações da bolsa de valores brasileira.

## Funcionamento

O arquivo main.py usa o módulo de automatização de testes em páginas web selenium. Esse programa buscará indicadores de todas as empresas listadas no site investidor10 e os registrará no arquivo stocks_data.csv.

A partir deste arquivo, é possível criar diferentes estratégias de investimento com base nos indicadores obtidos. Tais estratégias (contidas nos arquivos .py cujos nomes começam com "analyze") leem o arquivo csv resultante da execução de main.py.

Como o programa deve acessar diversas páginas web para obter todos os indicadores de todas as empresas, a execução é consideravelmente demorada.