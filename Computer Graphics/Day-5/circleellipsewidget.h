#ifndef CIRCLEELLIPSEWIDGET_H
#define CIRCLEELLIPSEWIDGET_H

#include <QWidget>

class CircleEllipseWidget : public QWidget
{
    Q_OBJECT
public:
    explicit CircleEllipseWidget(QWidget *parent = nullptr);

protected:
    void paintEvent(QPaintEvent *event) override;

private:
    void drawMidpointCircle(QPainter &painter, int cx, int cy, int r);
    void drawMidpointEllipse(QPainter &painter, int cx, int cy, int a, int b);
};

#endif // CIRCLEELLIPSEWIDGET_H
