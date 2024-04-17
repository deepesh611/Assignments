package sample.javafxdemo;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.sql.*;


public class HelloController {
    @FXML
    private Button cancelButton;
    @FXML
    private Button loginButton;
    @FXML
    private Label msgBoxG;
    @FXML
    private Label msgBoxR;
    @FXML
    private TextField usernameField;
    @FXML
    private PasswordField passwordField;

    public void loginButtonOnAction(ActionEvent e) {
        if (usernameField.getText().isBlank() || passwordField.getText().isBlank()){
            msgBoxR.setText("Please fill the Credentials...");
            msgBoxG.setText("");
        }

        else{
            validateLogin();
        }
    }

    public void cancelButtonOnAction(ActionEvent e) {
        Stage stage = (Stage) cancelButton.getScene().getWindow();
        stage.close();
    }

    public void validateLogin(){
        DBConnection connectNow = new DBConnection();
        Connection connectDB = connectNow.getConnection();

        String verifyLogin = "select * from users where username = '" + usernameField.getText() + "' and password = '" + passwordField.getText() + "'";

        try {
            Statement statement = connectDB.createStatement();
            ResultSet queryResult = statement.executeQuery(verifyLogin);

            if (queryResult.next()){
                msgBoxG.setText("Login Successful");
                msgBoxR.setText("");
            }

            else{
                msgBoxR.setText("Invalid Login. Please try again.");
                msgBoxG.setText("");
            }
        }

        catch (Exception e){
            e.printStackTrace();
        }
    }
}