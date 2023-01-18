from collections import defaultdict

jug1 = int(input("Enter the capacity of jug 1 : "))
jug2 = int(input("Enter the capacity of jug 2 : "))
goal1  = int(input("Enter the capacity of goal1 : "))
goal2  = int(input("Enter the capacity of goal2 : "))

visited = defaultdict(lambda: False)

def waterJugSolver(amount1, amount2):

	if (amount1 == goal1 and amount2 == goal2):
		print(amount1, amount2)
		return True
	
	if visited[(amount1, amount2)] == False:
		print(amount1, amount2)
	
		visited[(amount1, amount2)] = True
	
		return (waterJugSolver(0, amount2) or
				waterJugSolver(amount1, 0) or
				waterJugSolver(jug1, amount2) or
				waterJugSolver(amount1, jug2) or
				waterJugSolver(amount1 + min(amount2, (jug1-amount1)),
				amount2 - min(amount2, (jug1-amount1))) or
				waterJugSolver(amount1 - min(amount1, (jug2-amount2)),
				amount2 + min(amount1, (jug2-amount2))))
	
	else:
		return False

waterJugSolver(0, 0)