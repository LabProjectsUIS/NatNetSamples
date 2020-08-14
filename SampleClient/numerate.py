def numerate(in_file, out_file):


    data = open(out_file, 'w')
    numel = 0
    with open(in_file, 'r') as file:
        for line in file:
            data.write(str(numel) + '\t' + line)
            numel+=1
			
    data.close()
	
if __name__ == "__main__":
    in_file = raw_input("input file: ")
    out_file = raw_input("output file: ")
    numerate(in_file, out_file)