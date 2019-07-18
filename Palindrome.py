
def main():
    #Enter Code Here
    word = input("-> ")
    print(len(word))
    if (len(word) == 3):
        if word[0] == word[2]:
            print("That's a Palindrome")
    elif (len(word) == 5):
        if word[0] == word[4] and word[1] == word[3]:
            print("That's a Palindrome")    
    elif (len(word) == 7):
        if word[0] == word[6] and word[1] == word[5] and word[2] == word[4]:
            print("That's a Palindrome")            
    elif (len(word) == 9):
        if word[0] == word[8] and word[1] == word[7] and word[2] == word[6] and word[3] == word[5]:
            print("That's a Palindrome")
    elif (len(word) == 11):
        if word[0] == word[10] and word[1] == word[9] and word[2] == word[8] and word[3] == word[7] and word[4] == word[6]:
            print("That's a Palindrome")  
    else:
        print("That's not a Palindrome")
    
def Palindrome():
    #Enter Code Here
    print()
    
    

if __name__ == "__main__":
    main()