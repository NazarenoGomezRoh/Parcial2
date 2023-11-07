"""Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
caracteres–;
c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
además un listado por nivel por nombre;
e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
f) Determina cuantos Pokémons hay de tipo eléctrico y acero. 2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar"""

from arbol_binario import BinaryTree

class MiArbol(BinaryTree):
    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        __inorden(self.root)

pokemon_data = [
    {"nombre": "Pikachu", "numero": 25, "tipo": "Electric"},
    {"nombre": "Bulbasaur", "numero": 1, "tipo": ["Grass", "Poison"]},
    {"nombre": "Charmander", "numero": 4, "tipo": ["Fire"]},
    {"nombre": "Squirtle", "numero": 7, "tipo": ["Water"]},
    {"nombre": "Jigglypuff", "numero": 39, "tipo": ["Normal", "Fairy"]},
    {"nombre": "Gengar", "numero": 94, "tipo": ["Ghost", "Poison"]},
    {'nombre': 'jolteon', 'numero': 6, 'tipo': 'Electric'},
    {'nombre': 'lycanroc', 'numero': 9, 'tipo': 'Rock'},
    {'nombre': 'tyrantrum', 'numero': 8, 'tipo': 'Metal'}  
]

arbol_de_nombre= MiArbol()
arbol_de_numero= MiArbol()
arbol_de_tipos= MiArbol()

for pokemon in pokemon_data:
    arbol_de_nombre.insert_node(pokemon['nombre'], {'numero': pokemon['numero'],'tipo': pokemon['tipo']})
    arbol_de_numero.insert_node(pokemon['numero'], {'nombre': pokemon['nombre'],'tipo': pokemon['tipo']})
    arbol_de_tipos.insert_node(str(pokemon['tipo']), {'numero': pokemon['numero'],'nombre': pokemon['nombre']})
    
print("b.datos del pokemon numero 25")
print(arbol_de_numero.search(25).other_values)

print ("--------------------------")

print('busqueda por proximidad "bul"')
print(arbol_de_nombre.search_by_coincidence('bul'))

print("c.")
#Ingresar el tipo a buscar, en este caso Rock
pos = arbol_de_tipos.search('Rock')
if pos:
    print('TIPOS POISON:', pos.other_values)
pos = arbol_de_tipos.search('Poison')
if pos:
    print('TIPOS FIRE:', pos.other_values)
    pos = arbol_de_tipos.search('Fire')
if pos:
    print('TIPOS WATER:', pos.other_values)
pos = arbol_de_tipos.search('Water')
if pos:
    print('TIPOS ELECTRIC:', pos.other_values)
print("-----------------------------------------------------------------------------------")

# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
# además un listado por nivel por nombre;
print("d. LISTADO ASCENDENTE POR NUMERO")
arbol_de_numero.inorden()
print("-----------------------------------------------------------------------------------")
print("LISTADO ASCENDENTE POR NOMBRE")
arbol_de_nombre.inorden()
print("-----------------------------------------------------------------------------------")
print("LISTADO POR NIVEL POR NIVEL")
arbol_de_nombre.by_level()
print("-----------------------------------------------------------------------------------")

# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
jolteon = arbol_de_nombre.search('jolteon')
print("INFORMACION ACERCA DE JOLTEON:", jolteon.other_values)
lycanroc = arbol_de_nombre.search('lycanroc')
print("INFORMACION ACERCA DE LYCANROC:", lycanroc.other_values)
tyrantrum = arbol_de_nombre.search('tyrantrum')
print("INFORMACION ACERCA DE TYRANTRUM:", tyrantrum.other_values)
print("-----------------------------------------------------------------------------------")

# f) Determina cuantos Pokémons hay de tipo eléctrico y acero. 
print("e.CANTIDAD DE POKEMONS TIPO ELECTRICO", arbol_de_tipos.contar('Electric'))
print("CANTIDAD DE POKEMONS TIPO ACERO", arbol_de_tipos.contar('Metal'))












    
    

