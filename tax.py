def calculateTax(sum, dob, scop):
    if type(sum) != int:
        raise(TypeError)
    
    tax = sum * dob
    return {"tax": tax, "suma": sum, "dob": dob, "scop": scop}
    