import java.util.ArrayList;
import java.util.Scanner;

public class main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("Menú:");
            System.out.println("1. Insertar elemento en la lista");
            System.out.println("2. Opción 2");
            System.out.println("3. Opción 3");
            System.out.println("4. Salir");
            System.out.print("Ingrese una opción: ");
            opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    // Lógica de la opción 1
                    Scanner sc = new Scanner(System.in);
                    System.out.println("Ingrese un string");
                    String ingreso = sc.nextLine();
                    break;
                case 2:
                    // Lógica de la opción 2
                    System.out.println("Ha seleccionado la opción 2.");
                    break;
                case 3:
                    // Lógica de la opción 3
                    System.out.println("Ha seleccionado la opción 3.");
                    break;
                case 4:
                    // Salir del menú
                    System.out.println("Saliendo del menú.");
                    break;
                default:
                    System.out.println("Opción inválida. Por favor seleccione una opción válida.");
                    break;
            }
        } while (opcion != 4);

        scanner.close();
    }

}