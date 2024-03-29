#ifndef _SLIDE_LINE_H_
#define _SLIDE_LINE_H_

#include <stdio.h>
#include <stdlib.h>

#define SLIDE_LEFT  0
#define SLIDE_RIGHT 1

int slide_line(int *line, size_t size, int direction);
void merge_left(int *line, size_t size);
void merge_right(int *line, size_t size);


#endif
