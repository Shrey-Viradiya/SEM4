#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char * argv[])

{

printf("execDemo: My pid is %d \n", getpid());

char *args[] = {"./prac9","hello","world",NULL};
execvp(args[0], args);

// code below exec command never executes

printf("good bye");
return 0;

}
