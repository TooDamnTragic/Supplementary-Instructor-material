import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

/*
    (Djikastra's)
    Find the shortest path from vertex A to vertex E in the given graph.
*/

class Graph {
    private final Map<String, Map<String, Integer>> adjList = new HashMap<>();

    public void addEdge(String from, String to, int weight) {
        adjList.computeIfAbsent(from, k -> new HashMap<>()).put(to, weight);
        adjList.computeIfAbsent(to, k -> new HashMap<>()).put(from, weight);
    }

    public Map<String, Integer> dijkstra(String start) {
        PriorityQueue<Map.Entry<String, Integer>> queue = new PriorityQueue<>(Map.Entry.comparingByValue());
        Map<String, Integer> distances = new HashMap<>();
        adjList.keySet().forEach(node -> distances.put(node, Integer.MAX_VALUE));

        distances.put(start, 0);
        queue.add(Map.entry(start, 0));

        while (!queue.isEmpty()) {
            String current = queue.poll().getKey();

            for (var entry : adjList.get(current).entrySet()) {
                String neighbor = entry.getKey();
                int newDist = distances.get(current) + entry.getValue();

                if (newDist < distances.get(neighbor)) {
                    distances.put(neighbor, newDist);
                    queue.add(Map.entry(neighbor, newDist));
                }
            }
        }

        return distances;
    }

    public static void main(String[] args) {
        Graph graph = new Graph();
        graph.addEdge("A", "B", 4);
        graph.addEdge("A", "C", 1);
        graph.addEdge("C", "D", 2);
        graph.addEdge("B", "D", 5);
        graph.addEdge("D", "E", 1);

        System.out.println("Shortest path from A: " + graph.dijkstra("A"));
    }
}
