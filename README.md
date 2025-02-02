# Sistema de Autoatendimento

Este projeto implementa um sistema de autoatendimento para estabelecimentos, permitindo que clientes façam pedidos, a cozinha acompanhe a preparação e a administração gerencie produtos e pedidos.

## 🚀 Tecnologias Utilizadas
- Python (Flask)
- PostgreSQL
- Docker e Docker Compose
- Postman (para testes de API)

## 📌 Requisitos
Antes de iniciar, certifique-se de ter instalado:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Postman](https://www.postman.com/downloads/) (opcional, para testar as APIs)

## 🔧 Inicialização do Projeto

### 1️⃣ Clonar o Repositório
```sh
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

### 2️⃣ Construir e Executar os Containers
```sh
docker-compose up --build
```
Isso irá iniciar o backend e o banco de dados.

### 3️⃣ Testar as APIs
Importe o arquivo `api_tests.json` no Postman e siga a ordem das chamadas:
1. **Identificação do Cliente** (`POST /identificacao`)
2. **Obter Lista de Produtos** (`GET /produtos`)
3. **Criar um Pedido** (`POST /pedido`)
4. **Consultar Status do Pedido** (`GET /status/{pedido_id}`)
5. **Atualizar Status do Pedido** (`POST /atualizar_status/{pedido_id}`)
6. **Visualizar Pedidos na Cozinha** (`GET /cozinha`)
7. **Gerenciamento Administrativo**
   - Listar clientes (`GET /admin/clientes`)
   - Gerenciar produtos (`POST /admin/produtos`)
   - Acompanhar pedidos (`GET /admin/pedidos`)

### 4️⃣ Parar o Ambiente
Para parar os containers, pressione `CTRL+C` no terminal ou execute:
```sh
docker-compose down
```

## 📄 Licença
Este projeto é de código aberto e pode ser utilizado conforme os termos da licença definida no repositório.

---
Agora seu ambiente está pronto para testes! 🚀

