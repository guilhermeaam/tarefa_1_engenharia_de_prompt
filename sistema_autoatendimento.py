from flask import Flask, request, jsonify, render_template
import random
import time

app = Flask(__name__)

# Simulando o banco de dados
clientes = {}
pedidos = {}
produtos = {
    Lanche [
        {id 1, nome Hambúrguer, descricao Pão, carne, queijo e alface, preco 15.0},
        {id 2, nome Hot Dog, descricao Pão, salsicha, ketchup e mostarda, preco 10.0},
    ],
    Acompanhamento [
        {id 3, nome Batata Frita, descricao Porção de batatas fritas, preco 8.0},
        {id 4, nome Anéis de Cebola, descricao Porção de anéis de cebola fritos, preco 9.0},
    ],
    Bebida [
        {id 5, nome Refrigerante, descricao Lata de 350ml, preco 5.0},
        {id 6, nome Água, descricao Garrafa de 500ml, preco 3.0},
    ],
    Sobremesa [
        {id 7, nome Sorvete, descricao Casquinha de sorvete, preco 7.0},
        {id 8, nome Brownie, descricao Brownie de chocolate, preco 6.0},
    ]
}

# Rotas do sistema
@app.route(, methods=[GET])
def home()
    return render_template(home.html)

@app.route(identificacao, methods=[POST])
def identificacao()
    data = request.json
    if data.get(cpf)
        if data[cpf] in clientes
            return jsonify({message Cliente identificado, cliente clientes[data[cpf]]}), 200
        else
            return jsonify({message CPF não cadastrado}), 404
    elif data.get(nome) and data.get(email)
        cpf = str(random.randint(10000000000, 99999999999))
        clientes[cpf] = {nome data[nome], email data[email]}
        return jsonify({message Cliente cadastrado com sucesso, cpf cpf}), 201
    else
        return jsonify({message Cliente anônimo}), 200

@app.route(produtos, methods=[GET])
def produtos_disponiveis()
    return jsonify(produtos), 200

@app.route(pedido, methods=[POST])
def criar_pedido()
    data = request.json
    itens = data.get(itens, [])
    if not itens
        return jsonify({message Nenhum item selecionado}), 400

    pedido_id = str(random.randint(1000, 9999))
    total = sum(item[preco] for item in itens)
    pedidos[pedido_id] = {itens itens, status Recebido, total total}

    # Simulando QR Code
    qr_code_link = fhttpswww.mercadopago.com.brqrcode{pedido_id}
    return jsonify({pedido_id pedido_id, total total, qr_code qr_code_link}), 201

@app.route(statuspedido_id, methods=[GET])
def status_pedido(pedido_id)
    if pedido_id in pedidos
        return jsonify(pedidos[pedido_id]), 200
    else
        return jsonify({message Pedido não encontrado}), 404

@app.route(atualizar_statuspedido_id, methods=[POST])
def atualizar_status(pedido_id)
    if pedido_id not in pedidos
        return jsonify({message Pedido não encontrado}), 404

    status_atual = pedidos[pedido_id][status]
    proximos_status = {Recebido Em Preparação, Em Preparação Pronto, Pronto Finalizado}

    if status_atual in proximos_status
        pedidos[pedido_id][status] = proximos_status[status_atual]
        return jsonify({message Status atualizado, status pedidos[pedido_id][status]}), 200
    else
        return jsonify({message Pedido já finalizado}), 400

if __name__ == __main__
    app.run(debug=True)
