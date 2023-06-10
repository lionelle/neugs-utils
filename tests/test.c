#include <stdio.h>
#include <stdlib.h>


void unlimited_loop() {
    while (1); 
}

void memory_leak() {
    int *p = malloc(10 * sizeof(int));
    p[10] = 1;
    p[11] = 1;
}

int main(int argc, char **argv ) {
    int test = 0;
    if(argc > 1) {
        test = atoi(argv[1]);
    }
    if(test == 1) unlimited_loop();
    if(test == 2) memory_leak();

    printf("I am here\n");
    return 0;
}