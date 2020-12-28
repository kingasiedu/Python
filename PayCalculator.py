def calPay(rate,hours):
    otpay = 0
    pay = 0
    if hours > 80:
        ot = hours - 80
        otpay = ot * (rate*1.5)
    pay = hours * rate
    return otpay + pay


def getEmpl():
    empls = []
    while True:
        name = input("Name:")
        rate = int(input("rate:"))
        hours = int(input("hours:"))
        pay = calPay(rate, hours)
        empls.append([name,rate,hours])
        print("name: %s, rate: %d hours: %s pay %s" % (name, rate, hours, pay))


getEmpl()




