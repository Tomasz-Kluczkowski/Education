import urllib.request

url = "http://www.textfiles.com/apple/ADC/adv.881115"
destination_filename = "rfc793.txt"

urllib.request.urlretrieve(url, destination_filename)

