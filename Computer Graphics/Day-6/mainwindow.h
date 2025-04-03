#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QImage>
#include <QColor>
#include <QPoint>
#include <QPolygon>

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

protected:
    void paintEvent(QPaintEvent *event) override;

private:
    QImage canvas;  // Our drawing canvas
    void initCanvas();
    void drawShapes();

    // Fill algorithms:
    void floodFill(int x, int y, const QColor &targetColor, const QColor &replacementColor);
    void boundaryFill(int x, int y, const QColor &fillColor, const QColor &boundaryColor);
    void scanLineFill(const QPolygon &polygon, const QColor &fillColor);
};

#endif // MAINWINDOW_H
