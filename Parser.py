import Lexer as L




name = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

n = ["1","2","3","4","5","6","7","8","9","0"]

D = [":left",":right",":around"]

O = [":north",":south",":east",":west"]

D2 = [":front",":right",":left",":back"]

ListaPalabras = L.CrearLista(L.content)


listaComandos = []
listaComandos.append("(")
listaComandos.append(")")
listaComandos.append("defvar")
listaComandos.append("name")
listaComandos.append("move")
listaComandos.append("turn")
listaComandos.append("face")
listaComandos.append("put")
listaComandos.append("pick")
listaComandos.append("move-dir")
listaComandos.append("run-dirs")
listaComandos.append("move-face")
listaComandos.append("skip")
listaComandos.append("if")
listaComandos.append("loop")
listaComandos.append("repeat")
listaComandos.append("defun")
listaComandos.append("facing-p")
listaComandos.append("can-put-p")
listaComandos.append("can-pick-p")
listaComandos.append("can-move-p")
listaComandos.append("not")
listaComandos.append("rotate")


def eliminarParentesis(ListaPalabras: list)->list:
    nL1 = ListaPalabras.remove("(")
    nL2 = nL1.remove(")")
    return nL2

def comprobarDefvar (ListaPalabras: list)->bool:
    parentesis = L.comprobaciónParentesis(ListaPalabras)
    nuevoString = eliminarParentesis(ListaPalabras)
    condicion = False
    defVar = listaComandos(2)
    name = listaComandos(3)
    nCondicion = (n[0] or n[1] or n[2] or n[3] or n[4] or n[5] or n[6] or n[7] or n[8] or n[9])
    tamString = len(nuevoString)
    if (not (tamString == 3)):
        condicion = False
    elif (nuevoString(0) == defVar):
        if nuevoString(1) == name:
            if nuevoString(2) == nCondicion:
                condicion = True
    rta = False
    if (condicion and parentesis):
        rta = True 
    return rta

def comprobarnameVar (ListaPalabras: list)->bool:
    parentesis = L.comprobaciónParentesis(ListaPalabras)
    nuevoString = eliminarParentesis(ListaPalabras)
    condicion = False
    igual = "="
    name = listaComandos(3)
    nCondicion = (n[0] or n[1] or n[2] or n[3] or n[4] or n[5] or n[6] or n[7] or n[8] or n[9])
    tamString = len(nuevoString)
    if (not (tamString == 3)):
        condicion = False
    elif (nuevoString(0) == igual):
        if nuevoString(1) == name:
            if nuevoString(2) == nCondicion:
                condicion = True
    return (condicion and parentesis)


def comprobarMove (ListaPalabras: list)->bool:
    parentesis = L.comprobaciónParentesis(ListaPalabras)
    nuevoString = eliminarParentesis(ListaPalabras)
    condicion = False
    move = listaComandos(4)
    nCondicion = (n[0] or n[1] or n[2] or n[3] or n[4] or n[5] or n[6] or n[7] or n[8] or n[9])
    tamString = len(nuevoString)
    if (not (tamString == 2)):
        condicion = False
    elif (nuevoString(0) == move):
        if nuevoString(1) == nCondicion:
                condicion = True
    return (condicion and parentesis)


def comprobarTurn (ListaPalabras: list)->bool:
    parentesis = L.comprobaciónParentesis(ListaPalabras)
    nuevoString = eliminarParentesis(ListaPalabras)
    condicion = False
    turn = listaComandos(5)
    dCondicion = (D[0] or D[1] or D[2])
    tamString = len(nuevoString)
    if (not (tamString == 2)):
        condicion = False
    elif (nuevoString(0) == turn):
        if nuevoString(1) == dCondicion:
                condicion = True
    return (condicion and parentesis)

def comprobarFace (ListaPalabras: list)->bool:
    parentesis = L.comprobaciónParentesis(ListaPalabras)
    nuevoString = eliminarParentesis(ListaPalabras)
    condicion = False
    face = listaComandos(6)
    oCondicion = (O[0] or O[1] or O[2] or O[3])
    tamString = len(nuevoString)
    if (not (tamString == 2)):
        condicion = False
    elif (nuevoString(0) == face):
        if nuevoString(1) == oCondicion:
                condicion = True
    return (condicion and parentesis)

