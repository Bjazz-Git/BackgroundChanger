#include <windows.h>
#include <conio.h>
#include <stdio.h>

// Changes the user's background to the specified image
int changeImage(wchar_t *image)
{
    // Uses the image directory to find and set the image to the background
    int ret = SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, (void *)image, SPIF_UPDATEINIFILE);

    // Returns a number to represent success or failure of this process
    return ret;
}