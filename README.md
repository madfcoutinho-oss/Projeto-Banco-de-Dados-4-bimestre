# Projeto 01 -- CRUD de Alunos com Python e MongoDB

## Sobre o projeto

Este projeto é um sistema simples de cadastro de alunos desenvolvido em
Python, utilizando o MongoDB como banco de dados.

O programa permite realizar as operações básicas de um CRUD (Create,
Read, Update e Delete), utilizando a matrícula do aluno como
identificador.

Além dos dados do aluno, o sistema registra automaticamente a data em
que a matrícula foi cadastrada. Essa informação fica armazenada no
MongoDB, mas não é exibida na listagem do terminal.

## Funcionalidades

O sistema apresenta um menu com as seguintes opções:

1.  **Cadastrar:** registra um aluno com matrícula, nome e curso.
2.  **Listar:** exibe os alunos cadastrados, permitindo filtrar por
    curso ou visualizar todos.
3.  **Alterar:** atualiza o curso de um aluno a partir da matrícula.
4.  **Excluir:** remove um aluno a partir da matrícula.
5.  **Sair:** encerra o programa.

## Dados armazenados

Cada aluno é salvo em uma coleção do MongoDB chamada `alunos_p01`, com
os seguintes campos:

  Campo              Descrição
  ------------------ ------------------------------------------------
  `matricula`        Matrícula do aluno, com 5 caracteres numéricos
  `nome`             Nome do aluno
  `curso`            Curso em que o aluno está matriculado
  `data_matricula`   Data e horário em que o cadastro foi realizado

A matrícula possui um índice único no MongoDB para impedir que dois
alunos sejam cadastrados com a mesma matrícula.

A data é registrada automaticamente usando `datetime.now()`. Ela
permanece com o valor original quando o curso do aluno é atualizado.

## Tecnologias e bibliotecas

-   **Python:** linguagem utilizada no desenvolvimento.
-   **MongoDB:** banco de dados NoSQL utilizado para armazenar os
    alunos.
-   **PyMongo:** biblioteca responsável pela comunicação entre Python e
    MongoDB.
-   **python-dotenv:** biblioteca utilizada para carregar variáveis de
    ambiente de um arquivo `.env`.
-   **datetime:** biblioteca padrão do Python utilizada para registrar a
    data e o horário do cadastro.

## Organização dos arquivos

Uma possível organização do projeto é:

``` text
Projeto01/
├── conexao.py
├── main.py
├── .env
└── README.md
```

-   `conexao.py`: realiza a conexão com o MongoDB.
-   `main.py`: contém o menu e as operações do CRUD.
-   `.env`: armazena a variável de conexão com o banco de dados.
-   `README.md`: documentação do projeto.

Os nomes dos arquivos podem ser ajustados conforme a organização
utilizada no projeto.

## Instalação das dependências

Com o Python instalado, abra o terminal na pasta do projeto e execute:

``` bash
pip install pymongo python-dotenv
```

## Configuração da conexão

Crie um arquivo chamado `.env` na pasta do projeto e configure a
variável `MONGO_URI` com a string de conexão fornecida pelo MongoDB
Atlas:

``` env
MONGO_URI=sua_string_de_conexao
```

Substitua `sua_string_de_conexao` pela URI do seu próprio banco de
dados.

**Importante:** não compartilhe sua URI de conexão, pois ela pode conter
credenciais de acesso ao banco. O arquivo `.env` não deve ser enviado
publicamente.

## Como executar

1.  Verifique se o arquivo `.env` está configurado corretamente.
2.  Confira se o arquivo `conexao.py` consegue estabelecer a conexão com
    o MongoDB.
3.  Abra o terminal na pasta do projeto.
4.  Execute o arquivo principal. Por exemplo:

``` bash
python main.py
```

5.  Utilize as opções apresentadas no menu para cadastrar, listar,
    alterar ou excluir alunos.

## Observações

-   A matrícula deve possuir exatamente 5 caracteres numéricos.
-   Não é permitido cadastrar duas matrículas iguais.
-   Os campos de matrícula, nome e curso são obrigatórios.
-   A data de matrícula é registrada automaticamente no momento do
    cadastro.
-   A data original não é alterada quando o curso é atualizado.
-   A listagem pode ocultar os campos `_id` e `data_matricula`, mantendo
    essas informações armazenadas no banco.

## Autor

Projeto desenvolvido como atividade prática de programação, utilizando
Python e MongoDB.
