day = input()
mon = {'01': 'January', '02': 'February', '03': 'March','04': 'April','05': 'May','06': 'June', '07': 'July', '08': 'August', '09': 'September','10': 'October', '11': 'November', '12': 'December'}
day = day.replace("/")
day = day.replace(',')
word_list = day.split()

if word_list[0].isalpha():
    mm = mon[word_list[0]]
else:
    mm = word_list[1]
    dd = word_list[1]

