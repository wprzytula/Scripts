#include <stdio.h>

int main() {
    char c;
    while ((c = getchar()) != -1) {
        if (c != '\n')
            printf("%d\n", c);
    }
    return 0;
}
