# Search-Algorithms
Search Algorithms
This is a variant of a classic "toy" search problem in AI.  Consider four poor robotic explorers who are down to their last power pack that they're sharing amongst themselves - all four robots are plugged into a single power pack.  Their home 'base' is a research station on the other side of a large chasm.  Fortunately for them, the chasm can be crossed by a narrow bridge.  Unfortunately, because the bridge is so narrow they can only cross in single file - and the wires on their power pack are only long enough for two of them to cross at a time with the power pack shared between them.

Our robotic explorers need to plan a path that will allow them to cross the chasm.  They can only cross in pairs and each pair can only move across if they are connected to the power pack.  Your assignment is to code the search algorithms that will allow them to search through all of the possible sequences of actions that they could take in order for all four exploration robots to get to the other side of the bridge and move on to their base, where they can settle down with free power packs for all.  The purpose for this assignment is for you to gain some more hands on familiarity with the basic breadth-first, depth-first, and uniform cost search algorithms, and to experience how heuristic-based algorithms like A* perform in comparison.

The Problem:
As discussed above, our four exploratory robots have found themselves tethered together on a single power pack and now need to cross a narrow bridge that spans an amazingly deep chasm.  In addition to the restriction that our explorers can only cross two at a time and only if they're carrying the power pack, there is the added problem that they all move at different maximum speeds:
	A1 can cross the bridge by itself in only 1 minute. 
	B2-D3 can cross it by itself in 2 minutes. 
	C3-P7 takes 5 minutes to cross the bridge.
	DB99 takes a full 10 minutes to cross it by himself.
If two robots cross together, they both can only move at the speed of the slowest robot in the pair.  And, of course, the power pack cannot cross the bridge by itself - at least one robot is needed to carry it across the bridge.

Your job is to implement 2 search algorithms to solve this problem.  You will need to write two different search agents:
	UCAgent: a uniform-cost search agent
	AStarAgent: an A* search agent
For A* search, you can use the heuristic that everyone moves at the same speed as the fastest robot. (Think: why is this admissible?). 
As with the previous project, you will need to write agent code AND Test Harness code.  The test harness for this code will call the search agent with some initial state as determined by the user running the program.  The test harness should read two strings from the command line as arguments to the program.  These two strings will contain the letters "ABCDP" for robots A-D assigned by the first letter of their names as given above and the power pack (P) - these strings will represent the initial conditions of the search.  The first string represents the robots/pack on the start side of the bridge, and the second is the set of robots (and possibly power pack) on the end side of the bridge. (This allows us to consider situations where the robots had screwed up the order of operations and need help planning how to finish up optimally.) For example:
	"ABCDP" "" : traditional start of puzzle where all robots and the power pack are on the start side
	"AC" "BDP" : a starting point where A and C are on the start side, but B and D have crossed with the power pack.
For ease of programming you can assume that the input is correctly defined -- all 5 letters occur only once in the two strings and P never appears alone.  As a check on your code, if all robots start on the same side with the power pack, everyone can cross the bridge in 17 minutes.
The agent should take the start state and return a list of actions that correspond to the optimal sequence from that state. Each piece of the code should write informational messages to the console:
	The test harness should report the list of actions for the solution given by the agent.
	The agent should report each node expanded off of the queue (which should include minimally state, parent state, relevant cost(s), and depth) at the end the number of nodes expanded in the search and the total path cost of the optimal path.
Once again, it may be helpful to utilize the pseudocode in the book or from the slides to help design your agent. Your program will be graded on whether it accepts input in the specified format from the command line. 
Define a class for state. You may represent the state in any way you choose but as a suggestion you might want to consider representing the state as an array of boolean variables - one for each robot and for the power pack - with a true value representing the robots on one side of the bridge and a false value representing the other side of the bridge.
You should provide the grader with two different programs to run, and they should be named "UCSearch" and "AstarSearch" for ease of grading.  They should output the node expansions and other information as indicated above and in the end provide a correct sequence of actions to move the robots across the bridge in 17 minutes.
