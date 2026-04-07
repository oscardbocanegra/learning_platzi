public class Funciones {
    public static void main(String[] args) {
        double y = 3;
        circleArea(y);
        spheraArea(y);
        sphereVolumen(y);


        System.out.println("Pesos a dolares: " + converToDolar(1000, "COP"));
    }

    public static double circleArea(double r){
        return Math.PI * Math.pow(r,2);
    }

    public static double spheraArea(double r) {
        return 4 * Math.PI * Math.pow(r, 2);
    }

    public static double sphereVolumen(double r){
            return (4/3) * Math.PI * Math.pow(r,3);
    }

    /**
     * Descripcion: Funcion que especificando su moneda convierte una cantidad de pesos a dolares
     *
     * @param quantity Cantidad de dinero
     * @param currency Tipo de mondeda: Solo acepta pesos MXN o pesos COP
     * @return quantity devuelve la cantidad actualizada de dolares
     * */
    public static double converToDolar(double quantity, String currency){
        //MXN COP
        switch (currency){
            case "MXN":
                quantity = quantity * 0.052;
                break;
            case "COP":
                quantity = quantity * 0.00031;
                break;
        }
        return quantity;
    }
}
