from flask import Flask, render_template, request, jsonify

from sistema import (
    Sessao,
    busca_sequencial_id,
    bubble_sort,
    criar_sessao,
    calcular_estatisticas
)


app = Flask(__name__)

sessoes = []


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/api/sessoes", methods=["GET"])
def listar_sessoes():
    return jsonify([
        sessao.para_dict()
        for sessao in sessoes
    ])


@app.route("/api/sessoes", methods=["POST"])
def cadastrar_sessao():
    dados = request.json

    id_sessao = int(dados["id"])
    modelo = dados["modelo"]
    tipo = dados["tipo"]
    bateria_atual = float(dados["bateria_atual"])
    bateria_alvo = float(dados["bateria_alvo"])
    hora_inicio = int(dados["hora_inicio"])

    if busca_sequencial_id(sessoes, id_sessao) != -1:
        return jsonify({
            "erro": "ID já cadastrado."
        }), 400

    if bateria_atual < 0 or bateria_atual > 100:
        return jsonify({
            "erro": "Bateria atual inválida."
        }), 400

    if bateria_alvo <= bateria_atual or bateria_alvo > 100:
        return jsonify({
            "erro": "Bateria alvo inválida."
        }), 400

    if modelo not in ["BYD", "BMW", "Renault"]:
        return jsonify({
            "erro": "Modelo inválido."
        }), 400

    if tipo not in ["Padrão", "Premium"]:
        return jsonify({
            "erro": "Tipo de carregamento inválido."
        }), 400

    if hora_inicio < 0 or hora_inicio > 23:
        return jsonify({
            "erro": "Horário inválido."
        }), 400

    nova_sessao = criar_sessao(
        id_sessao,
        modelo,
        tipo,
        bateria_atual,
        bateria_alvo,
        hora_inicio,
        sessoes
    )

    sessoes.append(nova_sessao)

    return jsonify(nova_sessao.para_dict()), 201


@app.route("/api/sessoes/<int:id_sessao>", methods=["GET"])
def buscar_sessao(id_sessao):
    indice = busca_sequencial_id(sessoes, id_sessao)

    if indice == -1:
        return jsonify({
            "erro": "Sessão não encontrada."
        }), 404

    return jsonify(
        sessoes[indice].para_dict()
    )


@app.route("/api/sessoes/ordenar", methods=["POST"])
def ordenar_sessoes():
    dados = request.json

    chave = dados.get("chave")

    chaves_permitidas = [
        "id",
        "energia",
        "custo",
        "tempo"
    ]

    if chave not in chaves_permitidas:
        return jsonify({
            "erro": "Critério de ordenação inválido."
        }), 400

    bubble_sort(sessoes, chave)

    return jsonify([
        sessao.para_dict()
        for sessao in sessoes
    ])


@app.route("/api/estatisticas", methods=["GET"])
def estatisticas():
    return jsonify(
        calcular_estatisticas(sessoes)
    )


if __name__ == "__main__":
    app.run(debug=True)