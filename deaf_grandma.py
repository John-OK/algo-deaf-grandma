def deaf_grandma():
    number_goodbyes = 0
    user_response = input ("HEY KID!\n")

    while(number_goodbyes < 2):
        if(user_response == "GOODBYE!" and number_goodbyes == 0):
            user_response = input("LEAVING SO SOON?\n")
            number_goodbyes += 1
        elif(user_response == "GOODBYE!" and number_goodbyes == 1):
            print("LATER, SKATER!")
            number_goodbyes += 1
        elif(not user_response.isupper() and len(user_response) > 0):
            user_response = input("SPEAK UP, KID!\n")
        elif user_response == "":
            user_response = input("WHAT?!\n")
        else:
            user_response = input("NO, NOT SINCE 1946!\n")


deaf_grandma()