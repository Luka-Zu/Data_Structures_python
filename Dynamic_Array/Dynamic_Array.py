import ctypes

class Dynamic_Array:
    """
        data-structure which is similar to regular array,
        but difference is that its size can be dynamically modified
        at run-time.
    """
    def __init__(self):
        self.n = 0 # actual number of elements (at the creation of d. array it is 0)
        self.capacity  = 1 # Default capacity 
        self.array = self.make_array(self.capacity)
    
    def make_array(self, new_capacity):
        """
        Creates new array with diffrent capacity
        """
        return (new_capacity * ctypes.py_object)()


a = Dynamic_Array()

