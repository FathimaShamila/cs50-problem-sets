#include<math.h>
#include "helpers.h"


// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            float average = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue)/3.0;
            int value = (int)round(average);
            image[i][j].rgbtRed = value;
            image[i][j].rgbtGreen = value;
            image[i][j].rgbtBlue = value;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int sepiaRed,sepiaGreen,sepiaBlue;
    for(int i = 0;i < height; i++)
    {
        for(int j = 0;j < width; j++)
        {
            sepiaRed = (int)round(0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen + 0.189 * image[i][j].rgbtBlue);
            sepiaGreen = (int)round(0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 * image[i][j].rgbtBlue);
            sepiaBlue = (int)round(0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen + 0.131 * image[i][j].rgbtBlue);
            image[i][j].rgbtRed = fmin(255,sepiaRed);
            image[i][j].rgbtGreen = fmin(255,sepiaGreen);
            image[i][j].rgbtBlue = fmin(255,sepiaBlue);
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp;
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width/2; j++)
        {
            temp = image[i][j];
            image[i][j] = image[i][width-1-j];
            image[i][width-1-j] = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE image_copy[height][width];
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            int red = 0,blue = 0,green = 0, count = 0;
            for (int row = i-1; row <= i+1; row++)
            {
                for(int col = j-1; col <= j+1; col++)
                {
                    if(row >= 0 && row < height && col >=0 && col < width)
                    {
                        red += image[row][col].rgbtRed;
                        green += image[row][col].rgbtGreen;
                        blue += image[row][col].rgbtBlue;
                        count++;
                    }
                }
            }
            image_copy[i][j].rgbtRed = round((float)red/count);
            image_copy[i][j].rgbtGreen = round((float)green/count);
            image_copy[i][j].rgbtBlue = round((float)blue/count);
        }
    }
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            image[i][j] = image_copy[i][j];
        }
    }
}
