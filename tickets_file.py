def load(search):
    tickets_char_list = []
    tickets_list = []
    tickets_file = open('{}.txt'.format(search),'r')
    tickets_char = tickets_file.readlines()
    for ticket in tickets_char:
        new_tickets_char = ticket.split('\n')
        for item in new_tickets_char:
            if item != '':
                tickets_char_list.append(item)
    for item in tickets_char_list:
            new_item = item.split(' - ')
            tickets_list.append(new_item)
    tickets_file.close()
    return tickets_list

def save(ticket, search):
    ticket_char = ''
    i = 0
    while(i <= len(ticket)):
        if i == len(ticket)-1:
            ticket_char = ticket_char + ticket[i]
            break
        ticket_char = ticket_char + ticket[i] + ' - '
        i += 1
    tickets_file = open('{}.txt'.format(search),'a')
    tickets_file.writelines(ticket_char + '\n')
    tickets_file.close()
    #return flight_file

def rewrite(search, tickets_list):
    tickets_file = open(f'{search}.txt','w')
    tickets_file.close()
    for ticket in tickets_list:
        ticket_char = ''
        i = 0
        while(i <= len(ticket)):
            if i == len(ticket)-1:
                ticket_char = ticket_char + ticket[i]
                break
            ticket_char = ticket_char + ticket[i] + ' - '
            i += 1
        ticket_file = open(f'{search}.txt','a')
        ticket_file.writelines(ticket_char + '\n')
        ticket_file.close()
    return ticket_file