def comprobarPut (ListaPalabras: list)->bool:
    parentesis = L.comprobaciónParentesis(ListaPalabras)
    nuevoString = eliminarParentesis(ListaPalabras)
    condicion = False
    put = listaComandos(7)
    balloons = "Balloons"
    chips = "Chips"
    condicionalX = balloons or chips
    nCondicion = (n[0] or n[1] or n[2] or n[3] or n[4] or n[5] or n[6] or n[7] or n[8] or n[9])
    tamString = len(nuevoString)
    if (not (tamString == 3)):
        condicion = False
    elif (nuevoString(0) == put):
        if nuevoString(1) == condicionalX:
            if nuevoString(2) == nCondicion:
                condicion = True
    return (condicion and parentesis)

def comprobarPick (ListaPalabras: list)->bool:
    parentesis = L.comprobaciónParentesis(ListaPalabras)
    nuevoString = eliminarParentesis(ListaPalabras)
    condicion = False
    pick = listaComandos(8)
    balloons = "Balloons"
    chips = "Chips"
    condicionalX = balloons or chips
    nCondicion = (n[0] or n[1] or n[2] or n[3] or n[4] or n[5] or n[6] or n[7] or n[8] or n[9])
    tamString = len(nuevoString)
    if (not (tamString == 3)):
        condicion = False
    elif (nuevoString(0) == pick):
        if nuevoString(1) == condicionalX:
            if nuevoString(2) == nCondicion:
                condicion = True
    return (condicion and parentesis)

def comprobarMoveDir (ListaPalabras: list)->bool:
    parentesis = L.comprobaciónParentesis(L.content)
    nuevoString = eliminarParentesis(ListaPalabras)
    condicion = False
    moveDir = listaComandos(9)
    balloons = "Balloons"
    chips = "Chips"
    condicionalX = balloons or chips
    dCondicion = D2[0] or D2[1] or D2[2] or D2[3]
    tamString = len(nuevoString)
    if (not (tamString == 3)):
        condicion = False
    elif (nuevoString(0) == moveDir):
        if nuevoString(1) == condicionalX:
            if nuevoString(2) == dCondicion:
                condicion = True
    return (condicion and parentesis)

def comprobarRunDirs (ListaPalabras: list)->bool:
    parentesis = L.comprobaciónParentesis(L.content)
    nuevoString = eliminarParentesis(ListaPalabras)
    condicion = False
    runDir = listaComandos(10)
    dCondicion = D2[0] or D2[1] or D2[2] or D2[3]
    tamString = len(nuevoString)
    if (not (tamString == 2)):
        condicion = False
    elif (nuevoString(0) == runDir):
        if nuevoString(1) == dCondicion:
            condicion = True
    return (condicion and parentesis)

def comprobarMoveFace (ListaPalabras: list)->bool:
    parentesis = L.comprobaciónParentesis(L.content)
    nuevoString = eliminarParentesis(ListaPalabras)
    condicion = False
    moveFace = listaComandos(11)
    nCondicion = (n[0] or n[1] or n[2] or n[3] or n[4] or n[5] or n[6] or n[7] or n[8] or n[9])
    oCondicion = (O[0] or O[1] or O[2] or O[3])
    tamString = len(nuevoString)
    if (not (tamString == 3)):
        condicion = False
    elif (nuevoString(0) == moveFace):
        if nuevoString(1) == nCondicion:
            if nuevoString(2) == oCondicion:
                condicion = True
    return (condicion and parentesis)

def comprobarSkip (ListaPalabras: list)->bool:
    parentesis = L.comprobaciónParentesis(L.content)
    nuevoString = eliminarParentesis(ListaPalabras)
    condicion = False
    skip = listaComandos(12)
    tamString = len(nuevoString)
    if (not (tamString == 1)):
        condicion = False
    elif (nuevoString(0) == skip):
        condicion = True
    return (condicion and parentesis)

def comprobarFacing (ListaPalabras: list)->bool:
    parentesis = L.comprobaciónParentesis(L.content)
    nuevoString = eliminarParentesis(ListaPalabras)
    condicion = False
    facing = listaComandos[13]
    oCondicion = (O[0] or O[1] or O[2] or O[3])
    tamString = len(nuevoString)
    if (not (tamString == 2)):
        condicion = False
    elif (nuevoString(0) == facing):
        if (nuevoString(1) == oCondicion):
            condicion = True
    return (condicion and parentesis)

