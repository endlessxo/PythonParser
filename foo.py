f = open("part.txt", 'r')
out = f.readlines()


for a in out:
	begin = 0
	for i in range (0, len(a)):
		
		end = 1
		if a[i:i+6] == "text='":
			begin = i+6
		if a[i:i+11] == "', source='":
			end = i		
			try:
				#print begin
				#print end
				print a[begin:end]
			except:
				print "i tried so hard"

