
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
        
            init_char = init_char + p +symmetric_key
            
        else:
        
            init_char = init_char + normalised_ord(unencrypted_string[i-1]) + symmetric_key
            
        encrypted_string = encrypted_string + normalised_chr(init_char)
        
    return encrypted_string
def decrypt(encrypted_string):
    
    strlength = len(encrypted_string)
    
    for sym_key in range(95):
    
        for q in range(95):
        
            decrypted_string=""
            
            for i in range(strlength):
            
                init_char = normalised_ord(encrypted_string[i])
                
                if i == 0:
                
                    init_char = init_char - sym_key - q
                    
                else:
                
                    init_char = init_char - normalised_ord(decrypted_string[i-1]) - sym_key
                    
                decrypted_string = decrypted_string + normalised_chr(init_char)
            if decrypted_string.startswith("ShaastraCTF"):
                print(decrypted_string)

                
string = "ShaastraCTF{Brutu5_!5_betray!ng_a11_0f_u5}"
encrypted_string = encrypt(string)
print(encrypted_string)     
decrypt(encrypted_string)

