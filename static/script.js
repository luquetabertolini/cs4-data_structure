async function carregarSessoes() {

    const resposta = await fetch("/api/sessoes");

    const sessoes = await resposta.json();

    mostrarSessoes(sessoes);
}


function mostrarSessoes(sessoes) {

    const tabela = document.getElementById("tabelaSessoes");

    tabela.innerHTML = "";

    sessoes.forEach(sessao => {

        const linha = document.createElement("tr");

        const horas = Math.floor(sessao.tempo);
        const minutos = Math.round((sessao.tempo - horas) * 60);

        linha.innerHTML = `
            <td>${sessao.id}</td>
            <td>${sessao.modelo}</td>
            <td>${sessao.tipo}</td>
            <td>${sessao.energia.toFixed(2)} kWh</td>
            <td>${horas}h ${String(minutos).padStart(2, "0")}min</td>
            <td>R$ ${sessao.custo.toFixed(2)}</td>
        `;

        tabela.appendChild(linha);
    });
}


document.getElementById("formSessao").addEventListener("submit", async function(event) {

    event.preventDefault();

    const dados = {

        id: Number(document.getElementById("id").value),

        modelo: document.getElementById("modelo").value,

        bateria_atual: Number(
            document.getElementById("bateria_atual").value
        ),

        bateria_alvo: Number(
            document.getElementById("bateria_alvo").value
        ),

        tipo: document.getElementById("tipo").value,

        hora_inicio: Number(
            document.getElementById("hora_inicio").value
        )
    };


    const resposta = await fetch("/api/sessoes", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(dados)
    });


    const resultado = await resposta.json();


    const mensagem = document.getElementById("mensagem");


    if (!resposta.ok) {

        mensagem.textContent = "Erro: " + resultado.erro;

        return;
    }


    mensagem.textContent =
        "Sessão cadastrada com sucesso!";


    document.getElementById("formSessao").reset();


    carregarSessoes();
});


async function buscarSessao() {

    const id = document.getElementById("idBusca").value;

    const resposta =
        await fetch(`/api/sessoes/${id}`);


    const resultado =
        await resposta.json();


    const area =
        document.getElementById("resultadoBusca");


    if (!resposta.ok) {

        area.innerHTML =
            `<p>Sessão não encontrada.</p>`;

        return;
    }


    area.innerHTML = `

        <h3>Sessão encontrada</h3>

        <p>ID: ${resultado.id}</p>

        <p>Veículo: ${resultado.modelo}</p>

        <p>Tipo: ${resultado.tipo}</p>

        <p>Energia: ${resultado.energia.toFixed(2)} kWh</p>

        <p>Custo: R$ ${resultado.custo.toFixed(2)}</p>

    `;
}


async function ordenar(chave) {

    const resposta =
        await fetch("/api/sessoes/ordenar", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                chave: chave
            })
        });


    const sessoes =
        await resposta.json();


    mostrarSessoes(sessoes);
}


async function carregarEstatisticas() {

    const resposta =
        await fetch("/api/estatisticas");


    const dados =
        await resposta.json();


    document.getElementById("estatisticas").innerHTML = `

        <p>Sessões realizadas:
            <strong>${dados.total_sessoes}</strong>
        </p>

        <p>Energia fornecida:
            <strong>${dados.energia_total.toFixed(2)} kWh</strong>
        </p>

        <p>Faturamento total:
            <strong>R$ ${dados.faturamento_total.toFixed(2)}</strong>
        </p>

        <p>Ticket médio:
            <strong>R$ ${dados.ticket_medio.toFixed(2)}</strong>
        </p>

        <p>Maior consumo:
            <strong>${dados.maior_consumo.toFixed(2)} kWh</strong>
        </p>

        <p>Menor consumo:
            <strong>${dados.menor_consumo.toFixed(2)} kWh</strong>
        </p>

    `;
}


carregarSessoes();