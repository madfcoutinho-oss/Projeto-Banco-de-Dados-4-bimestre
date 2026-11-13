"""Projeto 01: CRUD de alunos por matricula."""
from pymongo.errors import DuplicateKeyError
from conexao import banco
from datetime import datetime

alunos = banco['alunos_p01']
alunos.create_index('matricula', unique=True)
tamanho = 0
data_matricula = datetime.now().strftime('%d/%m/%Y')

while True:
    print('\n[1] Cadastrar [2] Listar [3] Alterar [4] Excluir [0] Sair')
    opcao = input('Opção: ').strip()
    if opcao == '1':
        while tamanho != 5:
            matricula = input('\nMatrícula: ').strip()
            tamanho = len(matricula)
            if tamanho != 5:
                print("Matricula precisa ter 5 dígitos!")
        nome = input('Nome: ').strip()
        curso = input('Curso: ').strip()
        if not all([matricula, nome, curso]):
            print('Preencha todos os campos.')
            continue
        try:
            alunos.insert_one({'matricula': matricula, 'nome': nome, 'curso': curso, 'data matricula': data_matricula})
            print('Aluno cadastrado!')
        except DuplicateKeyError:
            print('Matrícula já cadastrada.')
    elif opcao == '2':
        print("\n[1] Administração [2] Analises Clínicas [3] Eletrônica [4] Informática [5] Publicidade [6] Química [7] Todos")
        ncurso = input('Digite o curso que queira achar: ').strip()
        if ncurso == '1':
            for aluno in alunos.find({'curso': 'Administração'}, {'_id': 0}).sort('nome', 1):
                print(aluno)
        elif ncurso == '2':
                    for aluno in alunos.find({'curso': 'Analises Clínicas'}, {'_id': 0}).sort('nome', 1):
                        print(aluno)
        elif ncurso == '3':
            for aluno in alunos.find({'curso': 'Eletrônica'}, {'_id': 0}).sort('nome', 1):
                print(aluno)
        elif ncurso == '4':
            for aluno in alunos.find({'curso': 'Informática'}, {'_id': 0}).sort('nome', 1):
                print(aluno)
        elif ncurso == '5':
            for aluno in alunos.find({'curso': 'Publicidade'}, {'_id': 0}).sort('nome', 1):
                print(aluno)
        elif ncurso == '6':
            for aluno in alunos.find({'curso': 'Química'}, {'_id': 0}).sort('nome', 1):
                print(aluno)
        elif ncurso == '7':
            for aluno in alunos.find({}, {'_id': 0}).sort('nome', 1):
                print(aluno)
        else:
            print("Opção inválida.")
    elif opcao == '3':
        matricula = input('\nMatrícula: ').strip()
        novo_curso = input('Novo curso: ').strip()
        if novo_curso:
            r = alunos.update_one({'matricula': matricula}, {'$set': {'curso': novo_curso}})
            print('Atualizado!' if r.matched_count else 'Aluno não encontrado.')
    elif opcao == '4':
        matricula = input('\nMatrícula: ').strip()
        r = alunos.delete_one({'matricula': matricula})
        print('Excluído!' if r.deleted_count else 'Aluno não encontrado.')
    elif opcao == '0':
        break
    else:
        print('Opção inválida.')