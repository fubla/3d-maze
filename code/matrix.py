from vector import *


class Matrix4x4(object):    #includes definition of matrices and matrix algebra
    
    def __init__(self, a11, a12, a13, a14, a21, a22, a23, a24, a31, a32, a33, a34, 
                 a41, a42, a43, a44):
        
        self.a11 = a11
        self.a12 = a12
        self.a13 = a13
        self.a14 = a14
        
        self.a21 = a21
        self.a22 = a22
        self.a23 = a23
        self.a24 = a24
        
        self.a31 = a31
        self.a32 = a32
        self.a33 = a33
        self.a34 = a34
        
        self.a41 = a41
        self.a42 = a42
        self.a43 = a43
        self.a44 = a44
        
    
    def __str__(self): #string representation of matrices
        
        return '|'+ str(self.a11)+' '+str(self.a12)+' '+str(self.a13)+' '+str(self.a14)+ '|\n'+ \
                '|'+ str(self.a21)+' '+str(self.a22)+' '+str(self.a23)+' '+str(self.a24)+ '|\n'+ \
                '|'+ str(self.a31)+' '+str(self.a32)+' '+str(self.a33)+' '+str(self.a34)+ '|\n'+ \
                '|'+ str(self.a41)+' '+str(self.a42)+' '+str(self.a43)+' '+str(self.a44)+ '|\n' 
        
        
    def __mul__(self, other):
        
        
        
        if isinstance(other, self.__class__):   #matrix-matrix multiplication
            
            c11 = self.a11*other.a11+self.a12*other.a21+self.a13*other.a31+self.a14*other.a41
            c12 = self.a11*other.a12+self.a12*other.a22+self.a13*other.a32+self.a14*other.a42
            c13 = self.a11*other.a13+self.a12*other.a23+self.a13*other.a33+self.a14*other.a43
            c14 = self.a11*other.a14+self.a12*other.a24+self.a13*other.a34+self.a14*other.a44
        
            c21 = self.a21*other.a11+self.a22*other.a21+self.a23*other.a31+self.a24*other.a41
            c22 = self.a21*other.a12+self.a22*other.a22+self.a23*other.a32+self.a24*other.a42
            c23 = self.a21*other.a13+self.a22*other.a23+self.a23*other.a33+self.a24*other.a43
            c24 = self.a21*other.a14+self.a22*other.a24+self.a23*other.a34+self.a24*other.a44
        
            c31 = self.a31*other.a11+self.a32*other.a21+self.a33*other.a31+self.a34*other.a41
            c32 = self.a31*other.a12+self.a32*other.a22+self.a33*other.a32+self.a34*other.a42
            c33 = self.a31*other.a13+self.a32*other.a23+self.a33*other.a33+self.a34*other.a43
            c34 = self.a31*other.a14+self.a32*other.a24+self.a33*other.a34+self.a34*other.a44
        
            c41 = self.a41*other.a11+self.a42*other.a21+self.a43*other.a31+self.a44*other.a41
            c42 = self.a41*other.a12+self.a42*other.a22+self.a43*other.a32+self.a44*other.a42
            c43 = self.a41*other.a13+self.a42*other.a23+self.a43*other.a33+self.a44*other.a43
            c44 = self.a41*other.a14+self.a42*other.a24+self.a43*other.a34+self.a44*other.a44
            
            return Matrix4x4(c11,c12,c13,c14,c21,c22,c23,c24,c31,c32,c33,c34,c41,c42,c43,c44)
    
        elif isinstance(other, Vector3D): #matrix-vector multiplication
            
            x = self.a11*other.x+self.a12*other.y+self.a13*other.z+self.a14*other.h
            y = self.a21*other.x+self.a22*other.y+self.a23*other.z+self.a24*other.h
            z = self.a31*other.x+self.a32*other.y+self.a33*other.z+self.a34*other.h
            h = 1
            
            return Vector3D(x, y, z)
       
        else: #invalid operands
            
            raise TypeError('Unsupported operand type(s) for *.')
            
            
            