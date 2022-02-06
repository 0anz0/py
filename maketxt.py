for i in range(5):
    file_name = '0000_0000_0000_' + str(i+1).zfill(6) +'.dkkey'
    with open(file_name, 'w') as f:
        f.write('test')