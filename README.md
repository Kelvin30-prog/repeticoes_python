  🐍 Meus Projetos de Python com while
O laço de repetição while é uma das ferramentas mais poderosas e fundamentais em Python, permitindo que um bloco de código se repita enquanto uma determinada condição for verdadeira.


  1. 🔢 Validador de Intervalo de Números.
O primeiro projeto utiliza o while para garantir que a entrada do usuário esteja dentro de um intervalo específico.
Objetivo: Permitir que o usuário digite números de 1 a 99.
Mecanismo while: O laço de repetição continua a executar enquanto o número digitado estiver entre 1 e 99.
Condição de Saída: Assim que o usuário digitar um número menor que 1 ou maior que 99, a condição do while se torna falsa e o sistema é encerrado. Este projeto demonstra como o while é útil para validação de dados e controle de fluxo.

  2. 📝 Coletor de Palavras com Encerramento por Comando.
O segundo projeto foca em coletar dados até que um comando específico seja dado.
Objetivo: Capturar palavras aleatórias do usuário.
Mecanismo while: O laço é configurado para rodar infinitamente (ou com uma condição que sempre será verdadeira inicialmente).
Condição de Saída: O sistema verifica a cada loop se a palavra digitada é 'sair'. Se for, o sistema interrompe a execução do laço e finalizar o programa.

  3. 🔁 Repetição de Operação Controlada por Confirmação.
Este projeto clássico permite replicar o cenário comum de "deseja realizar outra operação?".
Objetivo: Repetir um bloco de código (simulando uma operação qualquer) com base na escolha do usuário.
Mecanismo while: Uma variável de controle (geralmente uma flag booleana ou uma string) é verificada no início do laço.
Condição de Continuidade/Saída:
Se o usuário digitar 'sim', a variável de controle é mantida (ou redefinida) para permitir que o while continue para a próxima iteração.
Se o usuário digitar 'não', a variável de controle é modificada (por exemplo, de 'sim' para 'não') encerrando o laço.

  4. ⚙️ Menu Interativo com Saída por Opção Inválida.
O quarto e último projeto aplica o while na construção de um menu simples.
Objetivo: Apresentar cinco opções ao usuário e executar a ação correspondente.
Mecanismo while: O loop é mantido ativo para que o menu seja exibido e o usuário possa fazer sua escolha repetidamente.
Lógica e Saída:
Se o usuário escolhesse uma das cinco opções existentes, a escolha é exibida na tela e o loop continua, permitindo uma nova escolha.
Se o usuário selecionar uma opção não existente (ou inválida) o while é interrompido, garantindo que o sistema seja encerrado de forma limpa ao detectar uma entrada inesperada.


Esses exercícios práticos são cruciais para compreender como o while não serve apenas para repetições simples, mas é a espinha dorsal para a criação de menus interativos, validadores de entrada e sistemas de repetição controlada em Python.
