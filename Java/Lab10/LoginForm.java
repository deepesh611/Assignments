import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.*;

public class LoginForm extends JDialog {
    private JTextField tfUsername;
    private JPasswordField passwordField1;
    private JButton btnOK;
    private JButton btnCancel;
    private JPanel LoginPanel;

    public LoginForm(JFrame parent) {
        super(parent);

        btnOK.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String username = tfUsername.getText();
                String password = String.valueOf(passwordField1.getPassword());

                user = getAuthenticatedUser(username, password);

                if (user != null) {
                    JOptionPane.showMessageDialog(LoginForm.this,
                            "Login successful. \nWelcome " + user.name + "!",
                            "Login", JOptionPane.INFORMATION_MESSAGE
                    );
                    dispose();

                    SwingUtilities.invokeLater(() -> {
                        StudentDB studentDB = new StudentDB();
                        studentDB.setVisible(true);
                    });
                }


                else {
                    JOptionPane.showMessageDialog(LoginForm.this,
                            "Invalid email or password",
                            "Login", JOptionPane.ERROR_MESSAGE
                    );
                }
            }
        });

        btnCancel.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose();
            }
        });

        setTitle("Login");
        setContentPane(LoginPanel);
        setMinimumSize(new Dimension(550, 500));
        setModal(true);
        setLocationRelativeTo(parent);
        setDefaultCloseOperation(DISPOSE_ON_CLOSE);
        setVisible(true);
    }

    public static User user;

    private User getAuthenticatedUser(String username, String password) {
        User user = null;

        final String DB_URL = "jdbc:mysql://localhost/JavaDB?";
        final String USER = "root";
        final String PASSWORD = "";

        try{
            Connection conn = DriverManager.getConnection(DB_URL, USER, PASSWORD);
            System.out.println("Connected to the database");

            Statement stmt = conn.createStatement();
            String sql = "SELECT * FROM users WHERE username=? AND password=?";
            PreparedStatement ps = conn.prepareStatement(sql);
            ps.setString(1, username);
            ps.setString(2, password);

            ResultSet rs = ps.executeQuery();
            if (rs.next()) {
                user = new User();
                user.name = rs.getString("username");
                user.password = rs.getString("password");
            }

            stmt.close();
            conn.close();

        }

        catch (Exception e){
            e.printStackTrace();
        }

        return user;
    }



    public static void main(String[] args) {
        LoginForm dialog = new LoginForm(null);
        User user = LoginForm.user;

        if (user != null) {
            System.out.println("Welcome " + user.name);
            StudentDB studentDB = new StudentDB();
        }

        else {
            System.out.println("Login failed");
        }
    }
}
