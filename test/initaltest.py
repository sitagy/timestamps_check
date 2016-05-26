fn = open("output_log.txt", "r")

for line in fn:
    if 'DllNotFoundException' in line:
        print(line)







