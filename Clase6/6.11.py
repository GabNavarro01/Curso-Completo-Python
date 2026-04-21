import fileparse
import informe_funciones

camion = fileparse.parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
lista_precios = fileparse.parse_csv('../Data/precios.csv', types = [str, float], has_headers = False)
precios = dict(lista_precios)

informe  = informe_funciones.hacer_informe(camion, precios)
informe_funciones.imprimir_informe(informe)

