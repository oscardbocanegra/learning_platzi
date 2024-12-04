const numeroSecreto = Math.floor(Math.random() *10 + 1)

const nuemroJugador = parseInt(
    prompt("Adivina el numero secreto entre el 1 al 10")
)

console.log(`Este es el numero con el que juegas ${nuemroJugador}`)

if (nuemroJugador === numeroSecreto){
    console.log("Felicidades, adivinaste el numeo secreto")
}else if (nuemroJugador < numeroSecreto){
    console.log("El numero es mayor al que indicaste, intenta de nuevo")
}else if (nuemroJugador > numeroSecreto){
    console.log("El numero es menor al que indicaste, intenta de nuevo ")
}