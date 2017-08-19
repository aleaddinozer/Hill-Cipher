# coding: utf-8

import numpy as np

def shape_key():
    input_key = input("Enter key: ")
    i_key = []
    for ch in input_key:
        if ch.isalnum():
            i_key += [ord(ch)]   
                     
    all_cell = len(i_key)
    row_cell = int(all_cell**0.5)
    key_matrix = []
    
    if (row_cell*row_cell) != all_cell:
        print("It has to be a matrix with a square root without any non-alphanumeric letters.\nTry Again\n")
        return shape_key()
    else:
        for i in range(0,all_cell,row_cell):
            key_matrix += [i_key[i:i+row_cell]]
    key_matrix = np.mat(key_matrix,dtype = int)
    
    return key_matrix


def text_asmatrix(p_text,size):
   
    p_text = [ord(c) for c in p_text]#convert ascii
    text_matrix = []
    while len(p_text) > size:
        piece = p_text[:size]
        text_matrix.append(piece)
        p_text = p_text[size:]
    text_matrix.append(p_text)
    
    try:
        text_matrix = np.mat(text_matrix, dtype=int)
    
    except Exception:
        
        print("your text must be divisible by the length of the key matrix.")
        print("Key length:", size)
        p_text_again = input("Enter your text again: \n")
        
        return text_asmatrix(p_text_again, size)
   
    return text_matrix
        
def encrypt(plain_text, key):

    cipher_text = np.matmul(plain_text, key)
    arr = ""
    for i in np.array(cipher_text).flat:
        arr += chr(i % 26 + ord('a'))
    print("\nencrypted text:\n",arr)
    return cipher_text


def decryption(cipher_text, key):
   
    try:
        inv_key = np.linalg.inv(key) 
    except Exception:
        print("determinant of key is zero. So text cannot be deciphered")   
        quit()
         
    decrypted_text = np.matmul(cipher_text, inv_key)
    arr = ""
	
    #flat : lets us to iterate over entries of array without wasting memory
    for i in decrypted_text.flat:
        arr += chr(int(round(i)))
    
    print("decrypted text:\n",arr)
    
    return decrypted_text
   
   
if __name__ == '__main__':

#get key
# you may want to enter your key as a number sequence
#    get_key = input("Enter key as a number sequence for ex: 2 3 9 5:\n").split(sep=None)
    key = np.mat(shape_key(), dtype=int)
    print("key:\n", key)
    
#plain text to matrix
    p_text = input("Text to encrypt:")
    row_length = len(key)
    plain_matrix = text_asmatrix(p_text, row_length)
#    print("text as matrix:\n", plain_matrix)
    
#encryption
    encrypted_text = encrypt(plain_matrix, key)
    print("encrypted text as matrix:\n", encrypted_text) 
   
#decryption
    decrypted_text = decryption(encrypted_text, key)
    print("decrypted text as matrix:\n", decrypted_text)
