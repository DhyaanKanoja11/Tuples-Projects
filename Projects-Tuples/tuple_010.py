tup=()
style='~'*62
n=int(input("Enter The Number Of Elements You Want To Add in The Main TUPLE:- "))

for i in range(1,n+1):
    p=input(f"Enter Element #{i}: ")
    tup=tup+(p,)

print(f"The Main Tuple Created is :- {tup}")

while True:
    print(style)
    print("║▌║▌║█│║▌║▌║█│▌│█║▌║▌║ TUPLE OPERATIONS ║▌║▌║█│║▌║▌║█│▌║▌║▌║█│")
    print("1. \tDisplay Tuple")
    print("2. \tAccess Elements")
    print("3. \tCount Number Of Element in Tuple")
    print("4. \tSorting Tuple")
    print("5. \tMaximum And Minimum Of The Tuple")
    print("6. \tSlice A Tuple")
    print("7. \tAdd More Elements In a Tuple")
    print("8. \tIntegrated Programs Menu")
    print("9. \tExit")
    print(style)
    choice=int(input("Enter Your Choice: "))
    

# Display Tuple
    if choice==1:
        print(f"Displayed Tuple Is : {tup}")

#Access Elements
    elif choice==2:
        print(style)
        index=int(input("Enter Index to access the element:"))
        if 0<= index <len(tup):
            print(f"Element at index {index} is {tup[index]}")
        print(style)

#Count Number Of Elements
    elif choice==3:
        print(style)
        count=int(input("Enter Element You Want To Count: "))
        x=tup.count(count)
        print(f"{count} appears {x} times in tuple.")
        print(style)

#Sorting Tuple
    elif choice==4:
        print(style)
        sort_tuple = sorted(tup)
        print(f"Sorted Tuple Is : {sort_tuple}")
        print(style)

#Maximum and Minimum Of The Tuple
    elif choice==5:
        print(style)
        max_element = max(tup)
        min_element = min(tup)
        print(f"Maximum Value Is : {max_element}\nMinimum Value Is : {min_element}")
        print(style)

#Slice a Tuple
    elif choice==6:
        print(style)
        print("Slice A Tuple")
        a=int(input("Enter Start Index: "))
        b=int(input("Enter End Index: "))
        sliced_tuple=tup[a:b]
        print(f"Original Tuple: {tup}\nSliced Tuple: {sliced_tuple}")
        print(style)

    #Add More Elements In a Tuple
    elif choice==7:
        print(style)
        x=()
        n1=int(input("Enter The Number Of Elements You Want To Add in The Main TUPLE:- "))
        for i in range(1,n1+1):
            p=input(f"Enter Element #{i}: ")
            x=x+(p,)
        tup=tup+x
        print(f"Renewed Tuple is \n{tup}")
        print(style)

    #Integrated Programs Menu
    elif choice==8:
        while True:
            ("\nＩｎｔｅｇｒａｔｅｄ Ｐｒｏｇｒａｍｓ Ｍｅｎｕ")
            print('1. Sum Of Numerical Elements Of Tuple')
            print('2. Average Of Numerical Elements Of Tuple')
            print('3. Search And Replace')
            print('4. Concatenate Tuples')
            print('5. Display Unique Elements')
            print('6. Exit / Back To Main Menu')
            choice1=int(input("Enter Your Choice: "))

            #Sum Of Numerical Elements
            if choice1==1:
                print(style)
                sum=0
                num=len(tup)
                for i in tup:
                    if type(i) == int or float:
                        sum+=i
                print(f"\nSum of all numerical elements of tuple is {sum} .")
                print(style)

            #Average Of Numerical Elements
            elif choice1==2:
                print(style)
                avg=0
                count=0
                for i in tup:
                    if type(i) == int or float:
                        avg += i
                        count += 1
                avg = avg / count
                print(f"\nAverage of all numerical elements of tuple is {avg}.")
                print(style)

            #Search And Replace
            elif choice1==3:
                print(style)
                se = input("Enter the element to search for: ")
                re = input("Enter the replacement element: ")
                if se in tup:
                    lst1=[]
                    for i in tup :
                        if i==se:
                            lst1.append(re)
                        else:
                            lst1.append(i)
                    new_tuple=tuple(lst1)
                    tup=new_tuple
                    print('Updated Tuple:',new_tuple)

            #Concatenate Tuples
            elif choice1==4:
                print(style)
                tuplist=list(tup)
                n=int(input("\nHow many tuples do you want to concatenate? "))
                concat=[]
                while len(concat)<n:
                    temp=input(f"Enter a tuple no.{len(concat)+1}: ")
                    temp=eval(temp)
                    concat.extend(temp)
                final_tups=[tup,*concat]
                final_tuple=tuple(final_tups)
                print('\nConcatenated Tuple: ',final_tuple)
                tup=final_tuple
                print(style)

            #Display Unique Elements
            elif choice1==5:
                print('\n\n\n',style)
                print(f'The Unique Elements Of The List are {set(tup)}')
                print('\n\n\n',style)

            #Exit/Return To Main Menu
            elif choice1==6:
                print('Returning To Main Menu')
                break

            #Wrong Choice Entered
            else:
                print(style)
                print(f'\nPress Any Key To Continue.........')
                alphagamma=input(' ')
                print(style)

    #Exitting Main Menu
    elif choice==9:
        print(style)
        print('»»ᅳTᅳᅳhᅳᅳaᅳᅳnᅳᅳkᅳ ᅳYᅳᅳoᅳᅳuᅳ►')
        print("Exiting................")
        break 

    #Wrong Choice Entered
    else:
        print("Invalid Choice..........")
        print("Press Any Key To Continue................")
        BacktoMAinMenu=input("")
