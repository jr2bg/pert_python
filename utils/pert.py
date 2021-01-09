'''
Se usara POO, con nodos y aristas
Se va a considerar que los nodos tienen un 
- nombre
- descripción
- tiempo optimista
- tiempo pesimista
- tiempo más probable
- lista de nodos que apuntan a él (precedentes)

Se calculará
- tiempo pert
- camino crítico
- tiempo early
- tiempo late
'''
import datetime

class PERTNode:
  '''
  clase para el nodo PERT
  '''
  def __init__(self, name):
    '''
    constructor
    '''
    self.name = name
    self.t_e = 0
    self.t_l = 0
    self.h_nodo = 0
    self.fecha = None
    
    # edges que llegan
    self.inc = []
    # edges que salen
    self.out = []
    
  def addOutEdge(self, edge):
    '''
    método para agregar una edge saliente
    '''
    self.out.append(edge)
  
  
  def addIncEdge(self, edge):
    '''
    método para agregar una edge entrante
    '''
    self.inc.append(edge)
  
    
  def fTEarly(self, is_first = False):
    '''
    método para calcular el tiempo early
    '''
    if is_first:
      self.t_e = 0
      return
    
    # para cada arista que llega al nodo:
    #   tomamos el tiempo early del nodo del cual sale la arista +
    #   el tiempo PERT de la arista
    self.t_e = max([ed.n_sal.t_e + ed.t_pert for ed in self.inc])
  
  
  def fTLate(self, is_last = False):
    '''
    método para calcular el tiempo late
    '''
    if is_last:
      self.t_l = self.t_e
      return
    
    # para cada arista que sale del nodo:
    #   tomamos el tiempo late del nodo al cual entra la arista +
    #   el tiempo PERT de la arista
    self.t_l = max([ed.n_ent.t_l - ed.t_pert for ed in self.out])


  def printNode(self):
    '''
    método para imprimir información del nodin
    '''
    print("\n------ NODO %d -----"%(self.name))
    print("tiempo early:\t", self.t_e)
    print("tiempo late: \t", self.t_l)
    print("fecha:       \t", self.fecha)
    

class PERTEdge:
  '''
  clase para la arista PERT
  '''
  
  def __init__(self, name, to, tp, tn, n_sal, n_ent, prec={}, desc = None):
    '''
    constructor de los nodos pert
    
    n_sal -> nodo del cual sale
    n_ent -> nodo al que entra
    prec -> conjunto con nombres de instancias de nodos pert definidos previamente
    '''
    self.name = name
    self.desc = desc
    self.n_sal = n_sal
    self.n_ent = n_ent
    self.to = to
    self.tp = tp
    self.tn = tn
    self.prec = prec
    
    # tiempo PERT
    self.t_pert = (to + 4*tn + tp) / 6
    
    self.t_early = - float("inf")
    self.t_late = float("inf")
  
  
    
class PERTGraph:
  '''
  clase para el grafo PERT
  '''
  def __init__(self):
    '''
    constructor
    '''
    
    # lista de nodos
    self.nodes = []
    
    # lista de adyacencia, con llaves las instancias
    self.edges = {}
    
    # tamaño
    self.sz = 0
  
  def add_node(self, p_node):
    '''
    método para agregar un nodo al grafo PERT
    '''
    self.sz += 1
    # agregamos un nodin
    self.nodes.append(p_node)
    
  def add_edge(self, p_edge):
    '''
    método para agregar esges al grafo pert
    '''
    
    sal = p_edge.n_sal
    ent = p_edge.n_ent
    
    sal.addOutEdge(p_edge)
    ent.addIncEdge(p_edge)
    
    #self.edges[p_node] = []
    
    # anexamos sus correspondientes elementos en la lista de adyacencia
    #for incoming in p_node.prec:
      # en caso de no tener elementos precedentes, la lista es vacía
      #self.edges[incoming].append(p_node)
      # no debería haber error pues consideramos que se anexan secuencialmente
      
      
  def calculateTEarly(self):
    '''
    método para calcular el tiempo early de todos los elementos
    '''
    for i in range(self.sz):
      # condiciones sobre los tiempos early y late iniciales
      if i == 0:
        is_first = True
      else:
        is_first = False
      
      self.nodes[i].fTEarly(is_first)
  
      
  
  def calculateTLate(self):
    '''
    método para calcular el tiempo late de todos los elementos
    '''
    for i in range(self.sz):
      # condiciones sobre los tiempos early y late iniciales
      k = self.sz - i -1
      if k == self.sz -1:
        is_last = True
      else:
        is_last = False
      
      self.nodes[k].fTLate(is_last)
  
  def printAllNodes(self):
    '''
    método para imprimir todos los nodines
    '''
    for nodito in self.nodes:
      nodito.printNode()

