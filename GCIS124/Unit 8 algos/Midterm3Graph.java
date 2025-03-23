import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

class Midterm3Graph {
    private Map<String, Vertex> vertices = new HashMap<>();

    // Vertex Class
    static class Vertex {
        private String value;
        private List<Edge> neighbors = new ArrayList<>();

        Vertex(String value) {
            this.value = value;
        }

        public String getValue() {
            return value;
        }

        public List<Edge> getNeighbors() {
            return neighbors;
        }

        public void addNeighbor(Vertex neighbor, int weight) {
            neighbors.add(new Edge(neighbor, weight));
        }
    }

    // Edge Class for Weighted Connections
    static class Edge {
        Vertex vertex;
        int weight;

        Edge(Vertex vertex, int weight) {
            this.vertex = vertex;
            this.weight = weight;
        }
    }

    // Add Vertex
    public void addVertex(String value) {
        vertices.putIfAbsent(value, new Vertex(value));
    }

    // Add Edge (Connecting cities)
    public void addEdge(String city1, String city2, int weight) {
        Vertex v1 = vertices.get(city1);
        Vertex v2 = vertices.get(city2);

        if (v1 != null && v2 != null) {
            v1.addNeighbor(v2, weight);
            v2.addNeighbor(v1, weight); // Bi-directional graph
        }
    }

    // DFS Pathfinding Algorithm with Weights
    public List<String> dfPath(String start, String end) {
        Vertex s = vertices.get(start);
        Vertex e = vertices.get(end);

        Set<Vertex> visited = new HashSet<>();
        visited.add(s);

        List<String> path = visitDFPath(s, e, visited);
        if (path != null) {
            System.out.println("DFS Path Found: " + path);
        } else {
            System.out.println("No path found via DFS.");
        }
        return path;
    }

    private List<String> visitDFPath(Vertex v, Vertex e, Set<Vertex> visited) {
        if (v == e) {
            List<String> path = new LinkedList<>();
            path.add(e.getValue());
            return path;
        } else {
            for (Edge neighbor : v.getNeighbors()) {
                if (!visited.contains(neighbor.vertex)) {
                    visited.add(neighbor.vertex);
                    List<String> path = visitDFPath(neighbor.vertex, e, visited);
                    if (path != null) {
                        path.add(0, v.getValue());
                        return path;
                    }
                }
            }
            return null;
        }
    }

    // BFS Algorithm with Weights (Shortest Path)
    public void bfs(String start, String end) {
        Queue<Path> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        queue.add(new Path(Collections.singletonList(start), 0));

        while (!queue.isEmpty()) {
            Path currentPath = queue.poll();
            String city = currentPath.path.get(currentPath.path.size() - 1);

            if (city.equals(end)) {
                System.out.println("BFS Shortest Path: " + currentPath.path);
                System.out.println("Total Distance: " + currentPath.distance);
                return;
            }

            if (!visited.contains(city)) {
                visited.add(city);

                for (Edge neighbor : vertices.get(city).getNeighbors()) {
                    List<String> newPath = new ArrayList<>(currentPath.path);
                    newPath.add(neighbor.vertex.getValue());
                    queue.add(new Path(newPath, currentPath.distance + neighbor.weight));
                }
            }
        }
        System.out.println("No path found via BFS.");
    }

    // Helper Class for Tracking BFS Paths and Distances
    static class Path {
        List<String> path;
        int distance;

        Path(List<String> path, int distance) {
            this.path = path;
            this.distance = distance;
        }
    }

    public static void main(String[] args) {
        Midterm3Graph graph = new Midterm3Graph();

        // Adding cities as vertices
        String[] cities = {"LA", "LV", "DN", "DL", "KC", "CH", "NYC", "RO"};
        for (String city : cities) {
            graph.addVertex(city);
        }

        // Adding connections (edges) with weights
        graph.addEdge("LA", "LV", 350);
        graph.addEdge("LA", "DN", 850);
        graph.addEdge("LV", "DN", 750);
        graph.addEdge("LV", "DL", 1200);
        graph.addEdge("DN", "KC", 670);
        graph.addEdge("DL", "NYC", 800);
        graph.addEdge("NYC", "RO", 350);

        // Finding paths using BFS and DFS
        graph.dfPath("LA", "RO");  
        graph.bfs("LA", "RO");   
    }
}
