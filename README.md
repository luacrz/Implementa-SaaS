Descrição da solução:
A primeira solução usa QR Code e a segunda usa perguntas durante a aula.

A solução de QR Code usa a biblioteca qrcode para gerar um código QR exclusivo para cada aula. O código QR é exibido na tela durante a aula. Quando um aluno escaneia o código com seu dispositivo móvel, o sistema registra sua presença automaticamente.

A solução de perguntas durante a aula permite que o professor crie perguntas exclusivas que só podem ser respondidas por alunos presentes na aula. Durante a aula, em momentos aleatórios, uma pergunta é exibida na tela dos alunos. Os alunos têm um tempo limitado para responder à pergunta, quando um aluno envia sua resposta, o sistema verifica se a resposta está correta e, se estiver, registra a presença do aluno. Se a resposta estiver incorreta, o sistema informa ao aluno que a presença não foi registrada e permite que ele tente novamente com a próxima pergunta.

Ambas as soluções exigem que o aluno esteja autenticado e autorizado a registrar sua presença. Este código usa requisições POST para garantir que as informações enviadas pelo usuário sejam seguras.

Instruções para executar o projeto:
Baixar o código da aplicação, abra um terminal na pasta onde salvou o código e execute o seguinte comando: python app.py. A aplicação será iniciada e você poderá acessar o formulário de login no endereço que será indicado. Insira um nome de usuário e senha para fazer o login e veja a mensagem de sucesso ou de erro.