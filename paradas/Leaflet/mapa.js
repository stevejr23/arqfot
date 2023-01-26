// Crear la variable mapa con coordenadas de centro y zoom
let map = L.map('map').setView([-4.0075952, -79.2022123], 16)

// Agregar mapa base de OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Volar a coordenadas de los sitios de la Lista desplegable
document.getElementById('select-location').addEventListener('change', function (e) {
    let coords = e.target.value.split(",");
    map.flyTo(coords, 13);
})

// Agregar mapa base para el Mini Mapa
var carto_light = L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', { attribution: '©OpenStreetMap, ©CartoDB', subdomains: 'abcd', maxZoom: 26 });

// Agregar plugin MiniMap
var minimap = new L.Control.MiniMap(carto_light,
    {
        toggleDisplay: true,
        minimized: false,
        position: "bottomleft"
    }).addTo(map);

// Agregar escala
new L.control.scale({ imperial: false }).addTo(map);


// Agregar coordenadas para dibujar una polilinea
var BusA = [
    [-3.994550, -79.205290],
    [-3.994803, -79.205256],
    [-3.995383, -79.205172],
    [-3.995696, -79.205137],
    [-3.996140, -79.205093],
    [-3.996502, -79.205049],
    [-3.996707, -79.205022],
    [-3.997152, -79.204951],
    [-3.997379, -79.204920],
    [-4.001298, -79.204501]

];

// Ruta Bus
var BusA = L.polyline(BusA, {
    color: 'green'
}).addTo(map);

// Agregar un marcador
var marker_hospitalUTPL = L.circleMarker(L.latLng(-3.985775, -79.199130), {
    radius: 6,
    fillColor: "#ff0000",
    color: "blue",
    weight: 2,
    opacity: 3,
    fillOpacity: 1,
}).addTo(map);

// Agregar un marcador
var marker_taxi = L.icon({
    iconUrl: 'Leaflet.Legend-master/examples/marker/taxi.png',
    iconSize: [15, 15],
    iconAnchor: [15, 15],
    //popupAnchor: [-3, -76]
});
L.marker(L.latLng(-3.9950942,-79.2047547), {icon: marker_taxi}).addTo(map);

// Agregar la leyenda
const legend = L.control.Legend({
    position: "bottomright",
    collapsed: false,
    symbolWidth: 24,
    opacity: 1,
    column: 1,
    legends: [
        {
            label: "Ubicacion Usuario",
            type: "circle",
            radius: 5,
            color: "blue",
            fillColor: "#FF0000",
            fillOpacity: 1,
            weight: 2,
            layers: [marker_hospitalUTPL],
            inactive: false,
        }, {
            label: "Ruta Bus A",
            type: "polyline",
            color: "#FF0000",
            fillColor: "#FF0000",
            weight: 2,
            layers: BusA
        }, {
            label: "Taxi 1",
            type: "image",
            url: "Leaflet.Legend-master/examples/marker/taxi.png",
            layers: [marker_taxi],
            
        }]
}).addTo(map);