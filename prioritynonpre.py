# Each process has burst time and priority assigned to it. We will regard the arrival time column as priority column.

# Processes execute according to an order of priority; we have regarded lower value as higher priority.

#


def priononpre(pd):
	avgwait, avgturntime = 0,0
	waitingtime, turntime,wallclock = {},{},[]
	readyqueue = [[v[0],k] for k,v in pd.items()] #[arrival time, proc_num]
	readyqueue.sort()

	prioqueue = [[v[2],k] for k,v in pd.items()] #[prio_num, process_num]
	timer = readyqueue[0][0]
	wallclock.append([timer])
	while(len(readyqueue)):

		timer += pd[readyqueue[0][1]][1] # burst time 
		
		turntime[readyqueue[0][1]] = timer - readyqueue[0][0] # timer - arrival time
		waitingtime[readyqueue[0][1]] = turntime[readyqueue[0][1]] \
									- pd[readyqueue[0][1]][1] # turnaround - burst time
		wallclock.append([readyqueue[0][1],timer]) # timer 
		avgwait += waitingtime[readyqueue[0][1]]
		avgturntime += turntime[readyqueue[0][1]]
		
		if len(readyqueue)==1: # only one process remains 
			break

		qlinetil = [i for i in readyqueue[1:] if timer >= i[0]]

		minproc = min([ [ pd[i[1]][2],i[1] ] for i in qlinetil]) #process with minimum  [burst time, process number]

		nextinline = [i for i in readyqueue if i[1] == minproc[1]][0]
		readyqueue[0] = nextinline # assigning the process with the least burst at the begining of the array as the 0-th index has already been calculated.
		# print("in loop:", readyqueue,"need to delete:",nextinline)		

		del readyqueue[readyqueue.index(nextinline,1)] #deleting the min burst process at its old position in readyquee array.

	avgwait = avgwait/len(pd)
	avgturntime = avgturntime/len(pd)
	#print(waitingtime,turntime)

	combinedwaitturndict = {k:[waitingtime[k],turntime[k]] for k in waitingtime.keys()}
	return combinedwaitturndict, wallclock,avgwait,avgturntime


if __name__=='__main__':
	pd = {'1': [11, 2, 2], '2': [13, 13, 1], '3': [2, 10, 5], '4': [6, 5, 4], '5': [7, 4, 0]}
			#{'process name': [arrival(priority) time, burst time, prio_value]}

	priononpre(pd)
