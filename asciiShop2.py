
import sys
#sys.path.append("/Library/Python/2.7/site-packages")
import os
import uuid,urllib3
import time
from PIL import Image

url = 'http://thecatapi.com/api/images/get'

def getCat(directory=None, filename=None, format='png'):
    basename = '%s.%s' % (filename if filename else str(uuid.uuid4()), format)
    savefile =  os.path.sep.join([directory.rstrip(os.path.sep), basename]) if directory else basename
    downloadlink = url + '?type=%s' % format
    http = urllib3.PoolManager()
    r = http.request('GET', downloadlink)
    fp = open(savefile, 'wb')
    fp.write(r.data)
    fp.close()
    return savefile

class RandomCat(object):

    def __init__(self):

        self.name = ''          # name of image
        self.path = '.'         # path on local file system
        self.format = 'png'
        self.width = 0          # width of image
        self.height = 0         # height of image
        self.img = None         # Pillow var to hold image


    """
    @Description:
    - Uses random cat to go get an amazing image from the internet
    - Names the image
    - Saves the image to some location
    @Returns:
    """
    def getImage(self):
        self.name = self.getTimeStamp()
        getCat(directory=self.path, filename=self.name, format=self.format)
        self.img = Image.open(self.name+'.'+self.format)

        self.width, self.heigth = self.img.size

    """
    Saves the image to the local file system given:
    - Names
    - Path
    """
    def saveImage(self):
        pass

    """
    """
    def nameImage(self):
        pass

    """
    Gets time stamp from local system
    """
    def getTimeStamp(self):
        seconds,milli = str(time.time()).split('.')
        return seconds


"""
The ascii character set we use to replace pixels.
The grayscale pixel values are 0-255.
0 - 25 = '#' (darkest character)
250-255 = '.' (lightest character)
"""


class AsciiImage(RandomCat):

    def __init__(self,new_width="not_set"):
        super(AsciiImage, self).__init__()

        self.newWidth = new_width
        self.newHeight = 0

        self.asciiChars = [ '#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']
        self.invertedAsciiChars = [ '#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']
        self.invertedAsciiChars.reverse()
        self.imageAsAscii = []
        self.matrix = None


    """
    @Name: convertToAscii
    @Description: converts an image to ascii characters so that individual pixels can be manipulated
    @Params: None
    @Returns: None
    """
    def convertToAscii(self):

        if self.newWidth == "not_set":
            self.newWidth = self.width

        self.newHeight = int((self.heigth * self.newWidth) / self.width)

        if self.newWidth == None:
            self.newWidth = self.width
            self.newHeight = self.height

        self.newImage = self.img.resize((self.newWidth, self.newHeight))
        self.newImage = self.newImage.convert("L") # convert to grayscale
        all_pixels = list(self.newImage.getdata())
        self.matrix = listToMatrix(all_pixels,self.newWidth)


        for pixel_value in all_pixels:
            index = pixel_value // 25 # 0 - 10
            self.imageAsAscii.append(self.asciiChars[index])

    """
    Print the image to the screen
    """
    def printImage(self):
        self.imageAsAscii = ''.join(ch for ch in self.imageAsAscii)
        for c in range(0, len(self.imageAsAscii), self.newWidth):
            print (self.imageAsAscii[c:c+self.newWidth])

    """
    @Name: invert
    @Description: This method will take all the lightest pixels and make them the darkest, next lightest => next darkest, etc..
    @Params: None
    @Returns: (string) - Inverted ascii image.

    """

    def invert(self):
        self.imageAsAscii = []
        # All pixels in one long list
        all_pixels = list(self.newImage.getdata())



        for pixel_value in all_pixels:
            index = pixel_value // 25 # 0 - 10, array index to char list
            self.imageAsAscii.append(self.invertedAsciiChars[index])


    """
    @Name: flip
    @Description: This method will flip an image horizontally, or vertically.
    - Vertically means all pixels in row 0 => row N, row 1 => row N-1, ... row N/2 => row N/2+1.
    - Horizontally means all pixels in col 0 => col N, col 1 => col N-1, ... col N/2 => col N/2+1
    @Params: direction (string) - [horizontal,vertical] The direction to flip the cat.
    @Returns: (string) - Flipped ascii image.
    """
    def flip(self, direction):

        flipdImg= []
        height = self.height
        width = self.width
        #Now its a 2D array
        self.matrix = listToMatrix(all_pixels,self.newWidth)
        print(self.matrix)

        if(direction == "vertical"):
            for rows in range(width):
                for cols in range(height//2):
                    flipdPixel = self.martix[rows][cols]
                    flipdImg[width-1-rows][cols] = flipdPixel #calculate where to insert pixel in [row]
                                            #always flipped vertically in same [cols]
                                            #vice versa true for flipping horizontally
        elif(direction == "horizontal"):
            for cols in range(height):
                for row in range(width//2):
                    flipdPixel = self.martix[rows][cols]
                    flipdImg[rows][height-1-cols] = flipdPixel

"""
Convert to 2D list of lists to help with manipulating the ascii image.
Example:

    L = [0,1,2,3,4,5,6,7,8]

    L = to_matrix(L,3)

    L becomes:

    [[0,1,2],
    [3,4,5],
    [6,7,8]]
"""
def listToMatrix(l, n):
    return [l[i:i+n] for i in xrange(0, len(l), n)]

if __name__=='__main__':
    awesomeCat = AsciiImage(150)
    awesomeCat.getImage()

    awesomeCat.convertToAscii()
    #awesomeCat.printImage()
    awesomeCat.flip("vertical")
    #awesomeCat.invert()


    awesomeCat.printImage()
