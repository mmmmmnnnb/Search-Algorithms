from itertools import combinations 
import operator
#Author Tianyu Jin
#An A star Agent
#class Node
class Node:
    def __init__(self, cost, depth, PositionA, PositionB, PositionC, PositionD, 
PositionP):
        self.PositionA = PositionA
        self.PositionB = PositionB
        self.PositionC = PositionC
        self.PositionD = PositionD
        self.PositionP = PositionP
        self.parent = None
        self.depth = depth
        self.heuristic = 4
        if PositionA:
            self.heuristic -= 1
        if PositionD:
            self.heuristic -= 1
        if PositionC:
            self.heuristic -= 1
        if PositionD:
            self.heuristic -= 1
        
        self.cost = cost
        self.GandH = self.cost + self.heuristic
    
    #print the information of each node expanded
    def getstring(self):
        
        start = " Expanding: Starting point: "
        end = " Destination: "
        strcost = " Cost: " + str(self.cost)
        strheu = " Heuristic: " + str(self.heuristic)
        strDepth = " Depth: "+ str(self.depth)
        parentstate = ""
        if(self.PositionA == False):
            start = start + "A"
        else:
            end = end + "A"
        if(self.PositionB == False):
            start = start + "B"
        else:
            end = end + "B"
        if(self.PositionC == False):
            start = start + "C"
        else:
            end = end + "C"
        if(self.PositionD == False):
            start = start + "D"
        else:
            end = end + "D"
        if(self.PositionP == False):
            start = start + "P"
        else:
            end = end + "P"
        
        if (self.parent == None):
            parentstate = " Parent State: None "
        else:
            parentstart = "Starting Point: "
            parentend = " Destination: "
            parentstate = "Parent State: "
            if(self.parent.PositionA == False):
                parentstart = parentstart + "A"
            else:
                parentend = parentend + "A"
            if(self.parent.PositionB == False):
                parentstart = parentstart + "B"
            else:
                parentend = parentend + "B"
            if(self.parent.PositionC == False):
                parentstart = parentstart + "C"
            else:
                parentend = parentend + "C"
            if(self.parent.PositionD == False):
                parentstart = parentstart + "D"
            else:
                parentend = parentend + "D"
            if(self.parent.PositionP == False):
                parentstart = parentstart + "P"
            else:
                parentend = parentend + "P"
            parentstate = parentstate + parentstart + parentend
        string = start + end + strcost + strheu + strDepth + "\n" + parentstate
        return(string)
    
    # put children in the frontier
    def putFrontier(self, frontier, explored):
        
        avilable = []
        #robot movable if on the same side with battery
        if self.PositionA == self.PositionP:
                
            
            avilable.append("A")
                
        if self.PositionB == self.PositionP:
                
            
            avilable.append("B")
                
        if self.PositionC == self.PositionP:
                
            
            avilable.append("C")
                
        if self.PositionD == self.PositionP:
                
            
            avilable.append("D")
        #use the python combination algorithm and calculate the possible movements.
        
        comb1 = combinations(avilable, 1)
        comb2 = combinations(avilable, 2)
        #handle single movement situation
        for character in list(comb1):
            if character == ('A',):
                exist = False
                newNode = Node(self.cost + 1, self.depth + 1, not self.PositionA, 
self.PositionB, self.PositionC, self.PositionD, not self.PositionP)
                newNode.parent = self
                if len(explored) == 0:
                    frontier.append(newNode)
                for node in list(explored):
                    if (node.PositionA == newNode.PositionA) and (node.PositionB ==
newNode.PositionB) and (node.PositionC == newNode.PositionC) and (node.PositionD ==
newNode.PositionD) and (node.PositionP == newNode.PositionP):
                        exist = True
                if not exist:
                    frontier.append(newNode)
                
            if character == ('B',):
                exist = False
                newNode = Node(self.cost + 2, self.depth + 1, self.PositionA, not 
self.PositionB, self.PositionC, self.PositionD, not self.PositionP)
                newNode.parent = self
                if len(explored) == 0:
                    frontier.append(newNode)
                for node in list(explored):
                    if (node.PositionA == newNode.PositionA) and (node.PositionB ==
newNode.PositionB) and (node.PositionC == newNode.PositionC) and (node.PositionD ==
newNode.PositionD) and (node.PositionP == newNode.PositionP):
                        exist = True
                if not exist:
                    frontier.append(newNode)
                
            if character == ('C',):
                exist = False
                newNode = Node(self.cost + 5, self.depth + 1, self.PositionA, 
self.PositionB, not self.PositionC, self.PositionD, not self.PositionP)
                newNode.parent = self
                if len(explored) == 0:
                    frontier.append(newNode)
                for node in list(explored):
                    if (node.PositionA == newNode.PositionA) and (node.PositionB ==
newNode.PositionB) and (node.PositionC == newNode.PositionC) and (node.PositionD ==
newNode.PositionD) and (node.PositionP == newNode.PositionP):
                        exist = True
                if not exist:
                    frontier.append(newNode)
            if character == ('D',):
                exist = False
                newNode = Node(self.cost + 10, self.depth + 1, self.PositionA, 
self.PositionB, self.PositionC, not self.PositionD, not self.PositionP)
                newNode.parent = self
                if len(explored) == 0:
                    frontier.append(newNode)
                for node in list(explored):
                    if (node.PositionA == newNode.PositionA) and (node.PositionB ==
newNode.PositionB) and (node.PositionC == newNode.PositionC) and (node.PositionD ==
newNode.PositionD) and (node.PositionP == newNode.PositionP):
                        exist = True
                if not exist:
                    frontier.append(newNode)
        
        #handle double movement situation
        for situation in list(comb2):
            if situation == ('A','B'):
                exist = False
                newNode = Node(self.cost + 2, self.depth + 1, not self.PositionA, 
not self.PositionB, self.PositionC, self.PositionD, not self.PositionP)
                newNode.parent = self
                if len(explored) == 0:
                    frontier.append(newNode)
                for node in list(explored):
                    if (node.PositionA == newNode.PositionA) and (node.PositionB ==
newNode.PositionB) and (node.PositionC == newNode.PositionC) and (node.PositionD ==
newNode.PositionD) and (node.PositionP == newNode.PositionP):
                        exist = True
                if not exist:
                    frontier.append(newNode)
            if situation == ('A','C'):
                exist = False
                newNode = Node(self.cost + 5, self.depth + 1, not self.PositionA,  
self.PositionB, not self.PositionC, self.PositionD, not self.PositionP)
                newNode.parent = self
                if len(explored) == 0:
                    frontier.append(newNode)
                for node in list(explored):
                    if (node.PositionA == newNode.PositionA) and (node.PositionB ==
newNode.PositionB) and (node.PositionC == newNode.PositionC) and (node.PositionD ==
newNode.PositionD) and (node.PositionP == newNode.PositionP):
                        exist = True
                if not exist:
                    frontier.append(newNode)
            if situation == ('A','D'):
                exist = False
                newNode = Node(self.cost + 10, self.depth + 1, not self.PositionA, 
self.PositionB, self.PositionC, not self.PositionD, not self.PositionP)
                newNode.parent = self
                if len(explored) == 0:
                    frontier.append(newNode)
                for node in list(explored):
                    if (node.PositionA == newNode.PositionA) and (node.PositionB ==
newNode.PositionB) and (node.PositionC == newNode.PositionC) and (node.PositionD ==
newNode.PositionD) and (node.PositionP == newNode.PositionP):
                        exist = True
                if not exist:
                    frontier.append(newNode)
            if situation == ('B','C'):
                exist = False
                newNode = Node(self.cost + 5, self.depth + 1, self.PositionA, not 
self.PositionB, not self.PositionC, self.PositionD, not self.PositionP)
                newNode.parent = self
                if len(explored) == 0:
                    frontier.append(newNode)
                for node in list(explored):
                    if (node.PositionA == newNode.PositionA) and (node.PositionB ==
newNode.PositionB) and (node.PositionC == newNode.PositionC) and (node.PositionD ==
newNode.PositionD) and (node.PositionP == newNode.PositionP):
                        exist = True
                if not exist:
                    frontier.append(newNode)
            if situation == ('B','D'):
                exist = False
                newNode = Node(self.cost + 10, self.depth + 1, self.PositionA, not 
self.PositionB, self.PositionC, not self.PositionD, not self.PositionP)
                newNode.parent = self
                if len(explored) == 0:
                    frontier.append(newNode)
                for node in list(explored):
                    if (node.PositionA == newNode.PositionA) and (node.PositionB ==
newNode.PositionB) and (node.PositionC == newNode.PositionC) and (node.PositionD ==
newNode.PositionD) and (node.PositionP == newNode.PositionP):
                        exist = True
                if not exist:
                    frontier.append(newNode)
            if situation == ('C','D'):
                exist = False
                newNode = Node(self.cost + 10, self.depth + 1, self.PositionA, 
self.PositionB, not self.PositionC, not self.PositionD, not self.PositionP)
                newNode.parent = self
                if len(explored) == 0:
                    frontier.append(newNode)
                for node in list(explored):
                    if (node.PositionA == newNode.PositionA) and (node.PositionB ==
newNode.PositionB) and (node.PositionC == newNode.PositionC) and (node.PositionD ==
newNode.PositionD) and (node.PositionP == newNode.PositionP):
                        exist = True
                if not exist:
                    frontier.append(newNode)
