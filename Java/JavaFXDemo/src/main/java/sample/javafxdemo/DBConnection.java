package sample.javafxdemo;

import java.sql.Connection;
import java.sql.DriverManager;

public class DBConnection {
    public Connection databaseLink;

    public Connection getConnection() {
        String databaseName = "javadb";
        String databaseUser = "root";
        String databasePassword = "";
        String url = "jdbc:mysql://localhost/" + databaseName;

        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            databaseLink = DriverManager.getConnection(url, databaseUser, databasePassword);
        }

        catch(Exception e){
            e.printStackTrace();
        }
        return databaseLink;
    }
}
