import grpc
import cliente_pb2
import cliente_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = cliente_pb2_grpc.MyUberServiceStub(channel)

    #Ingresar datos del usuario desde la consola
    name = input("Ingrese su nombre: ")
    phone = input("Ingrese su número de teléfono: ")

    response = stub.RegisterUser(cliente_pb2.UserRequest(name=name, phone=phone))
    print(response.message)

    # Mostrar los tipos de servicio disponibles
    print("\n Tipos de servicio disponibles:")
    services = stub.GetServiceTypes(cliente_pb2.Empty())
    for service in services.services:
        print(f"- {service.type}: {service.cost} pesos/hora ({service.description})")

    #Ingresar coordenadas para pedir un taxi
    x = int(input("\nIngrese su coordenada X (0-9): "))
    y = int(input("Ingrese su coordenada Y (0-9): "))

    taxi_response = stub.RequestTaxi(cliente_pb2.TaxiRequest(x=x, y=y))
    print(f"\n Taxi asignado: {taxi_response.plate}")

if __name__ == "__main__":
    run()
