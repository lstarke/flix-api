# API de filmes

## Descrição do Projeto

Este projeto é uma API RESTful desenvolvida com **Django** e **Django REST Framework** como parte de um estudo prático. A API permite o gerenciamento de um cadastro de filmes, incluindo funcionalidades de CRUD (Create, Read, Update, Delete) para as seguintes entidades:

- **Movies**: Informações sobre filmes, como título, ano de lançamento, gênero, etc.
- **Actors**: Cadastro de atores associados aos filmes.
- **Genres**: Categorias de filmes (ex.: Ação, Drama, Comédia).
- **Reviews**: Avaliações e comentários sobre os filmes.

## Pré-requisitos

Antes de instalar e executar o projeto, certifique-se de ter os seguintes itens instalados:

- **Python** (versão 3.8 ou superior)
- **pip** (gerenciador de pacotes do Python)
- **Git** (para clonar o repositório)
- Um banco de dados (o projeto usa SQLite por padrão, mas você pode configurar outro, como PostgreSQL, se desejar)

## Instruções de Instalação

Siga os passos abaixo para configurar o projeto localmente:

1. **Clone o repositório**  
    Clone o repositório para sua máquina local usando o comando: https://github.com/lstarke/flix-api.git

2. **Crie e ative um ambiente virtual**

    Crie um ambiente virtual para isolar as dependências do projeto: 

        python -m venv venv

    Ative o ambiente virtual (Windows):
        
        venv\Scripts\activate.bat

    Ative o ambiente virtual (Linux/MacOS):

        source venv/bin/activate

3. **Instale as dependências**

    Com o ambiente virtual ativado, instale as dependências listadas no arquivo `requirements.txt`:

        pip install -r requirements.txt

4. **Configure o banco de dados**

    Execute as migrações para criar o banco de dados (SQLite é usado por padrão):

        python manage.py makemigrations
        python manage.py migrate

5. **Crie um superusuário (opcional)**
    
    Para acessar o painel de administração do Django, crie um superusuário:

        python manage.py createsuperuser

6. **Inicie o servidor de desenvolvimento**  
    
    Inicie o servidor local do Django:

        python manage.py runserver

## Estrutura do Projeto

- **`models.py`**: Define os modelos de dados para Filmes, Atores, Gêneros e Reviews.
- **`serializers.py`**: Contém as classes de serialização para converter dados em JSON.
- **`views.py`**: Implementa as views da API usando ViewSets ou Generic Views.
- **`urls.py`**: Configura as rotas dos endpoints da API.
- **`settings.py`**: Configurações do Django, incluindo banco de dados e aplicativos instalados.

## Contribuições

Este é um projeto de estudo, mas sugestões e melhorias são bem-vindas! Sinta-se à vontade para abrir uma **issue** ou enviar um **pull request** no repositório.


