const express = require('express');
const mongoose = require('mongoose');
const app = express();
const port = 3000;

// Conectar a MongoDB Atlas
mongoose.connect('mongodb://localhost:27017/tienda', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

// Esquemas de ejemplo para las colecciones
const TacoSchema = new mongoose.Schema({}, { collection: 'tacos' });
const TortaSchema = new mongoose.Schema({}, { collection: 'tortas' });

const Taco = mongoose.model('Taco', TacoSchema);
const Torta = mongoose.model('Torta', TortaSchema);

// Configuración de EJS para las vistas
app.set('view engine', 'ejs');

// Ruta principal para mostrar el inventario y las promociones
app.get('/', async (req, res) => {
    try {
        // Contar documentos en cada colección
        const tacosCount = await Taco.countDocuments({});
        const tortasCount = await Torta.countDocuments({});

        // Promociones
        const tacosPromoPrice = 100; // 10 tacos por 100 pesos
        const tortasPromoPrice = 80; // 2 tortas por 80 pesos

        res.render('inventory', { 
            tacosCount, 
            tortasCount, 
            tacosPromoPrice, 
            tortasPromoPrice 
        });
    } catch (err) {
        console.error(err);
        res.status(500).send('Error al obtener el inventario');
    }
});

// Iniciar servidor
app.listen(port, () => {
    console.log(`Servidor corriendo en http://localhost:${port}`);
});

// Inicializar inventario si es necesario (solo ejecutar una vez)
 async function inicializarInventario() {
     await Taco.insertMany(Array(1000).fill({}));
     await Torta.insertMany(Array(500).fill({}));
     console.log('Inventario inicializado');
 }
 inicializarInventario();
