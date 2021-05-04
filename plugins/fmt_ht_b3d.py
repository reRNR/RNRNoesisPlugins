from inc_noesis import *
import os
import noewin


def registerNoesisTypes():
    handle = noesis.register("Hard Truck 2 models", ".b3d")
    noesis.setHandlerTypeCheck(handle, b3dCheckType)
    noesis.setHandlerLoadModel(handle, b3dLoadModel)
            
    return 1


class B3DStream(NoeBitStream):
    def readStringFromBytes(self, dataLength):
        name = self.readString()
        self.seek(dataLength - 1 - len(name), NOESEEK_REL)
        
        return name 
        
    def readMatrix4x3(self):
        xAxis = (self.readFloat(), self.readFloat(), self.readFloat()) 
        yAxis = (self.readFloat(), self.readFloat(), self.readFloat()) 
        zAxis = (self.readFloat(), self.readFloat(), self.readFloat()) 
        pos = (self.readFloat(), self.readFloat(), self.readFloat()) 
        
        return (xAxis, yAxis, zAxis, pos)
   

class HTB3DModel():
    def __init__(self):
        pass


class HTB3DObject():
    def __init__(self):
        self.id = 0
        self.name = ""
        self.models = []
        
    def readHeader(self, reader):
        self.name = reader.readStringFromBytes(32)  
        self.id = reader.readUInt)()      

    def readChildObjects(self, reader):
        count = reader.readUint()
        for i in range(count):
            self.read(reader)
            
    def readBoundingSphere(self, reader):
        self.reader.seek(16, NOESEEK_REL) 
           
    def readObjectData(self, reader):
        if self.id == 0:
            reader.seek(44, NOESEEK_REL) 
        elif self.id == 1:        
            reader.seek(64, NOESEEK_REL) 
        elif self.id == 2:
            self.readBoundingSphere()        
            reader.seek(16, NOESEEK_REL)
            
            self.readChildObjects()            
        elif self.id == 3:    
            self.readBoundingSphere()  
            
            self.readChildObjects()
        elif self.id == 4:
            self.readBoundingSphere()
            reader.seek(64, NOESEEK_REL) 
            
            self.readChildObjects() 
        elif self.id == 5:        
            self.readBoundingSphere()
            reader.seek(32, NOESEEK_REL) 
            
            self.readChildObjects()           
        elif self.id == 6:  
            self.readBoundingSphere()
            reader.seek(64, NOESEEK_REL) 
            count = reader.readUint()
            reader.seek(12 * count, NOESEEK_REL) 
            
            self.readChildObjects() 
        elif self.id == 7: 
            self.readBoundingSphere()
            reader.seek(32, NOESEEK_REL)  
            count = reader.readUint()
            self.reader.seek(12 * count, NOESEEK_REL) 
            
            self.readChildObjects()             
        elif self.id == 8:  
            self.readBoundingSphere()        
            self.reader.seek(12, NOESEEK_REL) 
            count = reader.readUint()
            for i in range(count): 
                type = reader.readUint()
                reader.seek(12, NOESEEK_REL) 
                vcount = reader.readUint()
                for k in range(vcount):
                    if type == 3 or type == 131 or type == 2:
                        reader.seek(12, NOESEEK_REL)                      
                    elif type == 177:
                        reader.seek(8, NOESEEK_REL)
                    elif type == 48 or type = 51 or type == 176 or type = 179:
                        reader.seek(16, NOESEEK_REL)
                    elif type == 50 or type = 178:
                        reader.seek(24, NOESEEK_REL)
                    else :
                        reader.seek(4, NOESEEK_REL)                                   
        elif self.id == 9:  
            self.readBoundingSphere()         
            reader.seek(16, NOESEEK_REL) 
            
            self.readChildObjects()                          
        elif self.id == 10:  
            self.readBoundingSphere()         
            self.reader.seek(16, NOESEEK_REL) 
            
            self.readChildObjects() 
        elif self.id == 11: 
            self.readBoundingSphere()         
            reader.seek(32, NOESEEK_REL) 
            
            self.readChildObjects() 
        elif self.id == 12:  
            self.readBoundingSphere()         
            self.reader.seek(24, NOESEEK_REL) 
            
            self.readChildObjects() 
        elif self.id == 13:
            self.readBoundingSphere()         
            reader.seek(8, NOESEEK_REL) 
            count = reader.readUint()
            reader.seek(4*count, NOESEEK_REL)            
            self.readChildObjects()         
        elif self.id == 14:              
            reader.seek(44, NOESEEK_REL) 
        elif self.id == 16:  
            reader.seek(44, NOESEEK_REL) 
        elif self.id == 17:    
            reader.seek(44, NOESEEK_REL) 
        elif self.id == 18:
            self.readBoundingSphere() 
            reader.seek(64, NOESEEK_REL)            
        elif self.id == 19:        
            readChildObjects()  
        elif self.id == 20:  
            self.readBoundingSphere()         
            count1 = reader.readUint()
            reader.seek(8, NOESEEK_REL) 
            count2 = reader.readUint() 
            reader.seek(12*count1, NOESEEK_REL)  
            reader.seek(count2*4, NOESEEK_REL)              
        elif self.id == 21: 
            self.readBoundingSphere()         
            reader.seek(8, NOESEEK_REL)           
            self.readChildObjects()  
        elif self.id == 23:         
            reader.seek(8, NOESEEK_REL)  
            count1 = reader.readUint()
            reader.seek(4*count1, NOESEEK_REL)            
            count2 = reader.readUint()
            for i in range(count2):
                reader.seek(16*count2, NOESEEK_REL)
        elif self.id == 24: 
            reader.readMatrix4x3()        
            reader.seek(1, NOESEEK_REL) 
            self.readChildObjects()             
        elif self.id == 25:  
            reader.seek(96, NOESEEK_REL)  
        elif self.id == 28: 
            self.readBoundingSphere()         
            reader.seek(12, NOESEEK_REL) 
            count = reader.readUint()
            for k in range(count):
                type = reader.readUint()
                reader.seek(12, NOESEEK_REL) 
                vcount = reader.readInt() 
                for i in range(vcount):                 
                    if type == -256:
                        reader.seek(8, NOESEEK_REL)
                    else:
                        reader.seek(16, NOESEEK_REL)                
        elif self.id == 29:  
            self.readBoundingSphere() 
            type = reader.readUint()
            reader.seek(32, NOESEEK_REL)
            if type != 3:
                reader.seek(4, NOESEEK_REL)                            
            self.readChildObjects()              
        elif self.id == 30:
            self.readBoundingSphere() 
            reader.seek(56, NOESEEK_REL)           
        elif self.id == 31:        
            self.readBoundingSphere() 
            count = reader.readUint()
            reader.seek(32, NOESEEK_REL)
            for i in range(count):
                reader.seek(8, NOESEEK_REL)            
        elif self.id == 33:  
            self.readBoundingSphere() 
            reader.seek(72, NOESEEK_REL) 
            self.readChildObjects()                 
        elif self.id == 34:    
            self.readBoundingSphere() 
            reader.seek(4, NOESEEK_REL)
            count = reader.readUint()
            for i in range(count):
                reader.seek(16, NOESEEK_REL)                
        elif self.id == 35:
            self.readBoundingSphere() 
            reader.seek(8, NOESEEK_REL)
            count = reader.readUint()
            for i in range(count):
                type = reader.readUint()
                reader.seek(12, NOESEEK_REL) 
                vcount = reader.readUInt()                 
                for k in range(vcount):
                    if type == 50:
                        reader.seek(24, NOESEEK_REL)                      
                    elif type == 49:
                        reader.seek(8, NOESEEK_REL)
                    elif type == 1 or type = 0 or type == 16 or type = 17:
                        reader.seek(12, NOESEEK_REL)
                    elif type == 2 or type = 3:
                        reader.seek(12, NOESEEK_REL)
                    else :
                        reader.seek(16, NOESEEK_REL)              
        elif self.id == 36:        
            self.readBoundingSphere() 
            reader.seek(64, NOESEEK_REL)
            type = reader.readUint()
            vcount = reader.readUInt()
            for k in range(vcount):
                if type == 2:
                    reader.seek(32, NOESEEK_REL)
                else:
                    reader.seek(20, NOESEEK_REL)
            self.readChildObjects()                              
        elif self.id == 37: 
            self.readBoundingSphere()         
            reader.seek(32, NOESEEK_REL)
            type = reader.readUint()
            vcount = reader.readUInt()
            for k in range(vcount):
                if type == 514:
                    reader.seek(36, NOESEEK_REL)
                elif type == 258 or type == 515:
                    reader.seek(40, NOESEEK_REL)                
                elif type == 2:
                    reader.seek(32, NOESEEK_REL)                
                elif type == 3:                
                    reader.seek(20, NOESEEK_REL)  
            self.readChildObjects()                    
        elif self.id == 39: 
            reader.seek(36, NOESEEK_REL)        
            self.readChildObjects() 
        elif self.id == 40:  
            self.readBoundingSphere()
            reader.seek(64, NOESEEK_REL) 
            reader.seek(8, NOESEEK_REL)
            count = reader.readUInt()  
            reader.seek(4*count, NOESEEK_REL)            
            
    def read(self, reader):
        self.readHeader(reader)
        self.readData(reader) 
        
    
