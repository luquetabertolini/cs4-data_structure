EFICIENCIA = 0.90


class Sessao:
    def __init__(self, id_sessao, modelo, tipo, energia, tempo, custo):
        self.id = id_sessao
        self.modelo = modelo
        self.tipo = tipo
        self.energia = energia
        self.tempo = tempo
        self.custo = custo

    def para_dict(self):
        return {
            "id": self.id,
            "modelo": self.modelo,
            "tipo": self.tipo,
            "energia": round(self.energia, 2),
            "tempo": round(self.tempo, 2),
            "custo": round(self.custo, 2)
        }


def busca_sequencial_id(sessoes, id_procurado):
    for i in range(len(sessoes)):
        if sessoes[i].id == id_procurado:
            return i

    return -1


def bubble_sort(sessoes, chave):
    n = len(sessoes)

    for i in range(n):
        trocou = False

        for j in range(0, n - 1 - i):
            val1 = getattr(sessoes[j], chave)
            val2 = getattr(sessoes[j + 1], chave)

            if val1 > val2:
                sessoes[j], sessoes[j + 1] = sessoes[j + 1], sessoes[j]
                trocou = True

        if not trocou:
            break


def calcular_tarifa(hora_inicio):
    if 17 <= hora_inicio <= 21:
        return 1.30
    elif 0 <= hora_inicio <= 6:
        return 0.80

    return 1.00


def criar_sessao(
    id_sessao,
    modelo,
    tipo,
    bateria_atual,
    bateria_alvo,
    hora_inicio,
    sessoes
):
    capacidades = {
        "BYD": 75.0,
        "BMW": 130.0,
        "Renault": 36.0
    }

    precos = {
        "Padrão": 0.90,
        "Premium": 1.50
    }

    potencias = {
        "Padrão": 21.0,
        "Premium": 55.0
    }

    capacidade_max = capacidades[modelo]

    pct_restante = bateria_alvo - bateria_atual

    energia_util = capacidade_max * (pct_restante / 100.0)

    energia_consumida = energia_util / EFICIENCIA

    potencia = potencias[tipo]
    preco = precos[tipo]

    if len(sessoes) >= 3:
        potencia = potencia * 0.80

    tempo_horas = energia_consumida / potencia

    custo_base = energia_consumida * preco

    taxa = calcular_tarifa(hora_inicio)

    custo_final = custo_base * taxa

    return Sessao(
        id_sessao,
        modelo,
        tipo,
        energia_consumida,
        tempo_horas,
        custo_final
    )


def calcular_estatisticas(sessoes):
    if not sessoes:
        return {
            "total_sessoes": 0,
            "energia_total": 0,
            "faturamento_total": 0,
            "ticket_medio": 0,
            "maior_consumo": 0,
            "menor_consumo": 0
        }

    total_sessoes = len(sessoes)

    energia_total = sum(s.energia for s in sessoes)

    faturamento_total = sum(s.custo for s in sessoes)

    ticket_medio = faturamento_total / total_sessoes

    maior_consumo = max(s.energia for s in sessoes)

    menor_consumo = min(s.energia for s in sessoes)

    return {
        "total_sessoes": total_sessoes,
        "energia_total": round(energia_total, 2),
        "faturamento_total": round(faturamento_total, 2),
        "ticket_medio": round(ticket_medio, 2),
        "maior_consumo": round(maior_consumo, 2),
        "menor_consumo": round(menor_consumo, 2)
    }