anemometro = "00500 55125 025125 215"
temperatura = "5252 6336 50"
giro = "625L S555"

test_string="{} # {} # {}".format(anemometro,temperatura,giro)

print(test_string)

temp = test_string.split("#")
print(temp)
print("temperatura {}".format(temp[1]))
