module sample.javafxdemo {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;


    opens sample.javafxdemo to javafx.fxml;
    exports sample.javafxdemo;
}