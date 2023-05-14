class cliente(): ## clientes empresa
    id = int
    nombre = str
    rut = str
    id_pedidos = []
    credito_consumido = int
    cupo_Credito = int
    id_vendedor = str

    def __init__(self, id, nombre, rut, cupo, id_vendedor):
        self.id = id
        self.nombre = nombre
        self.rut = rut
        self.id_pedidos = []
        self.credito_consumido = 0 
        self.cupo_Credito = cupo
        self.id_vendedor = id_vendedor

    def calcular_cupo_disponible(self):
        return self.cupo_Credito - self.credito_consumido
    
    def aumentarCupo(self, cupo):
        self.cupo_Credito += cupo

    def get_cupo_credito(self):
        return self.cupo_Credito

## Crear clientes

def cargarClientes():
    cliente1 = cliente(332, 'Kevin Fernandez', '76543210-3', 100000 , 1)
    cliente2 = cliente(333, 'Colegio Contigo-Aprendo', '78540102-6', 10000000 , 1)
    cliente3 = cliente(334, 'Guaton Salinas', '72554174-k', 500000 , 1)
    cliente4 = cliente(335, 'Lapiz Lopez', '77101205-3', 2000000 , 1)
    cliente5 = cliente(336, 'Libreria Nacional', '76893222-5', 3000000 , 1)

    return [cliente1, cliente2, cliente3, cliente4, cliente5]