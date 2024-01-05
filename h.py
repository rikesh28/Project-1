def convertDate(date):
    month_abbrev = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    if date[0] == '0':
        dates = date[1]
    
    else:
        dates = date[:2]
    
    month = month_abbrev[int(date[2:4])]
    year = date[4:]
    
    return f'{month} {dates}, {year}'

def main():
    print(convertDate('07071977'))
    
main()