class nodeTree:
    def __init__(self):
        self.root = None
# the agent
class UCAgent:
    def Search(self, startString, endString):
        
        frontier = []
        actions = []
        explored = []
        path = []
        
        done = False
        PositionA = False
        PositionB = False
        PositionC = False
        PositionD = False
        PositionP = False
        
        
        #check where the robots are
        if startString.find('A') == -1:
        
            PositionA = True
        
        if startString.find('B') == -1:
        
            PositionB = True
        
        if startString.find('C') == -1:
        
            PositionC = True
        
        if startString.find('D') == -1:
        
            PositionD = True
        
        if startString.find('P') == -1:
        
            PositionP = True
        
        tree = nodeTree()
        initialNode = Node(0, 0, PositionA, PositionB, PositionC, PositionD, 
PositionP)
        currentNode = initialNode
        finalNode = None
        tree.root = initialNode
        frontier.append(initialNode)
        #done when all the robots have cross the bridge
        while done == False:
        
            if len(frontier) == 0:
                actions.append("Failed")
                return(actions)
            
            if PositionA and PositionB and PositionC and PositionD:
            
                done = True
                print("...Path found.")
                
            else:
            #robot movable if on the same side with battery
                
                
                frontier.sort(key=operator.attrgetter('GandH'))
                #expand the node with smallest time cost.
                currentNode = frontier[0]
                del frontier[0]
                #the information of expanding 
                expanding = currentNode.getstring()
                print(expanding)
                currentNode.putFrontier(frontier, explored)
                explored.append(currentNode)
                #check where the robots are
                PositionA = currentNode.PositionA
                PositionB = currentNode.PositionB
                PositionC = currentNode.PositionC
                PositionD = currentNode.PositionD
                PositionP = currentNode.PositionP
        
        finalNode = currentNode
        # print the information after searching
        print("The number of node expanded: ", len(explored))
        print("The cost of path is: ", finalNode.cost )
        node = finalNode
        
        #place nodes in the path
        while not (node == None):
            path.append(node)
            node = node.parent
        
        path.sort(key=operator.attrgetter('depth'))
        i = 0
        #determine movements in each step by comparing list of nodes
        while i != finalNode.depth:
            thisNode = path[i]
            nextNode = path[i + 1]
            action = ""
            if thisNode.PositionP:
                action = action + "Come back: "
            
            else:
                action = action + "Go across: "
            if thisNode.PositionA != nextNode.PositionA:
                action = action + "A"
            
            if thisNode.PositionB != nextNode.PositionB:
                action = action + "B"
            
            if thisNode.PositionC != nextNode.PositionC:
                action = action + "C"
            
            if thisNode.PositionD != nextNode.PositionD:
                action = action + "D"
            action = action + "P"
            actions.append(action)
            i = i + 1
            
        return actions
       
#test harness
agent = UCAgent()
#Ask for initial state
InputString1 = input("Please enter the first string: ")
InputString2 = input("Please enter the second string: ")
actions = agent.Search(InputString1, InputString2)
print("The movements:")
for action in list(actions):
    print (action)
