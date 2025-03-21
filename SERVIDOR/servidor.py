import grpc
from concurrent import futures
import servidor_pb2
import servidor_pb2_grpc

class MyUberService(servidor_pb2_grpc.MyUberServiceServicer):
    taxis = {
        (1, 1): "XXC23",
        (5, 4): "XCV33",
        (6, 9): "GHJ45",
        (3, 8): "RR167",
        (4, 4): "GGT55",
        (2, 3): "HHW33"
    }
    
    usuarios_registrados = []  # Lista para almacenar usuarios

    def RegisterUser(self, request, context):
        # Guardar usuario en la lista
        self.usuarios_registrados.append({"name": request.name, "phone": request.phone})

        # Mostrar en la consola del servidor
        print(f"\nNuevo usuario registrado:")
        print(f"   Nombre: {request.name}")
        print(f"   Teléfono: {request.phone}")
        print(f"   Total de usuarios registrados: {len(self.usuarios_registrados)}")

        return servidor_pb2.RegisterResponse(success=True, message="Usuario registrado con éxito.")


    def GetServiceTypes(self, request, context):
        services = [
            servidor_pb2.Service(type="Normal", cost=50000, description="Taxis amarillos"),
            servidor_pb2.Service(type="Express", cost=70000, description="Taxis más amplios y cómodos."),
            servidor_pb2.Service(type="Excursión", cost=120000, description="Te llevan a cualquier lugar y te esperan."),
        ]
        return servidor_pb2.ServiceList(services=services)

    def RequestTaxi(self, request, context):
        nearest_taxi = min(self.taxis, key=lambda t: abs(t[0] - request.x) + abs(t[1] - request.y))
        plate = self.taxis.pop(nearest_taxi)  # Asignar y eliminar taxi
        return servidor_pb2.TaxiResponse(plate=plate)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servidor_pb2_grpc.add_MyUberServiceServicer_to_server(MyUberService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
