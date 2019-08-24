import webbrowser as wb

true=1
while true:
    print "Enter the website you wish to open : \n1.Google \n2.Wikipedia "
    choice = input()
    if choice == 1:
        wb.open("https://www.google.co.in")
    elif choice == 2:
        wb.open("https://www.wikipedia.org")
    else:
        break
