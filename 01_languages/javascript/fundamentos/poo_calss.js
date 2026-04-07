class Persona{
    constructor(nombre,edad){
        this.nombre = nombre
        this.edad = edad
    }
    saludar() {
        `Hola, mi nombre es ${this.nombre} y mi edad es ${this.edad}`
    }
}

const persona1 = new Persona("David", 20)
persona1.saludar()
console.log(persona1)

// Herencia

class Animal {
    constructor(nombre, tipo) {
        this.nombre = nombre
        this.tipo = tipo
    }

    emitirSonido() {
        console.log("El animal emite un sonido")
    }
}

class Perro extends Animal {
    constructor(nombre, tipo, raza) {
        super(nombre, tipo)
        this.raza = raza
    }

    emitirSonido(){
        console.log("El perro ladra")
    }
    correr(){
        console.log(`${this.nombre} corre alegremente`)
    }
}

const perro1 = new Perro("odin", "Mediano", "collie")
const perro2 = new Perro("maya", "Mediano", "collie")

perro1.correr()
perro2.emitirSonido()