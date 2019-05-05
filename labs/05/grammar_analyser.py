import sys

def main():
    filePath = sys.argv[1]
    dicc = {}
    fileCFG = open(filePath, 'r')
    for line in fileCFG:
        line = cleanLine(line)
        #Definiendo producciones de simbolos
        dicc[line[0]] = {
            'producciones': separarProducciones(line[1]),
            'symbolProd': line[1],
            'notUseless': False,
            'terminal': False
        }
    fileCFG.close()
    dicc = validarProducciones(dicc)
    dicc['S']['notUseless'] = True
    dicc['S']['terminal'] = True
    writeFile(dicc)

#Revisando si es terminal o alcanzable
def validarProducciones(dicc):
    values = {}
    for x, y in dicc.items():
        print('producciones from ', x)
        for prod in y['producciones']:
                #Cambiando bandera a true si el simbolo es alcanzable
            if symboloNoTerminal(prod):
                dicc[prod]['notUseless'] = True
                print(prod)
                #Cambiando bandera a true si el simbolo es terminal
            elif simboloTerminal(prod):
                dicc[x]['terminal'] = True
                print(prod)
                #Revisa si es una produccion con un simbolo alcanzable y un simbolo terminal 
            else:
                values = terminalNoTerminal(prod)
                for value in values['notUseless']:
                    dicc[value]['notUseless'] = True
    
    return dicc

#Genera el archivo con el cfg
def writeFile(dicc):
    f = open("generatedCFG.txt", "w")
    for x, y in dicc.items():
        if y['notUseless'] and y['terminal']:
            f.write('' + x + ' - ' + y['symbolProd'] + '\n')

#Se define que es un simbolo terminal
def simboloTerminal(prod):
    if(len(prod) < 2):
        return prod.islower()
    else:
        minuscula = True
        for char in prod:
            if not (char.islower()):
                minuscula = False
        return minuscula

#Se define que es un simbolo no terminal
def terminalNoTerminal(prod):
    values = {
        'notUseless': []
    }
    for char in prod:
        if not (char.islower()):
            values['notUseless'].append(char)
    return values

def symboloNoTerminal(prod):
    if(len(prod) < 2):
        return not(prod.islower())
    return False
            
#Se separan las producciones por |
def separarProducciones(symbolProd):
    producciones = symbolProd.split('|')
    return producciones

def cleanLine(line):
    line = line.split('->')
    line = line.replace(' ', '')
    line = line.replace('\n', '')
    return line

if __name__ == "__main__": main()