# ProManage

**ProManage** é um sistema de gerenciamento de projetos e tarefas inspirado em Trello. O projeto foi desenvolvido com o objetivo de proporcionar uma interface intuitiva para controle de tarefas e acompanhamento de status por meio de um layout de estilo Kanban. O sistema é simples, mas eficiente, oferecendo funcionalidades essenciais para o gerenciamento de projetos de pequeno a médio porte.

## Funcionalidades
- Criação e gerenciamento de múltiplos projetos.
- Sistema de tarefas visual (Kanban), com status customizáveis como "To-Do", "In Progress", "Review" e "Done".
- Autenticação de usuários com tela de cadastro e login.
- Edição e exclusão de tarefas, mantendo os usuários atualizados sobre o progresso.
- Interface responsiva e moderna, utilizando Bootstrap 4.
- Backend desenvolvido com Django para garantir segurança e eficiência na gestão dos dados.

## Requisitos

- **Python 3.10+**
- **Poetry** (para gerenciamento de dependências)

## Configuração Inicial

### Passo 1: Clonar o repositório

Clone este repositório para sua máquina local:

```bash
git clone https://github.com/allanrodigo/ProManage.git

cd promanage
```

### Passo 2: Instalar dependências com Poetry
O ProManage utiliza o **Poetry** para gerenciamento de dependências. Certifique-se de que o Poetry está instalado:

Instale o Poetry (caso não esteja instalado):
```bash
pip install poetry
```

Instale as dependências:
```bash
poetry install
```

Ative o ambiente virtual (caso não ative automaticamente):
```bash
poetry shell
```

### Passo 3: Configurar o banco de dados

O sistema utiliza o banco de dados SQLite por padrão. Para inicializar o banco de dados, rode as migrações:

```bash
cd .\ProManage\
```

```bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```
### Passo 4: Criar um superusuário (opcional)
Para acessar o painel de administração do Django e gerenciar usuários, você pode criar um superusuário:

```bash
poetry run python manage.py createsuperuser
```

### Passo 5: Iniciar o servidor de desenvolvimento

Agora você pode iniciar o servidor de desenvolvimento:

```bash
poetry run python manage.py runserver
```

Acesse o sistema no seu navegador em: http://127.0.0.1:8000/.


# Como Contribuir
1. Faça um fork do projeto.
2. Crie uma nova branch para sua feature: `git checkout -b minha-nova-feature`.
3. Faça o commit das suas alterações: `git commit -m 'Adicionando nova feature'`.
4. Faça um push para a branch: `git push origin minha-nova-feature`.
5. Envie um pull request para revisão.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).


### Resumo do README

1. **Descrição do Projeto**: Explica brevemente o que é o ProManage e suas principais funcionalidades.
2. **Requisitos**: Detalha as dependências do projeto, como Python e Poetry.
3. **Configuração Inicial**: Explica os passos para clonar o projeto, instalar dependências, configurar o banco de dados e rodar o servidor.
4. **Como Contribuir**: Oferece diretrizes para que outros desenvolvedores contribuam com o projeto.

Se precisar de mais informações ou ajustes, estou à disposição!
