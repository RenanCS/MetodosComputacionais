
import math
# [-50; +80]

def f(x):
    return ((math.pow(x,3)) - (5*math.pow(x,2)) + (17*x) + 21)
    #return math.pow(x,4) - 115*math.pow(x,3) + 1.575*math.pow(x,2) - 7.625*x + 12.500

def falsaposicao(a,b,fa,fb) :
    #return (a-(b-a) * fa)/ (fb - fa)
    return ((a * fb)  - (b * fa)) / (fb - fa)   

a=-1
b=0
i = 0

while(i < 10):
    print("iteracao = ", i)
    print("a = ", a)
    print("b= ", b)
    
    fa = f(a)
    print("P(a) - = ", fa)
    fb = f(b)
    print("P(b) + = ", fb)
    
    xa = a
    x = falsaposicao(a,b,fa,fb)
    er= abs((x - xa)/x)
    xs = f(x)
    
    #qual sub intervalo a raiz se encontra
    print("fa*fb < 0 =" , fa*fb)  
    print("Falsa Posicao   xs=", x)
    print("Falsa Posicao   F(xs)=", xs)
    print("Erro Relativo   ER=", er)
    print("\n")
    if(xs > 0):
        b = x
    elif(xs < 0):
        a = x
    else:
        break;
     
    i = i + 1
    
    


