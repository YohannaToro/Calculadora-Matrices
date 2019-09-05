from calculadora import CalculadoraBasica

def suma_matrices(m1,m2):
    matriz=[[() for i in range(len(m1))] for j in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            matriz[i][j]=CalculadoraBasica.suma_complejos(m1[i][j],m2[i][j])        
    return matriz
def inversa_matrices():
    return 0
def multiplicacion_escalar_matrices(c1,m1):
    matriz=[[() for i in range(len(m1[0]))] for j in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            matriz[i][j]=CalculadoraBasica.producto_complejos(c1,m1[i][j])        
    return matriz
def transpuesta(m1):
    matriz=[[() for i in range(len(m1))] for j in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            matriz[i][j]=m1[j][i]        
    return matriz
  
def matriz_conjugada(m1):
    for i in range(len(m1)):
        for j in range(len(m1)):
            m1[i][j]=conjugado_complejos(m1[i][j])       
    return m1
def matriz_adjunt(m1):
    return matriz_conjugad(transpuesta(m1))
def multiplicacion_matrices(x,y):
    matriz=[[() for i in range(max(len(x[0]),len(y[0])))] for j in range(max(len(x),len(y)))]
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(Y)):
                matriz[i][j] += producto_complejos(x[i][k],y[k][j])
    return matriz
def matriz_identidad(m1):
    matriz=[[() for i in range(len(m1))] for j in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            if i==j:matriz[i][j]=(1,0)
            else: matriz[i][j]=(0,0)
    return matriz
def matriz_unitaria(m):
    return multiplicacion_matrices(matriz_adjunt(m),m)==matriz_identidad(len(m))
def matriz_hermiltan(m):
    return (m==adjunta(m))
def accion_matriz():
    
    
    return 0
def norma_matrices():
    return 0
def distancia_entre_matrices():
    return 0


def producto_tensor():
    return 0
