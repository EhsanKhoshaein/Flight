def mgr_entering(search, flight_list):
    result = []
    flag = 0
    index = 0
    f_char = ''
    for flight in flight_list:
        if flight[0] == search:
            flag = 1
            i = 0
            while(i <= len(flight)):
                if i == len(flight)-1:
                    f_char = f_char + flight[i]
                    break
                f_char = f_char + flight[i] + ' - '
                i += 1
            index += 1
    result.append(flag)
    result.append(f_char)
    result.append(index)
    return result

def emp_entering(search, flight_list):
    flag = 0
    for flight in flight_list:
        if flight[0] == search:
            flag = 1
            break
    return flag, flight
