#include <windows.h>
#include <conio.h>
#include <stdio.h>

int changeImage(char *image)
{
    // Needs to be changed from static string
    const wchar_t *file = L"<image>";
    int ret = SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, (void *)file, SPIF_UPDATEINIFILE);
    return ret;
}