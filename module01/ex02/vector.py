class Vector() :
    def __init__(self,values) :
        if not (
            isinstance(values, list) 
            and all(isinstance(elem, list) and all(isinstance(x, float) for x in elem) for elem in values)
        ):
            if isinstance(values, int) :
                self.values = [[float(i)] for i in range(values)]
                self.shape = (values, 1)
                return 
            elif isinstance(values, tuple) :
                if values[1] < values[0] :
                    raise NameError(f"Initialization with range can't have bound 1 superior as bound 2")
                self.values = [[float(i)] for i in range(values[0], values[1])]
                self.shape = (values[1] - values[0], 1)
                return
            else :
                raise TypeError("values is not a list or is not a list of list or is stocking other types than float")
        self.values = values
        self.shape = (len(values), len(values[0]))

    def dot(self, vector) :
        scalar_mult = 0
        for elem1, elem2 in zip(self.values, vector.values) :
            for x1,x2 in zip(elem1, elem2) :
                scalar_mult += x1*x2
        return scalar_mult
    
    def T(self) :
        temp = Vector([row[:] for row in self.values])
        if(temp.shape[1] == 1) :
            temp.values = [[row[0] for row in self.values]]
        else :
            temp.values = [[x] for x in self.values[0]]
        temp.shape = (temp.shape[1], temp.shape[0])
        return temp
    
    def __add__(self, other) :
        if self.shape == other.shape :
            temp = Vector([row[:] for row in self.values])
            for i, elem in enumerate(temp.values) :
                for j, x in enumerate(elem) :
                    temp.values[i][j] += other.values[i][j] 
            return temp
        return None
        
    def __sub__(self, other) :
        if self.shape == other.shape :
            temp = Vector([row[:] for row in self.values])
            for i, elem in enumerate(temp.values) :
                for j, x in enumerate(elem) :
                    temp.values[i][j] -= other.values[i][j] 
            return temp
        return None

    def __mul__(self, other) :
        if isinstance(other, (int, float)) :
            return (Vector([[x * other for x in elem] for elem in self.values]))
        return None

    def __rmul__(self, other) :
        if isinstance(other, (int, float)) :
            return (Vector([[x * other for x in elem] for elem in self.values]))
        return None

    def __truediv__(self, other) :
        if isinstance(other, (int, float)) :
            if other == 0 :
                raise ZeroDivisionError(f"division by zero")
            return (Vector([[x / other for x in elem] for elem in self.values]))
        return None

    def __rtruediv__(self, other) :
        raise NotImplementedError(f"Division of a scalar by a Vector is not defined here.")

    def __str__(self) :
        return (f"Vector({self.values})")

    def __repr__(self) :
        return (f"Vector({self.values})")
