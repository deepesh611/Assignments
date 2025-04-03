#include "mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent) {
    this->setFixedSize(600, 400);

    // Create a button
    button = new QPushButton("Click Me", this);
    button->setGeometry(50, 50, 100, 30);

    // Create animation
    animation = new QPropertyAnimation(button, "geometry");
    animation->setDuration(1000);  // 1 second
    animation->setStartValue(QRect(50, 50, 100, 30));
    animation->setEndValue(QRect(300, 50, 100, 30));
    animation->setEasingCurve(QEasingCurve::OutBounce);

    animation->setDuration(1000);  // 1 second
    animation->setEndValue(QRect(300, 50, 100, 30));
    animation->setEndValue(QRect(300, 100, 100, 30));
    animation->setEasingCurve(QEasingCurve::OutBounce);

    // Start animation when button is clicked
    connect(button, &QPushButton::clicked, [this]() {
        animation->start();
    });

}

MainWindow::~MainWindow() {}
