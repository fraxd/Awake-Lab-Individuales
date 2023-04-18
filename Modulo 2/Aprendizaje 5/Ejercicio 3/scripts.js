window.addEventListener('load', () => {

    // Centro de la pagina (centro teorico del semafro)
    const centro = {
        x: window.innerWidth / 2,
        y: window.innerHeight / 2
    };
    var flagStop = false;
    var distancia = 500;

    window.addEventListener('mousemove', (event) => {
        // Obtener las coordenadas del puntero del mouse
        const puntero = {
            x: event.clientX,
            y: event.clientY
        };

        // Calcular la distancia entre el puntero y el centro de la página
        distancia = Math.sqrt(
            Math.pow(puntero.x - centro.x, 2) +
            Math.pow(puntero.y - centro.y, 2)
        );


        // Para revisar la distancia desde el centro de la pagina
        //console.log(distancia)

        //Analisis de que hacer
        if (distancia < 150) pasarArojo();
        if (distancia >= 150 && distancia <= 200) pasarAamarillo();
        if (flagStop && distancia > 200) {
            flagStop = false;
            pasarAVerde();
        }
    });

    // Semaforo default Verde
    function pasarAVerde() {
        document.getElementById("red").style.backgroundColor = '#000000';
        document.getElementById("yellow").style.backgroundColor = '#000000';
        document.getElementById("green").style.backgroundColor = '#00ff00'; // Activo
        if (distancia >= 200) setTimeout(pasarAamarillo, 3000);
        else flagStop = true;
    }
    //Semaforo Default Amarillo
    function pasarAamarillo() {
        document.getElementById("red").style.backgroundColor = '#000000';
        document.getElementById("yellow").style.backgroundColor = '#ffff00';// Activo
        document.getElementById("green").style.backgroundColor = '#000000';
        if (distancia >= 200) {
            setTimeout(pasarArojo, 1000);
        }
        else flagStop = true;

    }
    // Semafoto Default Rojo
    function pasarArojo() {
        document.getElementById("red").style.backgroundColor = '#ff0000';// Activo
        document.getElementById("yellow").style.backgroundColor = '#000000';
        document.getElementById("green").style.backgroundColor = '#000000';
        if (distancia >= 200) {
            setTimeout(pasarAVerde, 3000);
        }
        else flagStop = true;

    }



    // INICIO AUTOMATICO
    pasarAVerde();
});
