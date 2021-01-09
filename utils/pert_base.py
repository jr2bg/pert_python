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

class PERTEdge:
  '''
  clase para el nodo PERT
  '''
  
  def __init__(self, name, desc, to, tp, tn, prec={})
    '''
    constructor de los nodos pert
    
    prec -> conjunto con nombres de instancias de nodos pert definidos previamente
    '''
    self.name = name
    self.desc = desc
    self.to = to
    self.tp = tp
    self.tn = tn
    self.prec = prec
    
    # tiempo PERT
    self.t_pert = (to + 4*tn + tp) / 6
    
    self.t_early = - float("inf")
    self.t_late = float("inf")
  
  def fTEarly(self, is_first = False):
    '''
    método para calcular el tiempo early
    '''
    if is_first:
      self.t_early = 0
      return
    
    self.t_early = max([arista.t_early + arista.t_pert for arista in self.prec])
  
  def fTLate(self, is_last = False):
    '''
    método para calcular el tiempo late
    '''
    if is_last:
      self.t_late = self.t_early
      return
    
    self.t_late = 
    
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
    self.edges[p_node] = []
    
    # anexamos sus correspondientes elementos en la lista de adyacencia
    for incoming in p_node.prec:
      # en caso de no tener elementos precedentes, la lista es vacía
      self.edges[incoming].append(p_node)
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
      
      self.nodes[i].
  
      
    