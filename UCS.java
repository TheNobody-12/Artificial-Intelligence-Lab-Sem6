import java.util.Comparator; 
import java.util.HashSet; 
import java.util.InputMismatchException; 
import java.util.Iterator; 
import java.util.LinkedList; 
import java.util.PriorityQueue; 
import java.util.Scanner; 
import java.util.Set; 


public class UCS { 
 String[] c = {"0","s","a","b","c","d","e","f","g1","g2","g3"}; 
 private final PriorityQueue<Node> priorityQueue; 
 private final Set<Integer> settled; 
 private final int[] distances; 
 private final int numberOfNodes; 
 private final int[][] adjacencyMatrix; 
 private final LinkedList<Integer> path; 
 private final int[] parent; 
 private int source, destination; 
 public static final int MAX_VALUE = 999; 
 public UCS(int numberOfNodes) { 
 this.numberOfNodes = numberOfNodes; 
 this.settled = new HashSet<Integer>(); 
 this.priorityQueue = new PriorityQueue<>(numberOfNodes, new 
Node()); 
 this.distances = new int[numberOfNodes + 1]; 
 this.path = new LinkedList<Integer>(); 
 this.adjacencyMatrix = new int[numberOfNodes + 1][numberOfNodes + 
1]; 
 this.parent = new int[numberOfNodes + 1]; 
 } 
 public int uniformSearch(int[][] adjacencyMatrix, int source, int 
destination){ 
 int evaluationNode; 
 this.source = source; 
 this.destination = destination; 
 for (int i = 1; i <= numberOfNodes; i++) distances[i] = MAX_VALUE; 
 for (int sourcevertex = 1; sourcevertex <= numberOfNodes; 
sourcevertex++) 
 for (int destinationvertex = 1; destinationvertex <= 
numberOfNodes; destinationvertex++) 
 this.adjacencyMatrix[sourcevertex][destinationvertex] = 
adjacencyMatrix[sourcevertex][destinationvertex]; 
 priorityQueue.add(new Node(source, 0)); 
 distances[source] = 0; 
 while (!priorityQueue.isEmpty()){ 
 evaluationNode = getNodeWithMinDistanceFromPriorityQueue(); 
 System.out.print(evaluationNode+"\t"); 
 if (evaluationNode == destination) return 
distances[destination]; 
 settled.add(evaluationNode); 
 addFrontiersToQueue(evaluationNode); 
 } 
 return distances[destination]; 
 } 
 private void addFrontiersToQueue(int evaluationNode) { 
 for (int destination = 1; destination <= numberOfNodes; 
destination++) { 
 if (!settled.contains(destination)) { 
 if (adjacencyMatrix[evaluationNode][destination] != 
MAX_VALUE) { 
 if (distances[destination] > 
adjacencyMatrix[evaluationNode][destination] + distances[evaluationNode]) { 
 distances[destination] = 
adjacencyMatrix[evaluationNode][destination] 
 + distances[evaluationNode]; 
 parent[destination] = evaluationNode; 
 } 
 Node node = new Node(destination, 
distances[destination]); 
 priorityQueue.remove(node); 
priorityQueue.add(node); 
 } 
 } 
 } 
 } 
 private int getNodeWithMinDistanceFromPriorityQueue(){ 
 Node node = priorityQueue.remove(); 
 return node.node; 
 } 
 public void printPath(){ 
 path.add(destination); 
 boolean found = false; 
 int vertex = destination; 
 while (!found){ 
 if (vertex == source){ 
 found = true; 
 continue; 
 } 
 path.add(parent[vertex]); 
 vertex = parent[vertex]; 
 } 
 System.out.println(); 
 System.out.println("The Path between " + c[source] + " and " + 
c[destination]+ " is "); 
 Iterator<Integer> iterator = path.descendingIterator(); 
 while (iterator.hasNext()) 
 System.out.print(iterator.next() + "\t"); 
 } 
 public static void main(String... arg){ 
 int[][] adjacency_matrix;int number_of_vertices; 
 int source = 0;int destination = 0; 
 int distance; 
 Scanner scan = new Scanner(System.in); 
 try{ 
 System.out.println("Enter the number of vertices"); 
 number_of_vertices = scan.nextInt(); 
 adjacency_matrix = new 
int[number_of_vertices+1][number_of_vertices + 1]; 
 System.out.println("Enter the Weighted Matrix for the graph"); 
 for (int i = 1; i <= number_of_vertices; i++){ 
 for (int j = 1; j <= number_of_vertices; j++){ 
 adjacency_matrix[i][j] = scan.nextInt(); 
if (i == j) { 
 adjacency_matrix[i][j] = 0;continue; 
 } 
 if (adjacency_matrix[i][j] == 0) adjacency_matrix[i][j] 
= MAX_VALUE; 
 } 
 } 
 System.out.println("Enter the source "); 
 source = scan.nextInt(); 
 System.out.println("Enter the destination"); 
 destination = scan.nextInt(); 
 UCS uniformCostSearch = new 
UCS(number_of_vertices); 
 distance = 
uniformCostSearch.uniformSearch(adjacency_matrix,source, destination); 
 uniformCostSearch.printPath(); 
 System.out.println("\nThe Distance between source " + 
uniformCostSearch.c[source] + 
 " and destination " + uniformCostSearch.c[destination] 
+ " is " + distance); 
 } catch (InputMismatchException inputMismatch) { 
 System.out.println("Wrong Input Format"); 
 } 
 scan.close(); 
 } 
} 
class Node implements Comparator<Node> { 
 public int node,cost; 
 public Node(){} 
 public Node(int node, int cost){ 
 this.node = node;this.cost = cost; 
 } 
 @Override 
 public int compare(Node node1, Node node2){ 
 if (node1.cost < node2.cost) return -1; 
 if (node1.cost > node2.cost) return 1; 
 if (node1.node < node2.node) return -1; 
 return 0; 
 } 
 @Override 
 public boolean equals(Object obj){ 
 if (obj instanceof Node){ 
 Node node = (Node) obj; 
 return this.node == node.node; 
 } 
 return false; 
 } 
} 

/*
0 5 9 0 6 0 0 0 0 0
0 0 3 0 0 0 0 9 0 0
0 2 0 1 0 0 0 0 0 0
6 0 0 0 0 0 7 0 5 0
0 0 0 2 0 2 0 0 0 0
0 0 0 0 0 0 0 0 0 7
0 0 0 0 2 0 0 0 0 8
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
*/