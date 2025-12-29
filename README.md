# Create Python Project

Este projeto é um utilitário interativo para criar rapidamente projetos Django, Django REST Framework ou FastAPI já configurados com o gerenciador de pacotes [uv](https://github.com/astral-sh/uv).

## Como executar

No terminal, execute o comando conforme seu sistema operacional:

- **Windows:**
  ```
  python create-python-project.py
  ```
- **Linux/macOS:**
  ```
  python3 create-python-project.py
  ```

Ou, em qualquer sistema, usando uv:

```
uv run create-python-project.py
```

## Opções disponíveis

Ao rodar o script, você poderá escolher:

- **1 - Django**: Cria um projeto Django básico, já incluindo a seguinte dependência:

  - **django**: Framework principal para desenvolvimento web com Python.

- **2 - Django REST Framework**: Cria um projeto Django para APIs REST, já incluindo as seguintes dependências:

  - **django**: Framework principal.
  - **djangorestframework**: Toolkit para criação de APIs REST.
  - **psycopg2-binary**: Driver para uso do PostgreSQL.
  - **python-decouple**: Gerenciamento de configurações sensíveis e variáveis de ambiente.
  - **django-cors-headers**: Suporte a CORS (Cross-Origin Resource Sharing).
  - **dj-database-url**: Facilita a configuração do banco de dados via URL.
  - **drf-spectacular**: Geração automática de documentação OpenAPI/Swagger para DRF.

  Essas dependências tornam o projeto pronto para desenvolvimento de APIs REST modernas e documentadas.

- **3 - FastAPI**: Cria um projeto FastAPI básico, já incluindo as seguintes dependências:

  - **fastapi**: Framework moderno e rápido para construção de APIs com Python.
  - **uvicorn**: Servidor ASGI leve e rápido, recomendado para rodar aplicações FastAPI.

  O projeto já vem com um endpoint inicial de exemplo e pronto para desenvolvimento de APIs modernas.

Você também será solicitado a informar o nome do projeto.

## Sobre o arquivo `dev.py`

Após a criação do projeto, um arquivo `dev.py` será gerado dentro da pasta do projeto. Ele serve para facilitar a execução do servidor de desenvolvimento:

- Para projetos Django ou Django REST Framework: executa `uv run python manage.py runserver`
- Para projetos FastAPI: executa `uv run uvicorn main:app --reload`

Basta rodar:

```
uv run dev.py
```

Assim, o servidor de desenvolvimento será iniciado rapidamente.

---

Este utilitário automatiza a configuração inicial de projetos Django, Django REST Framework e FastAPI, tornando o processo mais ágil e padronizado.
