amount = int(input('How many minutes has it been since midnight?'))
hour = int(amount/60)
minut = amount%60
Out = 'It has been {} hour(s) and {} minute(s) since midnight.'
print(Out.format(hour,minut))
out = "It is {}:{} o'clock"
print(out.format(hour,minut))