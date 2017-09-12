def bad_type():
    inp = raw_input("Write something for me to type: ")
    return type(inp)
    
#A raw input is always reverted to a string because thats the data type occociated with that function.