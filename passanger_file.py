def load(name):
    ticket_char_list = []
    ticket_list = []
    ticket_file = open(f'{name}.txt','r')
    ticket_char = ticket_file.readlines()
    for item in ticket_char:
        new_ticket_char = item.split('\n')
        for info in new_ticket_char:
            if info != '':
                ticket_char_list.append(info)
    for item in ticket_char_list:
            new_item = item.split(' , ')
            ticket_list.append(new_item)
    ticket_file.close()
    return ticket_list
def save(flight, ticket, name):
    flight_char = ''
    i = 1
    while(i <= len(flight)-2):
        flight_char = flight_char + flight[i] + ' - '
        i += 1

    ticket_char = ''
    j = 1
    while(j <= len(ticket)-1):
        if j == len(ticket)-2:
            ticket_char = ticket_char + ticket[j]
            break
        ticket_char = ticket_char + ticket[j] + ' - '
        j += 1
    new_ticket_char = ''
    new_ticket_char = '{}'.format(new_ticket_char) + '{}'.format(flight_char) + '{}'.format(ticket_char)
    ticket_file = open(f'{name}.txt','a')
    ticket_file.writelines(new_ticket_char)
    #ticket_file.writelines(flight_char + '\n')
    ticket_file.close()
    return ticket_file
