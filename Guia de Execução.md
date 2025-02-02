# Instruções para Rodar o Projeto Localmente

## 1. Requisitos
Antes de iniciar, verifique se os seguintes requisitos estão instalados:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Postman](https://www.postman.com/downloads/) (opcional, mas recomendado para testes das APIs)

## 2. Clonar o Repositório
Abra um terminal e execute o seguinte comando para clonar o repositório:
```sh
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

## 3. Construir e Executar os Containers
Na raiz do projeto, execute:
```sh
docker-compose up --build
```
Isso irá iniciar todos os containers necessários, incluindo o backend e banco de dados.

## 4. Testar as APIs no Postman
Importe o arquivo de coleção Postman (`api_tests.json`) no Postman e siga a ordem das chamadas:

### Ordem Recomendada de Testes:
1. **Identificação do Cliente**
   - Via CPF ou Cadastro de novo cliente
   - Endpoint: `POST /identificacao`
2. **Obter Lista de Produtos Disponíveis**
   - Endpoint: `GET /produtos`
3. **Criar um Novo Pedido**
   - Endpoint: `POST /pedido`
4. **Consultar Status do Pedido**
   - Endpoint: `GET /status/{pedido_id}`
5. **Atualizar Status do Pedido**
   - Endpoint: `POST /atualizar_status/{pedido_id}` (somente para simulação da cozinha)
6. **Visualizar Pedidos na Cozinha**
   - Endpoint: `GET /cozinha`
7. **Gerenciamento Administrativo**:
   - Listar clientes: `GET /admin/clientes`
   - Gerenciar produtos: `POST /admin/produtos`
   - Acompanhar pedidos: `GET /admin/pedidos`

## 5. Parar o Ambiente
Para parar os containers, pressione `CTRL+C` no terminal onde o Docker está rodando ou execute:
```sh
docker-compose down
```

Agora seu ambiente está pronto para testes! Caso tenha alguma dúvida ou encontre erros, verifique os logs do Docker ou entre em contato com o suporte do projeto. 🚀

