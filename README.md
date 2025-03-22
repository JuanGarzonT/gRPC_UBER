# My-UBER gRPC Service

Este proyecto implementa un servicio remoto para la aplicación My-UBER utilizando gRPC en Python. 
Permite a los usuarios:

- Registrarse con nombre y teléfono.
- Consultar los tipos de servicio** disponibles.
- Solicitar un taxi basado en coordenadas dentro de una matriz 10x10.

# 📝 Requisitos

Asegúrate de tener instalado:
- Python 3.8+
- `grpcio` y `grpcio-tools`

Para instalarlos toca ir a la consola de comando y ejecutar:

- pip install grpcio grpcio-tools

# 📂 Estructura del Proyecto

GRPC_UBER/

├── CLIENTE/

│ ├── cliente.py # Cliente gRPC 

│ ├── cliente_pb2.py # Generado por protoc 

│ ├── cliente_pb2_grpc.py # Generado por protoc 

│ ├── cliente.proto # Definición del servicio gRPC 

├── SERVIDOR/ 

│ ├── servidor_pb2.py # Generado por protoc 

│ ├── servidor_pb2_grpc.py # Generado por protoc

│ ├── server.py # Servidor gRPC 

│ ├── servidor.proto # Definición del servicio gRPC 

├── README.md # Documentación


# 🚀 Cómo Generar los Archivos de gRPC
Después de definir `servidor.proto` y `cliente.proto`, genera los archivos necesarios en la respectiva
consola de cada uno con:

## Para cliente.proto
- python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. cliente.proto

## Para servidor.proto
- python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. servidor.proto


Esto creará:
- `cliente_pb2.py`
- `cliente_pb2_grpc.py`
- `servidor_pb2.py`
- `servidor_pb2_grpc.py`

# 🛠 Cómo Ejecutar el Proyecto

## 1 Iniciar el Servidor
Ejecuta el servidor en una terminal:

- python server.py

## 2️ Ejecutar el Cliente
En otra terminal, inicia el cliente:

python client.py


El cliente pedirá:
- Nombre y teléfono para registrarse.
- Consultará los tipos de servicio disponibles.
- Permitirá ingresar coordenadas para solicitar un taxi.

El servidor mostrará los registros de usuario en su consola.

# 🤝 Prueba en Red con Dos Computadoras
Si quieres probarlo en dos máquinas diferentes**:
1. Obtén la IP del servidor (`ipconfig` en Windows o `ifconfig` en Linux/macOS).
2. Modifica el cliente para conectarse a esa IP en `client.py`:
   python
        channel = grpc.insecure_channel("192.168.X.X:50051")  # Reemplaza con la IP real
   
3. Ejecuta el servidor en una máquina y el cliente en otra.
