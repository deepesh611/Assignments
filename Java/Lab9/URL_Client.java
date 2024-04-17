import java.io.*;
import java.net.*;

public class URL_Client {
    public static void main(String[] args) {
        final String SERVER_URL = "http://localhost:8080";

        try {
            URL url = new URL(SERVER_URL);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");

            // Read response from server
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                StringBuilder response = new StringBuilder();
                String line;
                while ((line = reader.readLine()) != null) {
                    response.append(line);
                }
                System.out.println("Response from server:");
                System.out.println(response.toString());
            }

            connection.disconnect();
        } catch (IOException e) {
            System.err.println("Client exception: " + e.getMessage());
        }
    }
}
