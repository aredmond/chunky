def chunker(input_file_name,chunksize=1048576):
	with open(input_file_name, 'r+b') as source:
		while True:
			buff = source.read(chunksize)
			if not buff:
				break
			yield buff

def unchunker(chunks, output_file_name):
	with open(output_file_name, 'w+b') as target:
		for chunk in chunks:
			target.write(chunk)

def file_split(data_file, count):
	with open(data_file, 'rb') as datafile:
             data = datafile.read()
        
        
        datasize = len(data)
	prefix, ftype = data_file.split('.')
	chunksize = datasize/count

        ## no need for remained, if it does not divide, 
        ## the last split point will be a fraction of a chunksize from the end
        ## ex. len(range(0,13,2) = 7   NOT   6
        splitpoints = range(0,datasize,chunksize)
        seriel_num = 1
        last_split = 0
        for split in splitpoints[1:]:
            with open((prefix + "_" + "split" + "_" + str(seriel_num)),'wb') as target:
                target.write(data[last_split:split])
            last_split = split
            seriel_num = seriel_num + 1
        ## Last chunk
        with open((prefix + "_" + "split" + "_" + str(seriel_num)),'wb') as target:
            target.write(data[splitpoints[-1]:])

file_split('data.bit', 4)
