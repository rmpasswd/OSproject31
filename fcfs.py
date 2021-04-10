# fcfs means that the processes will execute as per their arrival time. It is a non-preemptive scheduling algorithm; meaning that each process will hold the cpu till it finishes or goes to i/o state. 
# a fifo queue required to properly execute a fcfs algo. A ready queue in the order of 'arrival time'. Average  time in fcfs is too long.

#this program calculates waiting time, turnaround time (from wall-clock-0 to completion !) of each process; and average waiting time and turnaround time.

#completion time: the wall clock count when a process is finally done.
#turnaround time: diff between arrival time and completion time. becuz a process may halt and resume the arrival time - complettion time isn't always = burst time.
#waiting time: diff between turnaround time and burst time.

def fcfs(pd):
	
	avgwait, avgturntime = 0,0
	waitingtime, turntime,wallclock = {},{},[]
	readyqueue = [[v[0],k] for k,v in pd.items()]
	readyqueue.sort()
		#sorted by arrival time # [...,[arrival time,'proc name'] ,...]
	timer = readyqueue[0][0] # starting the clock from 0 or the first arrival time
	wallclock.append([timer])
	for i in readyqueue: # [[3,'1'],[9,'2']]
		timer += pd[i[1]][1] # burst time 

		turntime[i[1]] = timer - i[0]
		waitingtime[i[1]] = turntime[i[1]] - pd[i[1]][1]
		wallclock.append([i[1], timer])

		avgwait+= waitingtime[i[1]]
		avgturntime+= turntime[i[1]]
		# print("proc.name",i,"\n",)

	avgwait = avgwait/len(pd)
	avgturntime = avgturntime/len(pd)
	#print(waitingtime,turntime)


	combinedwaitturndict = {k:[waitingtime[k],turntime[k]] for k in waitingtime.keys()}
	return combinedwaitturndict, wallclock,avgwait,avgturntime

if __name__=='__main__':
	pd = {'1': [0, 5], '2': [3, 9], '3': [6, 6]} 
			#{'process name': [arrival time, burst time]}

	fcfs(pd)