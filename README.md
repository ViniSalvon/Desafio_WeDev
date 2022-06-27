<h1>Desafio Python</h1>

________________

<h3>Introdução</h3>

O desafio foi proposto pela empresa WeDev Software, e tinha como objetivo central um MVP de uma aplicação web.
Ainda, foi definido pela empresa que apenas a parte do back-end era requisito para cumprir esta tarefa.

Mais detalhes podem ser consultados no arquivo desafio.pdf.

_________________

<h3>Desenvolvimento</h3>

A seguir, estão detalhados os sistemas desenvolvidos.


<h4>1) Criação de um sistema hierárquico de usuários:</h4>

O sistema desenvolvido utilizou o sistema de usuários nativo do Django. Foram definidas 3 classes:

- Staff/Admin
- Professores
- Alunos

Enquanto professores e alunos foram definidos através do sistema de grupos nativo do Django, a Staff foi definida através do sistema de superusuários do Django.
Logo, os membros da Staff são os únicos capazes de logar no ambiente administrativo do site, aonde podem cadastrar usuários e cursos.

Com exceção de múltiplos números de telefone, todos os objetivos dos campos de cadastro de usuários foram atingidos.
No caso de cursos, todos os campos foram atendidos, sem exceção. Entretanto, é possível para os usuários da Staff cadastrar alunos em cursos.


<h4>2) Sistema de login:</h4>

Foi criado um sistema de login que engloba todos os usuários do site.
Ao logar, alunos e professores são redirecionados para suas respectivas páginas, as quais não são acessíveis por qualquer outro grupo.

Já membros da staffs são redirecionados para o painel administrativo.


<h4>Objetivos atingidos</h4>

- Staffs com permissão de cadastrar alunos, professores e cursos na plataforma
- Cursos serem vinculados a um, e somente um, professor durante o cadastro
- Cursos admitem múltiplos alunos matriculados
- Cadastro de alunos e professores contemplam todos os campos requisitados, com exceção de múltiplos campos para telefones.
- Cadastro de cursos contemplam todos os campos requisitados, sem exceção. Porém, existe a possibilidade de cadastrar alunos durante a criação do curso pelo Staff, com a possibilidade de ser deixado em branco.
- Cada usuário pode fazer login na aplicação e só possui acesso à sua respectiva tela.


<h4>Objetivos não atingidos</h4>

- Acessos a listas de alunos e cursos
- Total de alunos em um curso ministrado pelo professor
- Alunos poderem verificar e editar informações pessoais
- Registro de alunos em cursos
- Avaliação de cursos por parte de alunos
- Múltiplos telefones no cadastro de alunos e professores.

_________________

<h3>Conclusões e Aprendizados</h3>

Durante o exercício, o candidato teve um contato um pouco mais profundo com o framework Django, tendo tido um aprendizado relevante.
Alguns pontos de aprendizado podem ser listados a seguir:

- Criação de sites básicos utilizando o Django
- Criação de sistemas básicos de usuários
- Criação de sistemas de login e logout com redirecionamento
- Proteção básica de acesso
- Criação de aplicativos web de nível básico

No mais, o autor agradece à WeDev Software pela oportunidade de participar deste processo seletivo e pelo aprendizado adquirido.

__________________

<h3>Projetos Futuros</h3>

Com calma e mais tempo, devo procurar concluir todo o projeto proposto.
Posteriormente, devo investir tempo em projetos paralelos que podem agregar ao desenvolvimento web com Django e vice-versa.

___________________

<h3>Referências</h3>

- Stack Overflow
- Hashtag Programação (https://www.youtube.com/watch?v=DNGI5aD9MJs)
- Carol Padiernos (https://cpadiernos.github.io/how-to-add-fields-to-the-user-model-in-django.html)
- Esther Vaati (https://betterprogramming.pub/design-your-own-login-and-registration-system-in-django-b34a2fa8334d)
