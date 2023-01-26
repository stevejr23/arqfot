const mapa = document.getElementById('maparadas')

const map = L.map(mapa).setView([40.4381311, -3.8196232], 13);

const rutaSelector = document.getElementById('paradas')

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

const getData = async () => {
    const responseParadas = await fetch('./data/paradasbus.json');
    const dataParadas = await responseParadas.json();
    paradas = dataParadas.features;
    console.log(paradas);   

    // const getLine = (nameLine) => paradas.filter(paradas => paradas.properties.linea.includes(nameLine))

    // const paradasRuta1 = getLine("330");
    // const paradasRuta2 = getLine("N302");
    // const paradasRuta3 = getLine("334");
    // const paradasRuta4 = getLine("332");
    // const paradasRuta5 = getLine("331");
    // rutaSelector.addEventListener('chage', (e) => {
    //     if (e.target.value == 'ruta1') {
    //         L.geoJSON(paradasRuta1)
    //             .addTo(map)
    //     } else if (e.target.value == 'ruta2') {
    //         L.geoJSON(paradasRuta2)
    //             .addTo(map)
    //     } else if (e.target.value == 'ruta3') {
    //         L.geoJSON(paradasRuta3)
    //             .addTo(map)
    //     } else if (e.target.value == 'ruta4') {
    //         L.geoJSON(paradasRuta4)
    //             .addTo(map)
    //     }
    // }
    // )
}

getData()