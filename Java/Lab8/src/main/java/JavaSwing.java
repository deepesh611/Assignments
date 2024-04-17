import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class JavaSwing {

    public JFrame jframe;
    public JavaSwing() {
        jframe = new JFrame("Basic Swing Frame");

        JButton Print = new JButton("Analyse");
        Print.setBounds(130,80,100,30);
        Print.setBackground(Color.orange);

        JLabel char_count = new JLabel();
        char_count.setBounds(90,200,200,30);

        JLabel word_count = new JLabel();
        word_count.setBounds(90,190,200,30);

        JLabel output = new JLabel("The Output will be shown here...");
        output.setBounds(90, 150, 200, 30);

        JTextField InputBox = new JTextField();
        InputBox.setBounds(80, 40, 200, 30);

        jframe.add(InputBox);
        jframe.add(output);
        jframe.add(Print);
        jframe.add(char_count);
        jframe.add(word_count);

        Print.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String input = InputBox.getText();
                int charCount = input.length();
                int wordCount = input.split("\\s+").length;
                char_count.setText("Character count: " + charCount);
                word_count.setText("Word count: " + wordCount);
                output.setText(InputBox.getText());
                InputBox.setText("");
            }
        });

        jframe.setLayout(null);
        jframe.setSize(400, 400);
        jframe.setVisible(true);
        jframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    }

    public static void main(String[] args) {
        JavaSwing ns = new JavaSwing();
    }
}