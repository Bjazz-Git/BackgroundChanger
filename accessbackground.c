#include <windows.h>
#include <conio.h>
#include <stdio.h>

// int changeBackground(wchar_t *image);
// char *getBackground();
// void freeMemory(void* pointer);

// int main()
// {
//     char *background = NULL;
//     background = getBackground();
//     printf("Directory is %s", background);
//     freeMemory(background);
// }

// Changes the user's background to the specified image
int changeBackground(wchar_t *image)
{
    // Uses the image directory to find and set the image to the background
    int ret = SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, (void *)image, SPIF_UPDATEINIFILE);

    // Returns a number to represent success or failure of this process
    return ret;
}

// Gets the user's current background
char *getBackground()
{
    // Pointer to contain background
    char *background = malloc(MAX_PATH * sizeof(char));

    // Gets the desktop's background, returns a status code
    int ret = SystemParametersInfoA(SPI_GETDESKWALLPAPER, MAX_PATH, background, 0);

    return background;     
}


// Frees any memory allocated with malloc
void freeMemory(void* pointer)
{
    free(pointer);
}