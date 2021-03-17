import datetime # import python tool untuk conversi waktu

# function untuk conversi waktu
def timeConverter():
    converted = datetime.timedelta(seconds=x)
    return str(converted)

# if statement dalam while loop untuk filter inputs
while True:
    try:
        x = int(input('masukkan detik : '))
    except ValueError:
        print('Invalid Input !')
        continue
    if x > 359999:
        print('Value too high')
    else:
        print('Konversi :', timeConverter())