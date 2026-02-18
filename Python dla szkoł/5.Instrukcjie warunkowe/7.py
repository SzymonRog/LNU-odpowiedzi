def setPower( pm25, pm10 ):
    m = 0
    if pm25 <= 12 or pm10 <= 20:
        m = 0
    elif pm25 >= 13 and pm25 <= 24 or pm10 >= 21 and pm10 <= 50:
        m = 1
    elif pm25 >= 25 and pm25 <= 36 or pm10 >= 51 and pm10 <= 80 :
        m = 2
    elif pm25 >= 36 or pm10 >= 80:
        m = 3
    return m