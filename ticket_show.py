def showing(ticket, flight):
    print('\n          <><<><><><><><><><><><><><><><><><><><><><><><><><><><><><>><><><><><><><><><><><><><><><><><><><><>')
    print('          <>          Passanger Infromation:               Ticket Information:                              <>')
    i = 0
    j = 0
    while(i <= 4):
        print('          <>         ',end="")
        print("{0: ^20s}".format(ticket[j]),end='')
        print('         ',end="")
        print("         {0: ^20s}".format(flight[j]),end='')
        print('{0: ^20s}'.format(chr(32)),end='')
        print('         <>',end='\n')
        i += 1
        j += 1
    print('          <><<><><><><><><><><><><><><><><><><><><><><><><><><><><><>><><><><><><><><><><><><><><><><><><><><>')

