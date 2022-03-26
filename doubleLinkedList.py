import math
class DoubleLinkedList:
    #Creamos la clase nodo anidada en la clase doubleLinkedList
    class Node:
        #Creamos el método inicializador a la clase nodo
        def __init__(self, value):
            self.value = value
            self.next_node = None
            self.previous_node = None
    #Creamos el método inicializador de la clase DoubleLinkedList
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    #Método para imprimir la lista doblemente enlazada
    def show_double_linked_list(self):
        #Lista es la almacenara los nodos de la lista dblemente enlazada
        array_double_linked_list = []
        current_node = self.head
        while(current_node != None):
            #únicamente almacenamos en la lista el valor del nodo
            array_double_linked_list.append(current_node.value)
            current_node = current_node.next_node
        print(array_double_linked_list)
    
    #Método para añadir nodos al inicio de la lista
    def prepend_node(self, value):
        #Al nuevo nodo le asignamos la estructura real de la clase Node
        new_node = self.Node(value)
        #Validamos si no hay cabeza ni cola en la lista
        if self.head == None and self.tail == None:
            #La cabeza toma el valor del nuevo nodo
            self.head = new_node
            #La cola toma el valor que tiene la cabeza
            self.tail =  self.head
        else:
            #El enlace anterior de la actual cabeza conecta con el nuevo nodo
            self.head.previous_node = new_node
            new_node.next_node = self.head
            self.head = new_node
        self.length += 1

    def append_node(self,value):
        new_node = self.Node(value)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail =  self.head
        else:
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
            self.tail = new_node
        self.length += 1
    
    #Eliminar el primer nodo de la lista
    def shift_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        elif self.head != None:
            #El nodo a eliminar es la cabeza
            remove_node = self.head
            #La nueva cabeza será el nodo siguiente a la antigua cabeza
            self.head = remove_node.next_node
            #El enlace siguiente de la antigua cabeza apunta a None
            remove_node.next_node= None
            #El enlace anterior de la cabeza actual apunta a None
            self.head.previous_node = None
            print(f'El nodo eliminado ha sido: {remove_node.value}')
        self.length -=1
    
    #Eliminar el último nodo de la lista
    def pop_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            #El nodo a eliminar será la cola
            remove_node = self.tail
            #La nueva cola pasa a ser el nodo previo de la cola antigua
            self.tail = remove_node.previous_node
            #La cola la desvinculamos del nodo que era ela cola antigua
            self.tail.next_node = None
            remove_node.previous_node = None
            print(f'El nodo eliminado ha sido: {remove_node.value}')
        self.length -=1
    
    #Método para obtener el valor de un nodo en determinada posición
    def get_node(self, index):
        if(type(index)== str):
            return print("se esperaba un valor numérico")
        self.none_in_list()
        if(index == self.length):
            return self.tail
        elif(index == 1):
            return self.head
        elif (index > self.length or index < 1):
            print('Fuera del rango')
        elif not (index == self.length or index == 1):
            #Búsqueda rápida del nodo
            middle_index = int(self.length/2)
            if(index <= middle_index):
                current_node = self.head
                count_node = 1
                while(count_node != index):
                    current_node = current_node.next_node
                    count_node += 1
                return current_node
            else:
                current_node = self.tail
                count_node = self.length 
                while(count_node != index):
                    current_node = current_node.previous_node
                    count_node -= 1
                return current_node
        else:
            return None
    #actualizar el valor al cuadrado del nodo anterior 
    def none_in_list(self):
           if(self.head== None or self.tail==None):
                return print("la lista esta vacia") 
              
    def update(self,index):
        self.none_in_list()
        current_node=self.get_node(index)
        after_node=current_node.next_node
        valor=current_node.value
        if (type(valor) == str):
            return print("se esperaba un valor numérico")
        elif (index==0):
            return print("no hay nada mas allá de los límites")
        elif(index == self.length):
            return print("no hay nada mas alla de los límites")
        
        
        else:
            new_node=self.Node(math.pow(valor,2))
            new_node.next_node=after_node
            new_node.previous_node=current_node
            current_node.next_node=new_node
            after_node.previous_node=new_node
            
    
    def insert(self,index,value):
       
        current_node=self.get_node(index)
        valor=self.get_node(index).value
        before_node=self.get_node(index).previous_node
        new_node=self.Node(value)
        self.none_in_list()
        if(type(value) == str):
            return print ("no es un valor numérico")
        print (f"valor del siguiente {valor}")
        print (f"valor ingresado {value}")
        print (f"modulo {value % valor}")
        print (f"division {value / valor}")
        if(value%valor == 0):
            new_node.next_node=current_node
            new_node.previous_node=before_node
            before_node.next_node=new_node
            current_node.previous_node=new_node
        
            #return print ("no es multiplo del siguiente")
        self.length += 1    
    
    def shift_by_index(self,index):
        self.none_in_list()
        current_node=self.get_node(index)
        before_node=current_node.previous_node
        before_node.next_node=current_node.next_node
        current_node.next_node=None
        current_node.previous_node=None
        return print (current_node.value)
    
    def square_root(self):
        #after_node=current_node.next_node
        #before_node=current_node.previous_node
        if self.head == None:
            return print("La lista esta vacia")
            
        else:
            current_node=self.head
            while current_node != None:
                valor= (math.sqrt(current_node.value))
                print(valor)
                current_node.value=valor
                current_node=current_node.next_node
            
            
          
    
    def reverse(self):
        if self.head == None:
            return print("la lista está vacía")
        else:     
            current_node = self.head
            after_node = current_node.next_node
            current_node.next_node = None
            current_node.previous_node = after_node
            while after_node != None:
                after_node.previous_node = after_node.next_node
                after_node.next_node = current_node
                current_node = after_node
                after_node = after_node.previous_node
            self.head = current_node  
        self.square_root()