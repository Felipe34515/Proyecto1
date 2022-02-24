import string

texto = "ejemplo.txt"
with open(texto) as f:
    content = f.read().replace('\n', ' ')
        
print(content)
print(type(content))


def CrearLista (content):
    lista = content.split(" ")
    return lista

ListaTexto = CrearLista(content)
print(ListaTexto)


def comprobaciónParentesis (content):
    if type(content) is str:
        lista = CrearLista(content)
    else:
        Lista = content
    Izquierdo = 0
    derecho = 0
    for palabra in lista:
        listaPalabra = palabra.strip()
        for caracter in listaPalabra:
            if caracter == "(":
                Izquierdo += 1
        for caracter in listaPalabra:
            if caracter == ")":
                derecho += 1
    if Izquierdo == derecho:
        rta = True
    else:
        rta = False
    return rta

comprobacion = comprobaciónParentesis(content)
print (comprobacion)


def CrearTokens ():
    
    move_face = [":north",":south",":west",":east"]
    run_dirs = [":left",":right",":around","front","back"]
    pick = ["Balloons","Chips"]
    variable = []

    token = {
        "(": 1,
        ")": 2,
        "defvar":3,
        "name" : 4,
        "move": 5,
        "turn": 6,
        "face": 7,
        "pick":8,
        "put": 9,
        "move-dir":10,
        "run-dirs":11,
        "move-face":12,
        "skip":13,
        "if":14,
        "loop":15,
        "repeat":16,
        "defun":17,
        "facing-p":18,
        "can-put-p":19,
        "can-pick-p":20,
        "can-move-p":21,
        "not": 24,
        "rotate": 25,
        "Balloons": 26,
        "Chips":27,
    }