#include<stdio.h>
#include<string.h>

void main(int argc , char *argv[])
{
    FILE *fp;
    char line[100];

    if(argc!=3)
    {
        printf("\n3 arguments required...Invalid number of arguments... Please try again ...\n");
        printf("Try using:: ./compiled_file word_to_match filename");
    }
    else
    {
        fp = fopen(argv[2],"r");
        printf("\n--------------------GREP Command--------------");
        printf("\n");

        while(fscanf(fp , "%[^\n]\n" , line)!=EOF)
        {
            if(strstr(line , argv[1]) !=NULL)
            {
                printf("%s\n" , line);
            }
            else
            {
                continue;
            }
        }
        fclose(fp);
    }
}
