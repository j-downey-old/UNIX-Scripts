#!/usr/bin/python

import glob
import sys
import argparse

def main(argv):
    parser = argparse.ArgumentParser()
    
    # Adds all possible arguments
    parser.add_argument( 'path', help = 'Full path to image directory', 
                         metavar='P' )
    parser.add_argument( '-d', '--duration', default = 300.0, type = float, 
                         help = 'Length (in seconds) an image is displayed; default: 300 seconds',
                         dest = 'duration' )
    parser.add_argument( '-t', '--transition', default = 5.0, type = float,
                         help = 'Length (in seconds) of transition; default: 5 seconds', 
                         dest = 'transition')
                        
    args = parser.parse_args()
    path = args.path

    # Checks if '/' is present at the end of the path
    # Appends it if necessary
    if path[-1] != '/':
        path += '/'
    
    filetypes = ['jpg', 'jpeg', 'gif', 'png']
    images = []
    
    # Gets images from path
    for type in filetypes:
        images += glob.glob(path + '*.' + type)

    # Checks if any image files were added
    if len(images) == 0:
        print('Error in retrieving files from path: '+path)
        print('Is it a full path? Are any file types valid?')
        sys.exit(1)
    
    # Checks if XML file can be created
    try:
        file = open(path + 'slideshow.xml', 'w')
    except:
        print('Error in creating new XML file in path: ' + path)
        sys.exit(1)

    file.write('<background>\n')
    file.write('  <starttime>\n')
    file.write('    <year>2016</year>\n')
    file.write('    <month>01</month>\n')
    file.write('    <day>01</day>\n')
    file.write('    <hour>00</hour>\n')
    file.write('    <minute>00</minute>\n')
    file.write('    <second>00</second>\n')
    file.write('  </starttime>\n')
    
    for idx, img in enumerate(images, start = 0):
        file.write('  <static>\n')
        file.write('    <duration>' + str(args.duration) + '</duration>\n')
        file.write('    <file>' + img + '</file>\n')
        file.write('  </static>\n')
        
        # Assign appropriate prev and next filenames
        prev_img = img
           
        if idx<len(images) - 1:
           next_img = images[idx + 1]
        else:
           next_img = images[0]
            
        file.write('  <transition>\n')
        file.write('    <duration>' + str(args.transition) + '</duration>\n')
        file.write('    <from>' + prev_img + '</from>\n')
        file.write('    <to>' + next_img + '</to>\n')
        file.write('  </transition>\n')
         
    file.write('</background>')
    file.close()

if __name__ == "__main__":
    main(sys.argv[1:])

