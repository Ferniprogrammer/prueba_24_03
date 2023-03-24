class cuenta_estandard:
    def __init__(self, nombre, saldo, id_cuenta, fecha_apertura, num_cuenta):
        self.nombre = nombre
        self.saldo = saldo
        self.id_cuenta = id_cuenta
        self.fecha_apertura = fecha_apertura
        self.num_cuenta = num_cuenta
    
    def retirar(saldo, cantidad_a_retirar):
        if saldo > cantidad_a_retirar:
            saldo -= cantidad_a_retirar
            print("Retiro exitoso")
        else:
            print("Saldo insuficiente")
    
    def depositar(saldo, cantidad_a_depositar):
        saldo += cantidad_a_depositar
        print("Deposito exitoso")
    
    def consultar_saldo(saldo):
        print("Su saldo es de: ", saldo)
        
    def transferencia(saldo, cantidad_a_transferir, saldo_destino):
        if saldo > cantidad_a_transferir:
            saldo -= cantidad_a_transferir
            saldo_destino += cantidad_a_transferir
            print("Transferencia exitosa")
        else:
            print("Saldo insuficiente")

class cuenta_fija(cuenta_estandard):
    def __init__(self, nombre, saldo, id_cuenta, fecha_apertura, num_cuenta, fecha_vencimiento):
        super().__init__(nombre, saldo, id_cuenta, fecha_apertura, num_cuenta)
        self.fecha_vencimiento = fecha_vencimiento   

    def consultar_saldo_fijo(saldo):
        print("Su saldo es de: ", saldo)
    
    def retirar_fijo(saldo, cantidad_a_retirar):
        cantidad_a_retirar = cantidad_a_retirar + 0.05 * cantidad_a_retirar
        if saldo > cantidad_a_retirar:
            saldo -= cantidad_a_retirar
            print("Retiro exitoso")
        else:
            print("Saldo insuficiente")
            
    def depositar_fijp(saldo, cantidad_a_depositar):
         saldo += cantidad_a_depositar
         print("Deposito exitoso")
         
    def transferencia_fijo(saldo, cantidad_a_transferir, saldo_destino):
        importe = 0.05 * cantidad_a_transferir
        if saldo > cantidad_a_transferir + importe:
            saldo -= (cantidad_a_transferir + importe)
            saldo_destino += cantidad_a_transferir
            print("Transferencia exitosa")
        else:
            print("Saldo insuficiente")
            
class cuenta_VIP(cuenta_estandard):
    def __init__(self, nombre, saldo, id_cuenta, fecha_apertura, num_cuenta, negativo):
        super().__init__(nombre, saldo, id_cuenta, fecha_apertura, num_cuenta)
        self.negativo = negativo
          
    def consultar_saldo_VIP(saldo):
        print("Su saldo es de: ", saldo)
    
    def retirar_VIP(saldo, cantidad_a_retirar, negativo):
        if saldo + (-1 * negativo) > cantidad_a_retirar :
            saldo -= cantidad_a_retirar
            print("Retiro exitoso")
        else:
            print("Saldo insuficiente")
            
    def depositar_VIP(saldo, cantidad_a_depositar):
         saldo += cantidad_a_depositar
         print("Deposito exitoso")
         
    def transferencia_VIP(saldo, cantidad_a_transferir, saldo_destino, negativo):
        if saldo + (-1 * negativo) > cantidad_a_transferir:
            saldo -= cantidad_a_transferir
            saldo_destino += cantidad_a_transferir
            print("Transferencia exitosa")
        else:
            print("Saldo insuficiente")
         

    
        