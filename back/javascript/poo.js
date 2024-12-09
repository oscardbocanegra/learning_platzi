const persona = {
    nombre: "Oscar",
    edad: 20,
    direccion: {
        calle: "Cr5, #4-32",
        ciudad: "Tenjo - Cundinamarca"
    },
    saludar() {
        console.log(`Hola, mi nombre es ${persona.nombre}`)
    }
}

console.log(persona)
persona.saludar()

// Funcion constructora

function Presona(nombre, apellido, edad) {
    this.nombre = nombre
    this.apellido = apellido
    this.edad = edad
}

const persona1 = new Presona("David", "Bocanegra", 20)
console.log(persona1)
persona1.nacionalidad = "Colombiana"
console.log(persona1)