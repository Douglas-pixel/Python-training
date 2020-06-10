Iva = lambda cantidad = 15, aduana = 2.5 : cantidad * 0.13 + cantidad +aduana
def Pistones(funcion):
    def extra(*args, **kwargs):
        print("Mugiwara")
        pre_resultado = funcion(*args, **kwargs)
        return pre_resultado
    return extra
@Pistones
def Impuesto(dinero):
    return dinero * 1.13
resultado =Impuesto(100)
print(resultado)
