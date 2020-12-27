def calculateToalFine():
    speed_limit = int(input("Enter the speed limit:"))
    actual_speed = int(input("Enter actual speed:"))

    base_fine =20 +((actual_speed - speed_limit)* 5)
    print("base fine %d" % base_fine)
    spa = (base_fine // 10) * 10
    print("state penalty assessment: %d" % spa)
    scf = (base_fine // 10)* 5
    print("state court fund: %d" % scf)
    total_fine = base_fine + spa + scf
    print("total fine: %d" % total_fine)

calculateToalFine()


