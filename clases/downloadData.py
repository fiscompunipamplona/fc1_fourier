import wget

url = 'ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt'

wget.download(url)

data = open('co2_mm_mlo.txt')

n = 0

for strline in data.readlines():
    line = strline.split()
#    print(line[0])
    if line[0] != "#":
        print (line[0],line[2])

    n += 1
    if n > 150:
        break
