#include <graphics.h>
#include <math.h>
#include <iostream>

void drawLineDDA(int x0, int y0, int x1, int y1) {
    // Calculate dx, dy
    int dx = x1 - x0;
    int dy = y1 - y0;

    // Calculate the number of steps required
    int steps = abs(dx) > abs(dy) ? abs(dx) : abs(dy);

    // Calculate the increment in x and y for each step
    float Xinc = dx / (float) steps;
    float Yinc = dy / (float) steps;

    // Initialize starting points
    float x = x0;
    float y = y0;

    // Draw the line
    for (int i = 0; i <= steps; i++) {
        putpixel(round(x), round(y), WHITE); // Draw pixel at (x, y)
        x += Xinc; // Increment x
        y += Yinc; // Increment y
    }
}

int main() {
    int gd = DETECT, gm;

    // Initialize graphics mode
    initgraph(&gd, &gm, NULL);

    // Set the starting and ending points
    int x0, y0, x1, y1;
    std::cout << "Enter the starting point (x0, y0): ";
    std::cin >> x0 >> y0;
    std::cout << "Enter the ending point (x1, y1): ";
    std::cin >> x1 >> y1;

    // Call the DDA function to draw the line
    drawLineDDA(x0, y0, x1, y1);

    // Wait for user input and close the graphics window
    getch();
    closegraph();

    return 0;
}
