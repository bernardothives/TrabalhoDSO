## ClimaCO
**um sistema orientado a objetos para consulta do clima atual e previsões, via terminal**

como trabalho do curso de Sistemas de Informação UFSC, eu Gustavo Gomes e o Bernardo Thives estamos desenvolvendo em python um Weather App, no terminal.

## Entidades:
- Usuário: Tem como atributos: nome de usuário e CPF, não é possível cadastrar um usuário com cpf repetidos, e o cpf tem que ser válido.
- Localização: Tem como atributos: cidade, estado e país, não deve ser possivel cadastrar duas localizações com a mesma cidade.
- Notificação: Tem um tipo, um status e um usuário, são 3 tipos possíveis: banner, central e tela de bloqueio. Como status deve ser aceito somente sim/ativo(um valor booleano True) ou nao/inativo para False.
- Clima Atual: Recebe da abstrata um usuário e uma localização, além disso tem um horário e uma data.
- Clima Previsão: Também recebe da abstrata um usuário e uma localização, tem data e horário
- Dados Climáticos: É essa entidade que geramos com random dados de clima como temperatura, humidade, velocidade do vento, volume de chuva, visibilidade e sensação térmica.

## Controladores:
- Controlador do Usuário: faz o CRUD, instancia a tela do usuário, nessa classe tem métodos de tratamento de erros, também verificador de cpf válidos e buscar usuários por cpf.
- Controlador da Localização: faz o CRUD, instancia a tela da localização, trata erros como adição de localização com a mesma cidade, faz a busca de localização por cidade.
- Controlador da Notificação: faz o CRUD, instancia a tela da notificação, verifica se os inputs foram válidos e busca notificação por tipo, também não permite duas notificações com o mesmo tipo.
- Controlador do Alerta: não faz o CRUD pois não existe a entidade alerta mas intancia a tela do alerta, realiza a logica de quando dado do clima está extremo e envia para a tela mostrar ao usuário.
- Sistema: aqui é onde instanciamos todos os controladores, getters e setters dos controladores e a opção de encerrar o sistema
- Controlador do Clima Atual: intancia a tela do clima atual, envia para a tela mostrar os dados climáticos, registra no log de uso o usuário, a cidade e a hora. Apaga todo o histórico de logs ou um log em específico procurando por cpf, além disso também possui uma lista dos dados climáticos buscados e tem um método que retorna localização com maior temperatura apresentada entre outras funções desse tipo.
- Controlador do Clima Previsão: diferente do clima atual, intancia além da tela o controlador do alerta também possui logs e os mesmos métodos de busca detalhada do clima atual.

## Telas:
- Tela do Usuário: pega e mostra os dados além de selecionar usuário por cpf, as opções da tela são: incluir, alterar, listar, remover e retornar para a ultima tela.
- Tela da Localização: pega e mostra os dados além de selecionar localização por cidade, as opções da tela são: incluir, alterar, listar, remover e retornar para a última tela.
- Tela da notificação: pega dados podendo pegar especificamente, mostra dados, seleciona por tipo além de ter um método para ler boolean para facilitar a verificação do input.
- Tela do Sistema: tela principal do programa, mostra o nome do programa e as opções: usuário, localização, clima atual, previsão do clima, notificação e encerrar sistema.
- Tela do Alerta: apresenta a opção de voltar e ver alertas, além de um metodo seleciona cidade.
- Tela do Clima Atual: pega dados, mostra dados do clima e também mostra dados dos logs, além de selecionar por cpf, as opções da tela são: ver dados climáticos, ver logs, apagar todos os logs, apagar log específico e voltar para tela do sistema.
- Tela do Clima Previsão: pega dados, mostra clima e mostra logs, pode selecionar por cpf e as opções são: ver dados climáticos, ver logs, apagar todos os logs, apagar log especifico, ir para tela dos alertas e voltar para tela do sistema.

## Divisão das Tarefas:
Primeiramente decidimos dividir assim: Eu(Gustavo) fiz a parte do Usuário, Localização e Notificação e meu parceiro(Bernardo) ficou encarregado de ambos os Climas, Alerta e o Sistema. porem em diversos momentos eu ajudei em classes dele e ele me ajudou em classes que seriam minha responsabilidade, fizemos majoritariamente assíncrono mas também algumas ligações para alinhar as demandas.
