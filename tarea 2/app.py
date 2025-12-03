from flask import Flask, render_template
import os

app = Flask(__name__)

# Datos de los animales
animales = [
    {
        'id': 1,
        'nombre': 'Ternero',
        'descripcion': 'Ternero de raza Holando argentino, 6-8 meses, alimentación controlada',
        'lote': 'Lote A-15',
        'precio': '$2500000',
        'imagen': 'ternero.jpg'
    },
    {
        'id': 2,
        'nombre': 'Novillo',
        'descripcion': 'Novillo de raza Angus, 18-24 meses, peso aprox. 450 kg',
        'lote': 'Lote B-07',
        'precio': '$8.050.000',
        'imagen': 'novillo.jpg'
    },
    {
        'id': 3,
        'nombre': 'Novillito',
        'descripcion': 'Novillitos de raza Hereford, 12-14 meses, excelente estado sanitario',
        'lote': 'Lote C-22',
        'precio': '$6.050.000',
        'imagen': 'novillito.jpg'
    },
    {
        'id': 4,
        'nombre': 'Vaquillona',
        'descripcion': 'Vaquillona preñada de raza Brangus, 24 meses, inseminada con toro de pedigree',
        'lote': 'Lote D-11',
        'precio': '$9.050.000',
        'imagen': 'vaquillona.jpg'
    },
    {
        'id': 5,
        'nombre': 'Vaca',
        'descripcion': 'Vaca productora de raza Jersey, 5 años, producción de 22 litros/día',
        'lote': 'Lote E-03',
        'precio': '$11.200.000',
        'imagen': 'vaca.jpg'
    },
    {
        'id': 6,
        'nombre': 'Toro',
        'descripcion': 'Toro reproductor de raza Brahman, 4 años, pedigree certificado',
        'lote': 'Lote F-18',
        'precio': '$10.500.000',
        'imagen': 'toro.jpg'
    }
]

@app.route('/')
def index():
    return render_template('index.html', animales=animales)

if __name__ == '__main__':

    
    app.run(debug=True, port=5000)