# Function to convert a int to hex within the range 0 - 15
def int_to_hexa_char(tal):
    #var to hold hexadecimal chars. Ascending order.
    hexa_chars = "0123456789ABCDEF"

    #Returns the hexadecimal number at the index at tal (user input int)
    return hexa_chars[tal]

# Function for converting hexadecimal in range 0 - F to corresponding decimal number in range 0 - 15
def hexa_char_to_int(tal):
    #var to hold hexadecimal chars. Ascending order.
    hexa_chars = "0123456789ABCDEF"
    #converts any input from user to upper to ensure match in hexa_chars
    tal = tal.upper()
    # Compares the input with the hexa chars var. Return index number. 
    # Works up to f for hexa since they are specified in order in the hexa_chars variable
    return hexa_chars.index(tal)

# Reverses a string. (Hexa calc)
def reverse_string(tal):
    result = ""
    for c in tal:
        result = c + result
    return result

# Function for convert hex -> int without range restriction
def hexa_to_deci(tal):

    # Reverses string for hexadecimal calc in for loop
    reverse_tal = reverse_string(tal)

    # Def and declares total and square to 0 for use in loop. Add each calc to total, then increment square by 1 to represent a higher order
    total = 0
    square = 0

    for c in reverse_tal:
        calc_sequence = hexa_char_to_int(c) * 16 ** square
        total += calc_sequence
        square += 1
    return total



# Bool for while loop
running = True
# Default for user menu choice (0 = main menu)
user_menu_choice = 0

while running:

    if user_menu_choice == 0:

        print("----- Meny -----")
        print("1. Decimal heltal 0 - 15 till Hexadecimal 0 - F")
        print("2. Hexadecimal 0 - F till decimal heltal 0 - 15")
        print("3. Hexadecimalt till heltal konvertering")
        print("9. Avsluta \n")

        user_menu_choice = int(input("Vilken funktion vill du köra?"))

        

    # Checks menu choice for Dec to Hex 0 - F
    elif user_menu_choice == 1:
        #Takes input from user and runs it in the 0 -> 15, int -> hex function. Requires int as input
        tal = int_to_hexa_char(int(input("Ange ett heltal mellan 0 och 15: ")))
        print(tal)

    # Checks menu choice for Hex to Dec 0 - 15
    elif user_menu_choice == 2:
        #Takes input from user and runs it in the 0 -> F, hex -> int function
        tal = hexa_char_to_int(input("Ange ett hexadecimalt tal mellan 0 och F: "))
        print(tal)

    # Checks menu choice for Hex to Dec
    elif user_menu_choice == 3:
        #Takes input from user and runs it in the full convert function (Hex -> Dec)
        tal = hexa_to_deci(input("Ange ett hexadecimalt tal: "))
        print(tal)

    # check user input for exit app, stops while loop
    elif user_menu_choice == 9:
        running = False
        continue