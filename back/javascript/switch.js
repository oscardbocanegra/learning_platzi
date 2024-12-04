let expr = "Papayas"

switch(expr) {
    case "Naranjas":
        console.log("Las naranjas cuestan $20 el kilo")
        break;
    case "Manzanas":
        console.log("Las manzanas cuestan $43 el kilo")
        break;
    
    case "Platanos":
        console.log("Los platanos cuestan $30 el kilo")
        break;

    case "Mangos":
    case "Papayas":
        console.log("Los mangos y las papayas cuestan $25 el kilo")
        break;
    default:
        console.log(`Lo siento no contamos con ${expr}`)
}