#include <stdio.h>
#include <stdlib.h>
#include<stdint.h>
const int SIZE = 512;
typedef uint8_t BYTE;
int main(int argc, char *argv[])
{
    if(argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }
    FILE *card_name = fopen(argv[1],"r");
    if (card_name == NULL)
    {
        printf("Could not open file.\n");
        return 2;
    }
    BYTE buffer[SIZE];
    FILE *img = NULL;
    char filename[8];
    int file_count = 0;
    while(fread(buffer,sizeof(BYTE),SIZE,card_name) == 512)
    {
        if((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && ((buffer[3] & 0xf0) == 0xe0))
        {
            if(img != NULL)
            {
                fclose(img);
            }
            sprintf(filename,"%03i.jpg",file_count++);
            img = fopen(filename,"wb");
            if (img == NULL)
            {
                printf("Cant create image.\n");
                fclose(card_name);
                return 3;
            }
        }
        if(img != NULL)
        {
            fwrite(buffer,sizeof(BYTE),SIZE,img);
        }
    }
    if(img != NULL)
    {
        fclose(img);
    }
    fclose(card_name);
    return 0;
}
