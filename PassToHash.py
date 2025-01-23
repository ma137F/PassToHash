# Imports 
import os
import sys
import hashlib

# Declarations  

# List that contains the passwords read from the passowrds file.
words_lst = []

# List to store the lines from the hash file.
h_lines = []  
    
# Function that iterates over each password, encodes it according to the each hash type and checks if it's equal to the result.
def iter_hash_file(words_lst,h_lines):
    
    # First loop iterating over the word list and setting the current password value.
    for p in range(0, len(words_lst)): 
        password = words_lst[p] 

        # Second loop iterating over each line in the hashes file containing the encoding types and the final hash.
        for k in range(0, len(h_lines)):

            # Setting a varible pointing to the begining of each line.
            curr_line = h_lines[k]  
            # Variable contatining the hash at the end of the current line. 
            line_hash = curr_line[-1]

            # Setting a temprorary variable for encoding 
            pwd = password 
            # Third loop iterating ovear each element containing a hash type and encdonig the password accoding to it.
            for i in range(0, len(curr_line) - 1):             

                if(curr_line[i] == "md5"):

                    pwd = pwd.encode()                    
                    pwd_md5 = hashlib.md5(pwd).hexdigest()
                    pwd = pwd_md5
                
                if(curr_line[i] == "sha1"):

                    pwd = pwd.encode()                
                    pwd_sha1 = hashlib.sha1(pwd).hexdigest()
                    pwd = pwd_sha1

                if(curr_line[i] == "sha256"):

                    pwd = pwd.encode()
                    pwd_sha256 = hashlib.sha256(pwd).hexdigest()
                    pwd = pwd_sha256

                if(curr_line[i] == "sha512"):

                    pwd = pwd.encode()
                    pwd_sha512 = hashlib.sha512(pwd).hexdigest()
                    pwd = pwd_sha512
                
                # If the encoded password value matches the hash, the passowrd is printed.            
                if (pwd == line_hash):
                    print("password:",password)


# python main function
def main():

# Open the current files for reading
    with open(r'<PathToFile>Hashes.txt', 'r') as hashes:
        for line in hashes:
            h_lines.append(line.strip().split(','))

    with open(r'<PathToFile>Passwords.txt', 'r') as passwords:
        for word in passwords:
            words_lst.append(word.rstrip())

    # Passing both lists for the function to iterate over them.
    iter_hash_file(words_lst,h_lines)

if __name__=='__main__':
    main()

