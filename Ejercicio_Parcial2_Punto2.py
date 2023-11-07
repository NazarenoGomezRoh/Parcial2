"""
algoritmos necesarios para resolver las siguientes tareas:
a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
cantidad de episodios en los que aparecieron juntos ambos personajes que se
relacionan;
b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
c) determinar cuál es el número máximo de episodio que comparten dos personajes
d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.
"""
from grafo import Grafo 
from lista import Lista as ListaArista
from cola import Cola
from pila import Pila
from heap_min import Heap


mi_grafo = Grafo(dirigido=False)



mi_grafo.insert_vertice ('Luke Skywalker')
mi_grafo.insert_vertice ('Han Solo')
mi_grafo.insert_vertice ('Princess Leia')
mi_grafo.insert_vertice ('Darth Vader')
mi_grafo.insert_vertice ('Yoda',)
mi_grafo.insert_vertice ('Obi-Wan Kenobi')
mi_grafo.insert_vertice ('Chewbacca')
mi_grafo.insert_vertice ('R2-D2')
mi_grafo.insert_vertice ('C-3PO')
mi_grafo.insert_vertice ('Boba Fett')
mi_grafo.insert_vertice ('BB-8')
mi_grafo.insert_vertice ('Kylo Ren')
mi_grafo.insert_vertice ('Rey')
   

mi_grafo.insert_arist('Chewbacca', 'R2-D2', 14)
mi_grafo.insert_arist('Kylo', 'Darth Vader', 3)
mi_grafo.insert_arist('Obi-Wan Kenobi', 'Luke Skywalker', 4)
mi_grafo.insert_arist('Luke Skywalker', 'Han Solo', 3)
mi_grafo.insert_arist('Darth Vader', 'Yoda', 4)
mi_grafo.insert_arist('Han Solo', 'Princess Leia', 2)
mi_grafo.insert_arist('Darth Vader', 'Obi-Wan Kenobi', 9)
mi_grafo.insert_arist('Boba Fett', 'BB-8', 6)
mi_grafo.insert_arist('Yoda', 'Luke Skywalker', 5)
mi_grafo.insert_arist('R2-D2', 'Luke Skywalker', 4)
mi_grafo.insert_arist('Han Solo', 'Kylo Ren', 3)
mi_grafo.insert_arist('Kylo Ren', 'Luke Skywalker', 8)
mi_grafo.insert_arist('Han Solo', 'Princess Leia', 3)
mi_grafo.insert_arist('BB-8', 'Rey', 3)
mi_grafo.insert_arist('BB-8', 'Luke Skywaler', 3)


#b)
bosque = mi_grafo.kruskal()
for arbol in bosque:
    print("---------------------------------------------------------------------------------")
    print('b.ARBOL DE EXPANSION MINIMA:')
    print(bosque)
    for nodo in arbol.split(';'):
        if 'Yoda' in nodo and '-' in nodo:
            print("Yoda aparece en el arbol de expansion minima, relacionado de la siguente manera:", nodo)



