import java.io.*;
import java.net.*;

public class EchoClient {
    public static void main(String[] args) {
        final String SERVER_ADDRESS = "localhost"; // Server's IP address or hostname
        final int PORT = 12345; // Same port as server

        try (Socket socket = new Socket(SERVER_ADDRESS, PORT);
             BufferedReader inputFromUser = new BufferedReader(new InputStreamReader(System.in));
             PrintWriter outputToServer = new PrintWriter(socket.getOutputStream(), true);
             BufferedReader inputFromServer = new BufferedReader(new InputStreamReader(socket.getInputStream()))) {

            System.out.println("Connected to server. Enter message (type 'exit' to quit):");
            String messageToServer;
            while ((messageToServer = inputFromUser.readLine()) != null) {
                if (messageToServer.equalsIgnoreCase("exit")) {
                    break;
                }
                // Send message to server
                outputToServer.println(messageToServer);

                // Receive and print server's response
                System.out.println("Server response: " + inputFromServer.readLine());
            }
        } catch (UnknownHostException e) {
            System.err.println("Unknown host: " + SERVER_ADDRESS);
        } catch (IOException e) {
            System.err.println("Client exception: " + e.getMessage());
        }
    }
}
