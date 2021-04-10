# The process that have just arrived and has higher priority will take over the running process.



def priopre(pd):

	restart = False
	avgwait, avgturntime = 0,0
	waitingtime, turntime, wallclock = {},{},[]
	readyqueue = [[v[0],v[2],v[1],k] for k,v in pd.items()] #[arrival,prio,burst,'proc num']
	readyqueue.sort()
	# print(readyqueue)

	timer = readyqueue[0][0]
	wallclock.append([timer])
	current = readyqueue[0]
	
	while(len(readyqueue)):
		restart=False
		if timer>=readyqueue[-1][0]:
			for i in readyqueue:
				i[0]=0

		try:
			indx = readyqueue.index(current) # [8,2] dont exist no more
		except Exception as e:
			readyqueue.sort()
			current = readyqueue[0]
			indx = readyqueue.index(current)


		try:
		 	second = readyqueue[indx+1]

		except Exception as IndexError:
			for i,j in enumerate(readyqueue):
				readyqueue[i][0]=0 # setting arrival time=0 so that...
			readyqueue.sort() # it can be sorted according to priority num.

		# print(current)
		qline = [i for i in readyqueue if i[0]<(current[0]+current[2])]  # procs that arrive before current finishes. checking if any of them have higher prio(lower prionum)
		# print(qline)
		for i in qline:
			if i[1] < current[1]: # found a higher priority proc

				timer += i[0] - current[0]
				wallclock.append([current[3], timer])

				readyqueue[indx] = [0,readyqueue[indx][1], readyqueue[indx][2] - (i[0] - current[0]),readyqueue[indx][3]]
				# need to have turntime entries.
				current = i
				restart = True
				break

		if restart: # a shorter process have been found.
			continue
		# now the current process is clear to finish.
		# print(current," is clear to finish")
		timer += current[2]
		wallclock.append([current[3], timer])
		turntime[current[3]] = timer - pd[current[3]][0] # timer - arrival time
		waitingtime[current[3]] = turntime[current[3]]- pd[current[3]][1] 

		del readyqueue[indx]
	# print(waitingtime)
	for k,v in waitingtime.items():
		avgwait += v
	avgwait= avgwait/len(waitingtime)
	
	for k,v in turntime.items():
		avgturntime += v
	avgturntime = avgturntime/len(turntime)
	
	#print(waitingtime,turntime)
	# print("wallclock: ", wallclock)

	combinedwaitturndict = {k:[waitingtime[k],turntime[k]] for k in waitingtime.keys()}
	return combinedwaitturndict, wallclock,avgwait,avgturntime

if __name__=='__main__':
	pd = {'1': [4, 5, 1], '2': [1, 2, 4], '3': [6, 4, 3], '4': [2, 1, 2], '5': [7, 2, 5]}
			#{'process name': [arrival(priority) time, burst time, prio_value]}

	priopre(pd)

