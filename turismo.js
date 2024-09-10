class PaqueteTuristico {
    constructor(destino, fecha, precioVuelo, precioHotel) {
        this.destino = destino;
        this.fecha = fecha;
        this.precioVuelo = precioVuelo;
        this.precioHotel = precioHotel;
    }

    mostrarDetalles() {
        return `Destino: ${this.destino}, Fecha: ${this.fecha}, Precio Vuelo: ${this.precioVuelo}, Precio Hotel: ${this.precioHotel}/noche`;
    }

    calcularCostoTotal(noches) {
        return this.precioVuelo + (this.precioHotel * noches);
    }
}

function search() {
    const destination = document.getElementById('destination').value;
    const travelDate = document.getElementById('travel-date').value;

    if (destination && travelDate) {
        const resultsContainer = document.getElementById('results-container');
        resultsContainer.innerHTML = `<p>Buscando viajes a <strong>${destination}</strong> en la fecha <strong>${travelDate}</strong>...</p>`;

        setTimeout(() => {
            const paquete = new PaqueteTuristico(destination, travelDate, 500, 150);
            resultsContainer.innerHTML = `
                <p>${paquete.mostrarDetalles()}</p>
                <p>Costo total para 5 noches: $${paquete.calcularCostoTotal(5)}</p>
            `;
        }, 1000);
    } else {
        alert('Por favor, ingrese un destino y una fecha de viaje.');
    }
}

function mostrarNotificaciones() {
    const ofertas = [
        "¡Oferta especial! Vuelo a Nueva York con 20% de descuento.",
        "Paquete todo incluido a Cancún disponible por tiempo limitado.",
        "Reserva un hotel en Tokio y recibe una noche gratis.",
        "Descuento del 30% en vuelos a Barcelona para este fin de semana."
    ];

    setInterval(() => {
        const indice = Math.floor(Math.random() * ofertas.length);
        const notificacion = document.createElement('div');
        notificacion.className = 'notificacion';
        notificacion.innerText = ofertas[indice];
        
        document.body.appendChild(notificacion);

        setTimeout(() => {
            document.body.removeChild(notificacion);
        }, 5000); // Notificación visible por 5 segundos
    }, 10000); // Nueva notificación cada 10 segundos
}

mostrarNotificaciones();
