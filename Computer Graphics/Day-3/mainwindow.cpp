#include "mainwindow.h"
#include <QPainter>
#include <QPen>
#include <QDebug> // Include for qDebug() output

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    setFixedSize(500, 500);  // Set the window size
}

MainWindow::~MainWindow()
{
}

void MainWindow::paintEvent(QPaintEvent *event)
{
    QPainter painter(this);
    painter.setPen(QPen(Qt::gray));

    int gridSize = 20;
    int width = this->width();
    int height = this->height();

    // Draw the grid
    for (int x = 0; x < width; x += gridSize) {
        painter.drawLine(x, 0, x, height);
    }
    for (int y = 0; y < height; y += gridSize) {
        painter.drawLine(0, y, width, y);
    }

    painter.setPen(QPen(Qt::red, 2));
    int x0 = 180, y0 = 280, x1 = 360, y1 = 440;
    drawBresenhamLine(x0, y0, x1, y1, painter);
}

void MainWindow::drawBresenhamLine(int x0, int y0, int x1, int y1, QPainter &painter)
{
    int dx = abs(x1 - x0);
    int dy = abs(y1 - y0);
    int sx = (x0 < x1) ? 1 : -1;
    int sy = (y0 < y1) ? 1 : -1;
    int err = dx - dy;

    while (true) {
        // Draw the point as a small circle (ellipse) for visibility
        painter.drawEllipse(x0 - 1, y0 - 1, 3, 3); // Draw small circles at each point

        // Optionally print the coordinates to the console
        qDebug() << "(" << x0 << "," << y0 << ")";

        if (x0 == x1 && y0 == y1)
            break;

        int e2 = err;
        if (e2 > -dy) {
            err -= dy;
            x0 += sx;
        }
        if (e2 < dx) {
            err += dx;
            y0 += sy;
        }
    }
}
