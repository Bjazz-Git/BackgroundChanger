#include <windows.h>
#include <conio.h>
#include <stdio.h>

int changeBackground(wchar_t *image);
wchar_t* getBackground();

int main()
{
    wchar_t background = getBackground();
}

// Changes the user's background to the specified image
int changeBackground(wchar_t *image)
{
    // Uses the image directory to find and set the image to the background
    int ret = SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, (void *)image, SPIF_UPDATEINIFILE);

    // Returns a number to represent success or failure of this process
    return ret;
}

// Gets the user's current background
wchar_t* getBackground()
{
    wchar_t buffer[MAX_PATH];
    int ret = SystemParametersInfoA(SPI_GETDESKWALLPAPER, MAX_PATH, buffer, 0);
    printf("%i", ret);
    return buffer;     
}