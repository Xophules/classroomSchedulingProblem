# Name: Xophules
# Date: 10/6/17
# Vers: 1.1
# Desc: A greedy algorithm for the class scheduling problem. Modified for the correct output


import heapq
import datetime


def scheduleRooms(rooms, cls):
	orderedcls = [(cls[item][0], cls[item][1], item) for item in cls]  # Append the classname to the list
	heapq.heapify(orderedcls) # Turn list into a pQue

	sched = {}
	while orderedcls:
		i = heapq.heappop(orderedcls)  # Pull off pQue Earliest class
		for j in rooms:  # Iterate to find an empty room
			if j not in sched:  # No classes instantiated yet
				sched[j] = [i]
				break
			if sched[j][len(sched[j]) - 1][1] <= i[0]:  # Find if prev class before class i starts
				sched[j].append(i)
				break
		else:  # Proud of this solution. https://github.com/satwikkansal/wtfpython#yes-it-exists
			print "Not enough rooms. The class", i[2], "did not fit into any rooms. Exiting function... "
			return 0

	return {i: [cl[2] for cl in sched[i]] for i in sched} # Pull the start and end times out of the dictionary


if __name__ == "__main__":
	cl1 = {"a": (datetime.time(9), datetime.time(10, 30)),
		   "b": (datetime.time(9), datetime.time(12, 30)),
		   "c": (datetime.time(9), datetime.time(10, 30)),
		   "d": (datetime.time(11), datetime.time(12, 30)),
		   "e": (datetime.time(11), datetime.time(14)),
		   "f": (datetime.time(13), datetime.time(14, 30)),
		   "g": (datetime.time(13), datetime.time(14, 30)),
		   "h": (datetime.time(14), datetime.time(16, 30)),
		   "i": (datetime.time(15), datetime.time(16, 30)),
		   "j": (datetime.time(15), datetime.time(16, 30))}
	rm1 = [1, 2, 3]
	print cl1
	print scheduleRooms(rm1, cl1)

	print scheduleRooms([1, 2], cl1)
	ensrooms = ['KEH U1', 'KEH M1', 'KEH M2', 'KEH M3', 'KEH U2', 'KEH U3', 'KEH U4', 'KEH M4', 'KEH U8', 'KEH U9']
	csclasses = {'CS 1043': (datetime.time(9, 30), datetime.time(11)),
				 'CS 2003': (datetime.time(10, 30), datetime.time(12)),
				 'CS 2123': (datetime.time(11, 15), datetime.time(12, 45)),
				 'CS 3003': (datetime.time(8, 15), datetime.time(11, 30)),
				 'CS 3353': (datetime.time(11), datetime.time(12)),
				 'CS 4013': (datetime.time(13), datetime.time(14, 45)),
				 'CS 4063': (datetime.time(12, 30), datetime.time(14, 30)),
				 'CS 4123': (datetime.time(14), datetime.time(15)),
				 'CS 4163': (datetime.time(14), datetime.time(16, 30)),
				 'CS 4253': (datetime.time(12), datetime.time(16)),
				 }
	print csclasses
	print scheduleRooms(ensrooms, csclasses)
	print scheduleRooms(ensrooms[:4], csclasses)

