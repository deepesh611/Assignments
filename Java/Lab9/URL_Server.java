import java.io.*;
import java.net.*;
import java.util.*;

public class URL_Server {
    public static void main(String[] args) {
        final int PORT = 8080;

        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("Server is running and listening on port " + PORT);

            while (true) {
                // Wait for client connection
                Socket clientSocket = serverSocket.accept();
                System.out.println("Client connected: " + clientSocket);

                // Handle client's HTTP request
                try (
                    BufferedReader reader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                    PrintWriter writer = new PrintWriter(clientSocket.getOutputStream(), true);
                ) {
                    String httpRequest = reader.readLine();
                    System.out.println("Received HTTP request from client:");
                    System.out.println(httpRequest);

                    // Send HTTP response back to client
                    String httpResponse = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n";
                    httpResponse += "<h1>Hello from Server!</h1>\r\n";
                    writer.println(httpResponse);
                } catch (IOException e) {
                    System.err.println("Error handling client request: " + e.getMessage());
                } finally {
                    // Close client socket
                    clientSocket.close();
                    System.out.println("Client disconnected");
                }
            }
        } catch (IOException e) {
            System.err.println("Server exception: " + e.getMessage());
        }
    }
}
