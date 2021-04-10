# AKA Shortest Remainig
# Shortest Job first has the advantage of having a minimum average waiting time among all scheduling algorithms.
# It is practically infeasible as Operating System may not know burst time and therefore may not sort them

# processes will always run until they complete OR a new process is added that requires a smaller amount of time.


def sjfpre(pd):

	avgwait, avgturntime = 0,0
	waitingtime, turntime, wallclock = {},{},[]
	readyqueue = [[v[0],v[1],k] for k,v in pd.items()] #[arrival,burst,'proc num']
	readyqueue.sort()
	print(readyqueue)

	timer = readyqueue[0][0]
	wallclock.append([timer])
	current = readyqueue[0]

	# for indx,i in enumerate(readyqueue): # [[2, 10, '3'], [6,	5, '4'], [7, 4, '5'], [11, 2, '1'], [13, 13, '2']]
	
	while(len(readyqueue)):
		# timer = current[0]
		restart = False
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
			readyqueue.sort() # it can be sorted according to burst time.


		# print("current: ", current)
		if current[1] - (second[0] - current[0]) > second[1]: #the second process take over.
			# print("second process taking over: ",second)
			timer += second[0] - current[0]
			wallclock.append([current[2], timer])

			readyqueue[indx] = [0,readyqueue[indx][1] - (second[0] - current[0]),readyqueue[indx][2]]
			current = second

		else: # the current is clear to finish...or is it ? #[[2, 6, '3'], [6, 5, '4'], [7, 4, '5'], [11, 2, '1'], [13, 13, '2']]

			qline = [i for i in readyqueue if i[0] < (current[0] + current[1]) ]
			for i in qline:
				# print("checking for i:" ,i)
				if i[1] < current[1] - abs(i[0] - current[0]): # a process that will take over

					timer += i[0] - current[0]
					wallclock.append([current[2], timer])

					readyqueue[indx] = [0, readyqueue[indx][1] - (i[0] - current[0]),readyqueue[indx][2]]
					# need to have turntime entries.
					current = i
					restart = True
					break
			# print(wallclock)
			if restart: # a shorter process have been found.
				continue
			# now the current process is clear to finish.
			# print(current," is clear to finish")
			timer += current[1]
			wallclock.append([current[2], timer])
			turntime[current[2]] = timer - pd[current[2]][0] # timer - arrival time
			waitingtime[current[2]] = turntime[current[2]]- pd[current[2]][1] 

			del readyqueue[indx]
			# turnaround - burst time

	# avgwait += waitingtime[readyqueue[0][1]]

	for k,v in waitingtime.items():
		avgwait += v
	avgwait= avgwait/len(waitingtime)
	
	for k,v in turntime.items():
		avgturntime += v
	avgturntime = avgturntime/len(turntime)
	
	#print(waitingtime,turntime)
	print("wallclock: ", wallclock)
	
	combinedwaitturndict = {k:[waitingtime[k],turntime[k]] for k in waitingtime.keys()}
	return combinedwaitturndict, wallclock,avgwait,avgturntime

if __name__=='__main__':
	pd = {'1': [8, 2], '2': [13, 13], '3': [2, 10], '4': [6, 5], '5': [7, 4]}
	# pd = {'1': [4, 5], '2': [1, 2], '3': [6, 4], '4': [2, 1], '5': [7, 2]} 
			#{'process name': [arrival time, burst time]}
	sjfpre(pd)


