import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;
import java.util.Stack;

class Midterm3Graph {
    private Map<String, List<Node>> map = new HashMap<>();

    static class Node {
        String city;
        int distance;

        Node(String city, int distance) {
            this.city = city;
            this.distance = distance;
        }
    }

    // Add an edge between two nodes
    public void addEdge(String city1, String city2, int distance) {
        map.putIfAbsent(city1, new ArrayList<>());
        map.putIfAbsent(city2, new ArrayList<>());
        map.get(city1).add(new Node(city2, distance));
        map.get(city2).add(new Node(city1, distance)); // Bi-directional graph
    }

    // BFS Algorithm
    public void bfs(String start, String target) {
        Queue<List<String>> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        queue.add(Collections.singletonList(start));

        while (!queue.isEmpty()) {
            List<String> path = queue.poll();
            String city = path.get(path.size() - 1);

            if (city.equals(target)) {
                System.out.println("BFS Shortest Path: " + path);
                return;
            }

            if (!visited.contains(city)) {
                visited.add(city);

                for (Node neighbor : map.getOrDefault(city, new ArrayList<>())) {
                    List<String> newPath = new ArrayList<>(path);
                    newPath.add(neighbor.city);
                    queue.add(newPath);
                }
            }
        }
        System.out.println("No path found via BFS.");
    }

    // DFS Algorithm
    public void dfs(String start, String target) {
        Stack<List<String>> stack = new Stack<>();
        Set<String> visited = new HashSet<>();
        stack.push(Collections.singletonList(start));

        while (!stack.isEmpty()) {
            List<String> path = stack.pop();
            String city = path.get(path.size() - 1);

            if (city.equals(target)) {
                System.out.println("DFS Found Path: " + path);
                return;
            }

            if (!visited.contains(city)) {
                visited.add(city);

                for (Node neighbor : map.getOrDefault(city, new ArrayList<>())) {
                    List<String> newPath = new ArrayList<>(path);
                    newPath.add(neighbor.city);
                    stack.push(newPath);
                }
            }
        }
        System.out.println("No path found via DFS.");
    }

    public static void main(String[] args) {
        Midterm3Graph graphoo = new Midterm3Graph();

        // Adding the nodes and distances
        graphoo.addEdge("LA", "LV", 350);
        graphoo.addEdge("LA", "DN", 850);
        graphoo.addEdge("LV", "DN", 750);
        graphoo.addEdge("LV", "DL", 1200);
        graphoo.addEdge("DN", "KC", 670);
        graphoo.addEdge("DL", "KC", 500);
        graphoo.addEdge("KC", "CH", 1000);
        graphoo.addEdge("DL", "NYC", 800);
        graphoo.addEdge("NYC", "RO", 350);

        // Finding the shortest path
        graphoo.bfs("LA", "RO");  // BFS Example
        graphoo.dfs("LA", "RO");  // DFS Example
    }
}
