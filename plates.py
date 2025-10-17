def main():
    plate = input("Plate: ") #get input from the user
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#decide whether to print "Valid" or "Invalid"
def is_valid(plate):
    #rule 1: two letters in the beginning
    if not plate[0:2].isalpha():
        return False
    #plate[0:2] returns up to two characters safely even if the string is shorter
    #.isalpha() checks whether those characters are all letters

    #rule 2: between 2 and 6 characters inclusive
    if not 2 <= len(plate) <= 6:
        return False
    #enforced the permitted length range

    #rule 3: letters and numbers only (alphanumeric)
    if not plate.isalnum():
        return False
    #.isalnum() makes sure there are only letters and numbers

    #loop that scans characters from the start
    for i in range(len(plate)):
        char = plate[i]

        #on the first character that isdigit()
        if char.isdigit():
            #rule 4: digits at the end
            if not plate[i:].isdigit():
                return False
            #ensures that from that position to the end all characters are digits

            #rule 5: the first digit used cannot be '0'
            if char == '0':
                return False
            #rejects plates whose first used digit is '0'

            #if the digits rules passed, break exits the loop
            break

    #if all checks passed, the plate is valid
    return True

main()