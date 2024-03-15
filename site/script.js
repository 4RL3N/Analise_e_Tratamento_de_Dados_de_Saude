// Adiiciona um ouvinte de evento de clique ao elemento com o ID "btnSubmit"
document.getElementById("btnSubmit").addEventListener("click", function() {
    // Obtém o valor do elemento com o ID "year"
    var selectedYear = document.getElementById("year").value;

    // Se nenhum ano foi selecionado, exibe um alerta e retorna
    if (!selectedYear) {
        alert("Por favor, escolha um ano.");
        return;
    }

    // Obtém o valor do botão de opção selecionado com o nome "mapType"
    var mapType = document.querySelector('input[name="mapType"]:checked');
    // Se nenhum tipo de mapa foi selecionado, exibe um alerta e retorna
    if (!mapType) {
        alert("Por favor, escolha um tipo de mapa.");
        return;
    }

    mapType = mapType.value;

    // Se o tipo de mapa selecionado for "colormetrico", exibe uma imagem no elemento com o ID "mapContainer"
    if (mapType === "colormetrico") {
        // Obtém a referência ao contêiner do mapa
        var mapContainer = document.getElementById("mapContainer");
    
        // Remove qualquer elemento filho existente no contêiner do mapa
        while (mapContainer.firstChild) {
            mapContainer.removeChild(mapContainer.firstChild);
        }
    
        // Cria um título para exibir a média de empenhado
        var titulo = document.createElement("h2");
        titulo.textContent = "Média de empenhado";
    
        // Adiciona o título ao contêiner do mapa
        mapContainer.appendChild(titulo);
    
        // Adiciona a nova imagem ao contêiner do mapa
        mapContainer.innerHTML += `<img src="mapa_resultado${selectedYear}.png" alt="Mapa">`;
        mapContainer.style.display = "block";
    }
    
    
    // Se o tipo de mapa selecionado for "interativo", redireciona para uma página HTML específica
    else if (mapType === "interativo") {
        window.location.href = `interativo_${selectedYear}.html`;
    }
});

// Para cada botão de opção com o nome "mapType", adiciona um ouvinte de evento de clique
document.querySelectorAll('input[name="mapType"]').forEach(function(btn) {
    btn.addEventListener("click", function() {
        // Obtém o valor do botão de opção clicado
        var optionSelected = this.getAttribute("value");
        // Se o valor for "colormetrico" ou "interativo", exibe o elemento com o ID "yearInput" e oculta o elemento com o ID "mapContainer"
        if (optionSelected === "colormetrico" || optionSelected === "interativo") {
            document.getElementById("yearInput").style.display = "block";
            document.getElementById("mapContainer").style.display = "none";
        }
    });
});
