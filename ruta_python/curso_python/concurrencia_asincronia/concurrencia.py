import threading
import time

# Funcion que simula el procesamiento de una solicitud
def process_request(nombre):
    print(f'Procesando solicitud de {nombre}')
    time.sleep(2)
    print(f'Solicitud de {nombre} procesada')

threads = []

for i in range(3):
    #Crear nuevo hilo que ejecuta la funcion process_request
    thread = threading.Thread(target=process_request, args=(f'Usuario {i}',))
    threads.append(thread)
    thread.start()

# Esperar a que todos los hilos terminen
for thread in threads:
    thread.join()

print('Todas las solicitudes han sido procesadas')