const express = require('express');
const app = express()
app.use(express.static('Leaflet'));
const port = 3000


app.get('/', (req, res) => {
  res.sendFile(__dirname + '/mapa.html');
});

app.listen(port, () => {
  console.log(`Aplicación escuchando en el puerto  ${port}`)
})
