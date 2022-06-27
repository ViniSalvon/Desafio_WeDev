Desafio Python

________________

===== Introdu��o =====

O desafio foi proposto pela empresa WeDev Software, e tinha como objetivo central um MVP de uma aplica��o web.
Ainda, foi definido pela empresa que apenas a parte do back-end era requisito para cumprir esta tarefa.

Mais detalhes podem ser consultados no arquivo desafio.pdf.

_________________

===== Desenvolvimento =====

A seguir, est�o detalhados os sistemas desenvolvidos.


1) Cria��o de um sistema hier�rquico de usu�rios:

O sistema desenvolvido utilizou o sistema de usu�rios nativo do Django. Foram definidas 3 classes:

- Staff/Admin
- Professores
- Alunos

Enquanto professores e alunos foram definidos atrav�s do sistema de grupos nativo do Django, a Staff foi definida atrav�s do sistema de superusu�rios do Django.
Logo, os membros da Staff s�o os �nicos capazes de logar no ambiente administrativo do site, aonde podem cadastrar usu�rios e cursos.

Com exce��o de m�ltiplos n�meros de telefone, todos os objetivos dos campos de cadastro de usu�rios foram atingidos.
No caso de cursos, todos os campos foram atendidos, sem exce��o. Entretanto, � poss�vel para os usu�rios da Staff cadastrar alunos em cursos.


2) Sistema de login:

Foi criado um sistema de login que engloba todos os usu�rios do site.
Ao logar, alunos e professores s�o redirecionados para suas respectivas p�ginas, as quais n�o s�o acess�veis por qualquer outro grupo.

J� membros da staffs s�o redirecionados para o painel administrativo.


=== Objetivos atingidos ===

- Staffs com permiss�o de cadastrar alunos, professores e cursos na plataforma
- Cursos serem vinculados a um, e somente um, professor durante o cadastro
- Cursos admitem m�ltiplos alunos matriculados
- Cadastro de alunos e professores contemplam todos os campos requisitados, com exce��o de m�ltiplos campos para telefones.
- Cadastro de cursos contemplam todos os campos requisitados, sem exce��o. Por�m, existe a possibilidade de cadastrar alunos durante a cria��o do curso pelo Staff, com a possibilidade de ser deixado em branco.
- Cada usu�rio pode fazer login na aplica��o e s� possui acesso � sua respectiva tela.


=== Objetivos n�o atingidos ===

- Acessos a listas de alunos e cursos
- Total de alunos em um curso ministrado pelo professor
- Alunos poderem verificar e editar informa��es pessoais
- Registro de alunos em cursos
- Avalia��o de cursos por parte de alunos
- M�ltiplos telefones no cadastro de alunos e professores.

_________________

===== Conclus�es e Aprendizados =====

Durante o exerc�cio, o candidato teve um contato um pouco mais profundo com o framework Django, tendo tido um aprendizado relevante.
Alguns pontos de aprendizado podem ser listados a seguir:

- Cria��o de sites b�sicos utilizando o Django
- Cria��o de sistemas b�sicos de usu�rios
- Cria��o de sistemas de login e logout com redirecionamento
- Prote��o b�sica de acesso
- Cria��o de aplicativos web de n�vel b�sico

No mais, o autor agradece � WeDev Software pela oportunidade de participar deste processo seletivo e pelo aprendizado adquirido.

__________________

===== Projetos Futuros =====

Com calma e mais tempo, devo procurar concluir todo o projeto proposto.
Posteriormente, devo investir tempo em projetos paralelos que podem agregar ao desenvolvimento web com Django e vice-versa.

___________________

===== Refer�ncias =====

Stack Overflow
Hashtag Programa��o (https://www.youtube.com/watch?v=DNGI5aD9MJs)
Carol Padiernos (https://cpadiernos.github.io/how-to-add-fields-to-the-user-model-in-django.html)
Esther Vaati (https://betterprogramming.pub/design-your-own-login-and-registration-system-in-django-b34a2fa8334d)