def comprobarCanPutP (ListaPalabras: list)->bool:
    parentesis = L.comprobaciónParentesis(L.content)
    nuevoString = eliminarParentesis(ListaPalabras)
    condicion = False
    canPutP = listaComandos(14)
    balloons = "Balloons"
    chips = "Chips"
    condicionalX = balloons or chips
    nCondicion = (n[0] or n[1] or n[2] or n[3] or n[4] or n[5] or n[6] or n[7] or n[8] or n[9])
    tamString = len(nuevoString)
    if (not (tamString == 3)):
        condicion = False
    elif (nuevoString(0) == canPutP):
        if (nuevoString(1) == condicionalX):
            if (nuevoString(2) == nCondicion):
                condicion = True
    return (condicion and parentesis)


def comprobarCanPickP (ListaPalabras: list)->bool:
    parentesis = L.comprobaciónParentesis(L.content)
    nuevoString = eliminarParentesis(ListaPalabras)
    condicion = False
    canPickP = listaComandos(15)
    balloons = "Balloons"
    chips = "Chips"
    condicionalX = balloons or chips
    nCondicion = (n[0] or n[1] or n[2] or n[3] or n[4] or n[5] or n[6] or n[7] or n[8] or n[9])
    tamString = len(nuevoString)
    if (not (tamString == 3)):
        condicion = False
    elif (nuevoString(0) == canPickP):
        if (nuevoString(1) == condicionalX):
            if (nuevoString(2) == nCondicion):
                condicion = True
    return (condicion and parentesis)

def comprobarCanMoveP (ListaPalabras: list)->bool:
    parentesis = L.comprobaciónParentesis(L.content)
    nuevoString = eliminarParentesis(ListaPalabras)
    condicion = False
    canMoveP = listaComandos(16)
    oCondicion = (O[0] or O[1] or O[2] or O[3])
    tamString = len(nuevoString)
    if (not (tamString == 2)):
        condicion = False
    elif (nuevoString(0) == canMoveP):
        if (nuevoString(1) == oCondicion):
            condicion = True
    return (condicion and parentesis)

def comprobarCondicion (ListaPalabras: list)->bool:
    facing = comprobarFacing(ListaPalabras)
    can_put = comprobarCanPutP(ListaPalabras)
    can_pick = comprobarCanPickP(ListaPalabras)
    can_move = comprobarCanMoveP(ListaPalabras)
    condicionales = facing or can_put or can_pick or can_move
    return condicionales

def comprobarNot (ListaPalabras: list)->bool:
    parentesis = L.comprobaciónParentesis(L.content)
    condicion = False
    nuevoString = eliminarParentesis(ListaPalabras)
    tamString = len(nuevoString)
    notInstruccion = listaComandos[17]
    if (tamString != 2):
        condicion = False
    else:
        cumpleCondicion = comprobarCondicion(nuevoString(1))
        if (ListaPalabras(0) == notInstruccion):
            if cumpleCondicion:
                condicion = True
    return(condicion and parentesis)

def comprobarBloques (ListaPalabras:list)->bool:
    defVar = comprobarDefvar(ListaPalabras)
    name = comprobarnameVar(ListaPalabras)
    move= comprobarMove(ListaPalabras)
    turn = comprobarTurn(ListaPalabras)
    face = comprobarFace(ListaPalabras)
    put = comprobarPut(ListaPalabras)
    pick = comprobarPick(ListaPalabras)
    moveDir = comprobarMoveDir(ListaPalabras)
    runDir = comprobarRunDirs(ListaPalabras)
    moveFace = comprobarMoveFace(ListaPalabras)
    skip = comprobarSkip(ListaPalabras)
    condicion = defVar or name or move or turn or face or put or pick or moveDir or runDir or moveFace or skip
    return condicion

bloques = comprobarBloques(ListaPalabras)
print(bloques)


def comprobarEstructuraCondicional(ListaPalabras: list)->bool:
    condicion = False
    parentesis = L.comprobaciónParentesis(L.content)
    nuevoString = eliminarParentesis(ListaPalabras)
    ifComando = "if"
    tamString = len(nuevoString)
    if (tamString != 4):
        condicion = False
    else:
        if nuevoString(0) == ifComando:
            if (comprobarCondicion(nuevoString(1)) or comprobarNot(nuevoString(1))):
                if (comprobarBloques(nuevoString(2)) and comprobarBloques(nuevoString(3))):
                    condicion = True
                return condicion and parentesis











    
    



















        







