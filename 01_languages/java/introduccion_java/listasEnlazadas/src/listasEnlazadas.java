//En esta importacion lo que vamos a hacer es permitirle a la clsae almacenar datos en memorio de una forma dinamica
import java.util.ArrayList;
import java.util.Scanner;

public class listasEnlazadas {

    //En esta parte del codigo lo que estamos haciendo es crear una lista
    // en la cual vamos a permitir objetos de tipo String
    public static void main(String[] args){
        ArrayList<String> listaDeStrings = new ArrayList<String>();

        // En estas lineas de codigo lo que etsamos haciendo es diciendole al usuario que ingrese un elemento
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un string");
        String ingreso = sc.nextLine();
        listaDeStrings.add(ingreso);
        System.out.println("Acabas de añadir: " + ingreso);
        listaDeStrings.add("Todo ok");
        listaDeStrings.add("ok");

        //sc.close();
        System.out.println("------------------------------------------------------------------------------");

        // En esta linea lo que estamos haciendo es contar el numero de elementos
        // que tenemos almacenados en la lista y este mismo lo almacenamos en una variable para luego imprimirla
        int numeroElementos = listaDeStrings.size();
        System.out.println("La lista tiene " + numeroElementos + " Elementos");
        System.out.println("------------------------------------------------------------------------------");

            //En la siguiente line lo que vamos a hacer es indicar el elemento que se encuentra en una determinada posicion
            //int posicionElemento = listaDeStrings.get(1);
            //System.out.println("El elemento de la pasicion 1 es" + posicionElemento);

        System.out.println("------------------------------------------------------------------------------");
        //Scanner scan = new Scanner(System.in);
        //Comprobamos un elemento de la lista
        System.out.println("Ingrese el elemento que quiere evaluar si se encuentra en la lista: ");
        String elemento = sc.nextLine();
        //sc.close();

        if (listaDeStrings.contains(elemento)) {
            System.out.println("El elemento " + elemento + " se encuentra en la lista");
        }else {
            System.out.println("El elemento" + elemento + " no se encuenta en la lista");
        }
        System.out.println("------------------------------------------------------------------------------");
        //Imprimimos los elementos que contiene la lista
        System.out.println("Imprimimos los elementos de la lista ");
        System.out.println(listaDeStrings);

        System.out.println("------------------------------------------------------------------------------");
        //Insertamos un nuevo elemento
        System.out.println("Que elemento quieres ingresar?");
        String nuevoElemento = sc.nextLine();
        listaDeStrings.add(nuevoElemento);
        System.out.println("El nuevo elemento es " + nuevoElemento);
        System.out.println(listaDeStrings);

        //Sacamos un elemeto concreto de la lista
        System.out.println("Que elemento quieres sacar de la lista?");
        String elementoFuera = sc.nextLine();
        listaDeStrings.remove(elementoFuera);
        System.out.println("El elemento que eliminista fue: " + elementoFuera);
        System.out.println(listaDeStrings);

                //Sacar el elemento que ocupa una posición en la lista
            //System.out.println("Que elemento quieres sacar de la lista por posicion?");
            //String posicionFuera = sc.nextLine();
            //listaDeStrings.remove(posicionFuera);
            //System.out.println("El elemento que eliminista fue: " + posicionFuera);
            //System.out.println(listaDeStrings);
        //reemplazar un elemento de la lista
        System.out.println("Que elemento quieres reemplazar de la lista?");
        String antiguo = sc.nextLine();
        sc.nextLine();
        System.out.println("Ingresa el nuevo valor del elemento:");
        String nuevoValor = sc.nextLine();
        listaDeStrings.set(Integer.parseInt(antiguo), nuevoValor);
        System.out.println("La lista actualizada es: " + listaDeStrings);

    }
}
