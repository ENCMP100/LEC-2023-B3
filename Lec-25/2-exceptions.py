## Exceptions and Input Output

def main():
    
    try:
        
        filename = input('Enter GPA data file (gpa[1-4].txt): ')
        # May raise IO error
        fileOpenedSuccessfully = False
        infile = open(filename)
        fileOpenedSuccessfully = True
        
        print("Data file opened successfully.")
        
        gpa = loadGpas(infile)
        
        print("GPA:")
        print(gpa)
        
    except IOError as error:
        print("File error:" + str(error))
    except ValueError as error:
        print("Value error: " + str(error))
    except RuntimeError as error:
        print("Runtime error: " + str(error))
    finally:
        if fileOpenedSuccessfully:
            infile.close()
    
    print("Program ended.")


def loadGpas(file):
    gpaValues = []
    line = file.readline()
    while line != "":
        val = float(line) # May raise a ValueError if the line is not numeric
        
        if not 0 <= val <= 4:
            raise RuntimeError("GPA must be between 0 and 4")
            
        gpaValues.append(val)
        
        line = file.readline()
    
    return gpaValues


main()

           
        
        
        
            

