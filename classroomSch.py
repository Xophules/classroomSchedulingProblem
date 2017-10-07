# Name: Xophules
# Date: 10/6/17
# Vers: 1.0
# Desc: A greedy algorithm for the class scheduling problem


import heapq


def scheduleRooms(rooms, cls):
	orderedcls = []  # Convert the time to seconds for easy comparison
	for i in cls:
		(h, m) = cls[i][0].split(':')
		result1 = int(h) * 3600 + int(m) * 60
		(h, m) = cls[i][1].split(':')
		result2 = int(h) * 3600 + int(m) * 60
		heapq.heappush(orderedcls, (result1, result2, i))  # Add to pQue

	# print
	sched = {}
	while orderedcls:
		i = heapq.heappop(orderedcls)  # Pull off pQue
		for j in rooms:  # Iterate to find an empty room
			if j not in sched:  # No classes instantiated yet
				# print i
				sched[j] = [i]
				break
			if sched[j][len(sched[j]) - 1][1] < i[0]:  # Find if prev class before class i starts
				sched[j].append(i)
				break
		else:  # Proud of this solution. https://github.com/satwikkansal/wtfpython#yes-it-exists
			print("Not enough rooms")
			print "The class", i[2], "Did not fit into any rooms"
			print "Exiting fuction... "
			return 0

	# All this does is to convert from sec to normal military time format
	for i in sched:
		for j in range(0, len(sched[i])):
			q = sched[i][j]
			m, _ = divmod(q[0], 60)
			h, m = divmod(m, 60)
			m1, _ = divmod(q[1], 60)
			h1, m1 = divmod(m1, 60)
			sched[i][j] = (q[2], "%d:%02d" % (h, m), "%d:%02d" % (h1, m1))

	return sched


if __name__ == "__main__":
	NumberOfClassRooms = 4  # Change the number of Classrooms
	rooms = ["c" + str(i) for i in range(0, NumberOfClassRooms)]  # ["c1", "c2", "c3", "c4"]
	classes = {"Com": ["7:15", "8:45"],
			   "Bio": ["7:00", "8:30"],
			   "Chem": ["9:00", "11:00"],
			   "Phys": ["9:45", "12:00"],
			   "Art": ["8:00", "9:30"],
			   "Bis": ["9:00", "10:30"],
			   "Wrt": ["12:00", "14:00"]}

	print scheduleRooms(rooms, classes)
