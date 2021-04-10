# SJF: Shortest Job First selects the process with the least execution(burst) time.

# in a scenario where arrival time is 0 for all process then the queue is executed as per ascending order of burst time.


def sjfnonpre(pd):
	
	avgwait, avgturntime = 0,0
	waitingtime, turntime, wallclock = {},{},[]
	readyqueue = [[v[0],k] for k,v in pd.items()] #[arrival,'proc num']
	readyqueue.sort()
	# print(readyqueue)

	timer = readyqueue[0][0]
	wallclock.append([timer])	

	while(len(readyqueue)):

		timer += pd[readyqueue[0][1]][1] # burst time
		
		turntime[readyqueue[0][1]] = timer - readyqueue[0][0] # timer - arrival time
		waitingtime[readyqueue[0][1]] = turntime[readyqueue[0][1]] \
									- pd[readyqueue[0][1]][1] # turnaround - burst time
		wallclock.append([readyqueue[0][1], timer]) # timer 
		avgwait += waitingtime[readyqueue[0][1]]
		avgturntime += turntime[readyqueue[0][1]]
		
		if len(readyqueue)==1: # only one process remains 
			break
		
		qlinetil = [i for i in readyqueue[1:] if timer >= i[0]]

		minburst = min([ [ pd[i[1]][1],i[1] ] for i in qlinetil]) #process with minimum  [burst time, process number]

		nextinline = [i for i in readyqueue if i[1] == minburst[1]][0]
		readyqueue[0] = nextinline # assigning the process with the least burst at the begining of the array as the 0-th index has already been calculated.
		# print("in loop:", readyqueue,"need to delete:",nextinline)		

		del readyqueue[readyqueue.index(nextinline,1)] #deleting the min burst process at its old position in readyquee array.

	avgwait = avgwait/len(pd)
	avgturntime = avgturntime/len(pd)
	#print(waitingtime,turntime)
	print("wallclock: ", wallclock)


	combinedwaitturndict = {k:[waitingtime[k],turntime[k]] for k in waitingtime.keys()}
	return combinedwaitturndict, wallclock,avgwait,avgturntime
	
if __name__=='__main__':
	pd = {'1': [11, 2], '2': [13, 13], '3': [2, 10], '4': [6, 5], '5': [7, 4]}
			#{'process name': [arrival time, burst time]}

	sjfnonpre(pd)

