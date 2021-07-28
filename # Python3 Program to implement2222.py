# Python3 Program to implement
# the above approach

# Stores minimum-cost of path from source
minSum = 1000000000

# Function to Perform BFS on graph g
# starting from vertex v
def getMinPathSum(graph, visited, necessary,
				source, dest, currSum):
	
	global minSum
	
	# If destination is reached
	if (src == dest):
	
		# Set flag to true
		flag = True;

		# Visit all the intermediate nodes
		for i in necessary:

			# If any intermediate node
			# is not visited
			if (not visited[i]):
				flag = False;
				break;
	
		# If all intermediate
		# nodes are visited
		if (flag):

			# Update the minSum
			minSum = min(minSum, currSum);
		return;
	
	else:

		# Mark the current node
		# visited
		visited[src] = True;

		# Traverse adjacent nodes
		for node in graph[src]:
			
			if not visited[node[0]]:
			
				# Mark the neighbour visited
				visited[node[0]] = True;

				# Find minimum cost path
				# considering the neighbour
				# as the source
				getMinPathSum(graph, visited,
							necessary, node[0],
							dest, currSum + node[1]);

				# Mark the neighbour unvisited
				visited[node[0]] = False;
		
		# Mark the source unvisited
		visited[src] = False;

# Driver Code
if __name__=='__main__':
	
	# Stores the graph
	graph=dict()
		
	graph[0] = [ [ 1, 2 ], [ 2, 3 ], [ 3, 2 ] ];
	graph[1] = [ [ 4, 4 ], [ 0, 1 ] ];
	graph[2] = [ [ 4, 5 ], [ 5, 6 ] ];
	graph[3] = [ [ 5, 7 ], [ 0, 1 ] ];
	graph[4] = [ [ 6, 4 ] ];
	graph[5] = [ [ 6, 2 ] ];
	graph[6] = [ [ 7, 11 ] ];
	
	# Number of nodes
	n = 7;

	# Source
	source = 0;

	# Destination
	dest = 6;

	# Keeps a check on visited
	# and unvisited nodes
	visited=[ False for i in range(n + 1)]

	# Stores intemediate nodes
	necessary = [ 2, 4 ];

	getMinPathSum(graph, visited, necessary,
				source, dest, 0);

	# If no path is found
	if (minSum == 1000000000):
		print(-1)
	else:
		print(minSum)

		# This code is contributed by pratham76
