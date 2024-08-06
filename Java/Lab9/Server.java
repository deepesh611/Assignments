// Server

import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) {
        final int PORT = 12345; // Choose any available port

        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("Server started. Waiting for clients...");

            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Client connected: " + clientSocket);

                // Create input and output streams for the client socket
                BufferedReader inputFromClient = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                PrintWriter outputToClient = new PrintWriter(clientSocket.getOutputStream(), true);

                // Read from client and echo back
                String messageFromClient;
                while ((messageFromClient = inputFromClient.readLine()) != null) {
                    System.out.println("Received from client: " + messageFromClient);
                    outputToClient.println("Echo: " + messageFromClient);
                }

                // Close client socket
                clientSocket.close();
            }
        } catch (IOException e) {
            System.err.println("Server exception: " + e.getMessage());
        }
    }
}
