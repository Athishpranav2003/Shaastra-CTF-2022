
def normalised_ord(char):

    normalised_char = ord(char)
    normalised_char = normalised_char-33
    normalised_char = normalised_char%94
    return normalised_char
    
    
def normalised_chr(char):

    normalised_char = char%94
    normalised_char = normalised_char+33
    return chr(normalised_char)
    
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
                return decrypted_string

encrypted_string = "E-;4FYXEuhk3}468:<>@B:.;9\P~*()_G$t@|sTW64G][q;4zo"
print(decrypt(encrypted_string))
