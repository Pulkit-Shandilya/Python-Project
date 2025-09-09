class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        return NotImplemented
    
    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Example usage
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)
result = c1 + c2
print("Sum:", result)