import math
import os
import time



names = {"b1" : ["nuo",True],
         "b2" : ['miu',True],
         "b3" : ['lof',True],
         "b4" : ['pod',True]}

while(True):
    print("Availabe books : ")
    for i, j in names.items():
        print(i, j)
    print("-------------------------------------------------")

    book_name = input('''Enter the name of the book you want to buy.
    True -> book is avaliable
    False -> book is not availiable
    Exit -> exit 
    ---------------------------------------------------------------------
    ''')
    if book_name.lower() == 'exit':
        break
    false_check = list(names.get(book_name))
    if false_check[1] == False:
        print("Book has already been purchased......")
        print("---------------------------------------------")
        break
    for i in names.keys():
        if book_name == i:
            print("Book found")
            option = input("Do you want to buy this book ?|")
            if option.lower() == 'yes':
                print('\n')
                print()
                print('Processing...')
                time.sleep(4)
                print("Book purchased...:-)")
                x = list(names.get(i))
                print(x)
                print("-------------------------------------------")
                intr_name = x[0]
                intr_avil = x[1]
                intr_avil = False
                names[book_name] = [intr_name, intr_avil]
            else:
                print("Availabe books : ")
                for i, j in names.items():
                    print(i, j)

            break
    else:
        print("Book not found")

