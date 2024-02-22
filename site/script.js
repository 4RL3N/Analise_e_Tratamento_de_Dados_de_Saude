document.getElementById("btnSubmit").addEventListener("click", function() {
    var selectedYear = document.getElementById("year").value;
    if (!selectedYear) {
        alert("Por favor, escolha um ano.");
        return;
    }

    var mapType = document.querySelector('input[name="mapType"]:checked');
    if (!mapType) {
        alert("Por favor, escolha um tipo de mapa.");
        return;
    }
    mapType = mapType.value;

    if (mapType === "colormetrico") {
        document.getElementById("mapContainer").innerHTML = `<img src="mapa_resultado${selectedYear}.png" alt="Mapa">`;
        document.getElementById("mapContainer").style.display = "block";
    } else if (mapType === "interativo") {
        window.location.href = `interativo_${selectedYear}.html`;
    }
});

document.querySelectorAll('input[name="mapType"]').forEach(function(btn) {
    btn.addEventListener("click", function() {
        var optionSelected = this.getAttribute("value");
        if (optionSelected === "colormetrico" || optionSelected === "interativo") {
            document.getElementById("yearInput").style.display = "block";
            document.getElementById("mapContainer").style.display = "none";
        }
    });
});
