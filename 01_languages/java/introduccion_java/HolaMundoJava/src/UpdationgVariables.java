public class UpdationgVariables {
    public static void main(String[] args) {
        int salary = 60000;
        //bono 200
        salary = salary + 200;
        System.out.println(salary);

        //pension descuento 50
        salary = salary - 50;
        System.out.println(salary);

        //2 horas extra
        //Comida: $45
        salary = salary + (30*2) - 45;
        System.out.println(salary);

        //Actualizar cadenas de texto
        String employeeName = "Oscar David Bocanegra";
        employeeName = employeeName + " Capera";
        System.out.println(employeeName);

        employeeName = "Futuro mejor ingeniero " + employeeName;
        System.out.println(employeeName);
    }
}
