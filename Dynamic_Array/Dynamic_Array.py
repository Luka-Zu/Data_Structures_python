import ctypes # this library provides C compatible data types, and allows calling functions in DLLs or shared libraries.

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

    def __len__(self):
        """
        Returns number of elements in D-Array
        """
        return self.n
    
    def __getitem__(self,k):
        """
        Returns element at index K
        """

        if not 0 <= k < self.n:
            # check if k is not in bounds of array 
            return IndexError("Index is out of bounds! ")
        
        return self.array[k] # returns an element

    def append(self,element):
        """
        Add element to the end of the array
        """
        pass
    
    def make_array(self, new_capacity):
        """
        Creates new array with diffrent capacity
        """
        return (new_capacity * ctypes.py_object)()


a = Dynamic_Array()

