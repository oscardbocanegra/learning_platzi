function calculateDiscpuntPrice (price, discountPercentage){
    const discount = (price * discountPercentage) / 100
    const priceWithDiscount = price - discount

    return priceWithDiscount
}

console.log('El precio con descuento es de: $' + calculateDiscpuntPrice(100, 20))