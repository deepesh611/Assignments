#include <QApplication>
#include "circleellipsewidget.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    CircleEllipseWidget w;
    w.show();
    return a.exec();
}