class HTB3D():
    def __init__(self, reader):
        self.reader = reader
        self.filesize = 0
        self.materialListOffset = 0
        self.materialListSectonSize = 0
        self.objectsSectionOffset = 0
        self.objectsSectionSize = 0
        self.materials = []
        self.objects = []
        
    def readHeader(self, reader):  
        if reader.readString() != "b3d":
           return 0
           
        self.filesize = reader.readUInt()   
        self.materialListOffset = reader.readUInt()   
        self.materialListSectonSize = reader.readUInt()   
        self.objectsSectionOffset = reader.readUInt() 
        self.objectsSectionSize = reader.readUInt()
        
        return 1   
        
    def readMaterialList(self, reader):
        count = reader.readUInt() 

        for i in range(count):
            self.materials.append(reader.readStringFromBytes(32))       
  
    def readObject(self, reader):
        object = HTB3DObject()
        object.read(reader)
        
        return object
  
    def readObjects(self, reader):
        while True:
            id = reader.readUInt()
            if id == 333:        
                self.objects.append(self.readObject())
            if id == 555:
                break              

    def read(self):
        self.readHeader(self.reader)      
        self.readMaterialList(self.reader)      
        self.readObjects(self.reader)      
    
    
def b3dCheckType(data):

	return 1


def b3dLoadModel(data, mdlList):
    noesis.logPopup()
    b3d = HTB3D(B3DStream(data))
    b3d.read()
    
    return 1    