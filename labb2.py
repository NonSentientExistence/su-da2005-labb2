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

# Converts int to corresponding hexadecimal number
def deci_to_hexa(tal):

    #Bool for while loop
    calculating = True
    # Empty str var to build final result
    result = ""
    
    # Loops until quotient is 0. If quotient check is done as loop condition it would stop before completing last digit in hex output
    while calculating:
        # Divides input or quotient with 16. Saves quotient in variable
        quotient = tal//16
        # Modus on input or quotient to get remainder
        remainder = tal%16
        # Call prev int -> hex func to convert remainder into hex
        remainder_hex = int_to_hexa_char(remainder)
        # Add to result string in each iteration, in correct order to avoid reversed hex output
        result = remainder_hex + result
        
        # If quotient is 0, stop calc while loop by setting condition variable to false
        if quotient == 0:
            calculating = False
        # if quotient isn't 0, set tal to calculated quotient and run again
        else:
            tal = quotient

    return result

def remove_prefix(hexa):
    # Bool for while loop condition
    cleaning = True
    # Set hexa to uppercase
    hexa = hexa.upper()

    # Check for inital 0x prefix, remove if found
    if hexa[:2] == "0X":
        hexa = hexa[2:]

    while cleaning:

        # Check if hexa string is empty and if true, set hexa to 0 and stop loop
        if hexa == "":
            hexa = "0"
            cleaning = False
        # Refactored to check for 0x or 0 prefix before loop. Incorrect return if input is i.e. 0x00000x, would return 0 when it should be X
        # check if the first char in hexa is 0
        # if true, save new string without first char into hexa var
        # Could also be refactored to use left slice to cut first char. Unsure if allowed so used this. 
        elif hexa[0] == "0":
            hexa = hexa[1:]
        # if lead char in hexa isn't X or 0, stop while loop
        else:
            cleaning = False

    return hexa

def add_mixed_list(input_list, output_form):
    # Result var to calc total in dec
    total_dec = 0
    # Splice in all elements in list into new list to ensure org list remains unchanged
    # Current function will not alter the list, protects against expanding the function where it could alter the original list
    calc_list = input_list[:]
    
    # Calculate addition result of input list into decimal
    for n in calc_list:
        if type(n) is int:
            total_dec += n
        elif type(n) is str:
            total_dec += hexa_to_deci(remove_prefix(n))      
    
    # Checks output_form for requested output format. Converts to hex if hexadecimal has been requested
    if output_form.upper() == "H":
        return deci_to_hexa(total_dec)
    elif output_form.upper() == "D":
        return total_dec
    else:
        print("Ogiltigt utformat angivet, ange h eller d")
        return
    
def validate_hexa(hexa):
    # Cleans prefix and leading zeros. Remove prefix also sets hexa to upper case for compare
    clean_hexa = remove_prefix(hexa)

    #var to hold valid hexadecimal chars.
    hexa_chars = "0123456789ABCDEF"

    # Iterates through all chars hexa and validates that it only contains valid hexadecimal characters.
    for n in clean_hexa:
        if n not in hexa_chars:
            return False
        
    return True

    
    

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
        print("4. Heltal till hexadecimal konvertering")
        print("5. Ta bort prefix från Hexadecimalt tal (0 och x)")
        print("6. Beräkna totalen av en blandad list(Hex och dec)")
        print("7. Validera ett hexadecimalt tal")
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

    elif user_menu_choice == 4:
        #Takes input from user and runs it in the full convert function (Dec -> Hex)
        tal = deci_to_hexa(int(input("Ange ett heltal: ")))
        print(tal)

    # Checks menu choice for prefix clean hexa
    elif user_menu_choice == 5:
        #Takes input from user and cleans prefixes (0 and X). Prints cleaned hexa
        tal = remove_prefix(input("Ange ett hexadecimalt tal: "))
        print(tal)

    # Checks menu choice for add mixed list
    elif user_menu_choice == 6:
        # Var for menu choice in this sub func
            
        # Empty list to submit to function
        submit_list = []

        #bool 
        mix_list_running = True

        #If submenu choice 1, let user input element to add to list
        while mix_list_running: 

            # User input, kind of number to add. Just for sorting input into the submit list
            print("Lägga till hexadecimalt eller decimal tal? (h/d) : ")
            hex_or_dec = input()

            # if for ensuring input is added correctly to input list. 
            if hex_or_dec.upper() == "H":
                add_to_list = input("Ange ett hexadecimalt tal att lägga till i listan: ")
                submit_list.append(add_to_list)
            # Checks if string is only numbers, if true then covert to int before adding to list
            elif hex_or_dec.upper() == "D":
                add_to_list = input("Ange ett heltal att lägga till i listan: ")
                if add_to_list.isdigit():
                    submit_list.append(int(add_to_list))
                else:
                    input("Ogiltigt heltal, försök igen. Tryck på valfri tangent...")
            else: 
                input("Ogiltigt utdata val, välj d eller h. Tryck på valfri tangent för att börja om...")
            
            # Print current list
            print("Din nuvarande lista innehåller följande tal: ")
            print(submit_list)
            # if input is y then continue add number loop. Anything else, stop loop
            add_more = input("Lägga till ett till tal? (y för ja, annars valfritangent)")
            if add_more.upper() == "Y":
                continue
            else: 
                mix_list_running = False

        # Asks for output format. Sets output_form according to choice to submit to func later
        print("Vill du has resultatet i decimal(d) eller hexadecimal(h)?")
        result_type = input("Ange d eller h: ")

        if result_type.upper() == "D":
            output_form = "d"

        elif result_type.upper() == "H":
            output_form = "h"
        
        # Prints submitted list and gives info on output result. Continues on any input 
        print("Din lista med tal: ")
        print(submit_list)
        print(f"Resultatet fås i hexadecimalt (H) eller i decimalt (D): {output_form.upper()}")
        input("Tryck enter för att fortsätta...")

        # Prints result of calculated list. Then prints original list to confirm it hasn't been modified 
        print(f"\nResultatet är :")
        print(add_mixed_list(submit_list,output_form))
        print(f"\nDin ursprunliga lista var :")
        print(submit_list)
        # Awaits any input so user can read. Clears list before sending user to main menu
        input("Tryck enter för att fortsätta...")
        submit_list.clear()
        
        user_menu_choice = 0
        
    # Checks menu choice for single hexadecimal number validation
    elif user_menu_choice == 7:
        # Validates if user input is a valid hexadecimal
        tal = validate_hexa(input("Ange ett hexadecimalt tal: "))
        print(tal)

    # check user input for exit app, stops while loop
    elif user_menu_choice == 9:
        running = False