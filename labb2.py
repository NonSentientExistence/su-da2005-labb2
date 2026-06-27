
# Function to convert a int to hex within the range 0 - 15
def int_to_hexa_char(tal):
    hexa_chars = "0123456789ABCDEF"

    #If compares tal for all possible inputs in range 0 - 15. Returns invalid input if not within 0 - 15. 
    if tal == 0:
        return 0
    elif tal == 1:
        return 1
    elif tal == 2:
        return 2
    elif tal == 3:
        return 3
    elif tal == 4:
        return 4
    elif tal == 5:
        return 5
    elif tal == 6:
        return 6
    elif tal == 7:
        return 7
    elif tal == 8:
        return 8
    elif tal == 9:
        return 9
    elif tal == 10:
        return "A"
    elif tal == 11:
        return "B"
    elif tal == 12:
        return "C"
    elif tal == 13:
        return "D"
    elif tal == 14:
        return "E"
    elif tal == 15:
        return "F"
    else:
        return "Invalid input"

tal = int_to_hexa_char(int(input("Ange ett heltal mellan 0 och 15: ")))

print(tal)