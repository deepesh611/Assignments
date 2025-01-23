#include "mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent) {
    resize(500, 500); // Set the window size
}

MainWindow::~MainWindow() {}

void MainWindow::paintEvent(QPaintEvent *event) {
    QPainter painter(this);
    drawLineDDA(painter, 50, 50, 450, 450); // Example line coordinates
}

void MainWindow::drawLineDDA(QPainter &painter, int x0, int y0, int x1, int y1) {
    int dx = x1 - x0;
    int dy = y1 - y0;

    int steps = std::max(abs(dx), abs(dy));
    float xInc = dx / (float) steps;
    float yInc = dy / (float) steps;

    float x = x0;
    float y = y0;

    for (int i = 0; i <= steps; i++) {
        painter.drawPoint(round(x), round(y)); // Draw the pixel
        x += xInc;
        y += yInc;
    }
}
