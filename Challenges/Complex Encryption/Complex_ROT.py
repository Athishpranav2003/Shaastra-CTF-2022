
def normalised_ord(char):

    normalised_char = ord(char)
    normalised_char = normalised_char-33
    normalised_char = normalised_char%94
    return normalised_char
    
    
def normalised_chr(char):

    normalised_char = char%94
    normalised_char = normalised_char+33
    return chr(normalised_char)
    
def key(unencrypted_string):

    strlength = len(unencrypted_string)
    sym_key = 0;
    p = normalised_ord(unencrypted_string[-2])
    
    for i in range(strlength):
    
        sym_key = sym_key + normalised_ord(unencrypted_string[i])
        
    return sym_key,p   
        
def encrypt(unencrypted_string):
    
    strlength = len(unencrypted_string)
    encrypted_string = ""
    symmetric_key , p = key(unencrypted_string)
    
    for i in range(strlength):
    
        init_char = normalised_ord(unencrypted_string[i])
        
        if i == 0 :
        
            init_char = init_char + p + symmetric_key
            
        else:
        
            init_char = init_char + normalised_ord(unencrypted_string[i-1]) + symmetric_key
            
        encrypted_string = encrypted_string + normalised_chr(init_char)
        
    return encrypted_string

                
string = input("Enter the string to be encrpyted : ")
encrypted_string = encrypt(string)
print(encrypted_string)     

