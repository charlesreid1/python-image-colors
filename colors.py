from PIL import Image
import sys
import os.path

def analyze( imgFile ):
    # open the image
#
################################
#
# if you ad open( imgPath + imgFile ) 
# then it will work being run from anywhere.
# otherwise it has to be run from the dir 
# with the images.
#
################################
#
    img = Image.open(imgFile)

    # grab width and height
    width, height = img.size

    # make a list of all pixels in the image
    pixels = img.load()
    data = []
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y]
            data.append(cpixel)

    r = 0
    g = 0
    b = 0
    counter = 0

    # loop through all pixels
    # if alpha value is greater than 200/255, add it to the average
    # (note: could also use criteria like, if not a black pixel or not a white pixel...)
    for x in range(len(data)):
        try:
            if data[x][3] > 200:
                r+=data[x][0]
                g+=data[x][1]
                b+=data[x][2]
        except:
            r+=data[x][0]
            g+=data[x][1]
            b+=data[x][2]

        counter+=1

    # compute average RGB values
    rAvg = r/counter
    gAvg = g/counter
    bAvg = b/counter

    return (rAvg, gAvg, bAvg)



def startPage() :
    f.write('<html>\n');
    f.write('<body>\n');

def startTable() :
    f.write('<table width="400px" border="1"> \n');

def writePicture( image, avg_r, avg_g, avg_b ) :
    f.write('<tr>\n');
    f.write('<td width="200px"> \n');
    f.write('<img width="200px" height="200px" src="img/');
    f.write(image);
    f.write('" />\n');
    f.write('</td>\n');
    f.write('<td width="200px" style="background-color: rgb(');
    f.write(str(avg_r) + ',' + str(avg_g) + ',' + str(avg_b));
    f.write(');">');
    f.write('</td>\n');
    f.write('</tr>\n');

def endTable():
    f.write('</table>');

def endPage() :
    f.write('</body>\n');
    f.write('</html>\n');


f = open('CMRAverageColors.html','w');

startPage();
startTable();


for image in os.listdir( mypath ):
    if( image.find('jpg') > 0 ):
        r, g, b = analyze(image)
        writePicture(image, r, g, b);
        print "Finished with image " + image

endTable();
endPage();

f.closed

