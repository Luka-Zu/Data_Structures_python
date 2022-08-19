import ctypes # this library provides C compatible data types, and allows calling functions in DLLs or shared libraries.

class Dynamic_Array:
    """
        data-structure which is similar to regular array,
        but difference is that its size can be dynamically modified
        at run-time.
        It is done in O(N)
    """
    def __init__(self):
        self.n = 0 # actual number of elements (at the creation of d. array it is 0)
        self.capacity  = 1 # Default capacity 
        self.array = self.make_array(self.capacity)

    def __len__(self):
        """
            Returns number of elements in D-Array
            It is done in O(1)
        """
        return self.n
    
    def __getitem__(self,k):
        """
            Returns element at index K
            It is done in O(1)
        """

        if not 0 <= k < self.n:
            # check if k is not in bounds of array 
            return IndexError("Index is out of bounds! ")
        
        return self.array[k] # returns an element

    def append(self,element):
        """
            Add element to the end of the array
            It is done in amortized O(1)
        """
        if self.n == self.capacity:
            # we need to change capacity if it reached it's limit
            self._resize(2 * self.capacity)
        
        self.array[self.n] = element # Set the value of the last index to element
        self.n+=1 # and change size of array
    
    def insertAt(self,item,index):
        """
            This function inserts at specific index
            It is done in O(N)
        """
        if index < 0 or index > self.n:
            raise Exception("Enter correct index ")
        
        if self.n == self.capacity: # change capacity if neccesary
            self._resize(2*self.capacity)
        
        for i in range(self.n-1, index-1, -1):
            self.array[i+1] = self.array[i] # shift every existing value from range [index:n] by one 
        
        self.array[index] = item
        self.n += 1

        

        

    def _resize(self, new_capacity):
        """
            Function to resize array
            and copy all previous values in it 
            It is done in O(N)
        """
        new_array = self.make_array(new_capacity)

        for k in range(self.n):
            new_array[k] = self.array[k] # store all existing values in new_array
        
        self.array = new_array # change array to new_array 
        self.capacity = new_capacity # reset the capacity (usualy its *2 or /2)
        
    
    def make_array(self, new_capacity):
        """
            Creates new array with diffrent capacity
            It is done in O(N)
        """
        return (new_capacity * ctypes.py_object)()


    def delete(self):
        """
            This method deletes element from the end of array
            It is done in O(1)
        """

        if self.n == 0:
            raise Exception("There is no element left to delete! ")
        
        self.array[self.n-1] = None # in reality this is not even neccasary as we change n to n-1 and cant access this index at all
        self.n -= 1  # decrement n

    def removeAt(self,index):
        """
            This element deletes element from specified index
            It is done in O(n)
        """
        
        # check for incorrect index values
        if index < 0 or index > self.n: 
            raise Exception("Enter correct index! ")
        
        if self.n == 0: 
            raise Exception("There is no element left to delete! ")
        
        if index==self.n-1:
            self.delete()
            return  
        
        for i in range(index,self.n-1):
            self.array[i]=self.array[i+1]   # Shift every value in index [index:n] on left by one
             
             
             
        self.array[self.n-1]=0
        self.n-=1
        
