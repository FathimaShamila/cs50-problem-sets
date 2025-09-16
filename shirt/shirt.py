from PIL import Image
from PIL import ImageOps
import sys
import os
def main():
    file_ext = ('.jpg','.jpeg','.png')
    _,inp_ext = os.path.splitext(sys.argv[1])
    _,out_ext = os.path.splitext(sys.argv[2])
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    try:
        if len(sys.argv) == 3:
            if inp_ext != out_ext:
                sys.exit("Input and output have different extensions")
            elif inp_ext in file_ext and out_ext in file_ext:
                shirt  = Image.open("shirt.png")
                input_image = Image.open(input_file)
                input_image = ImageOps.fit(input_image,shirt.size)
                input_image.paste(shirt,shirt)
                input_image.save(output_file)
                #Image.open("after_shirt.png").show()
            else:
                sys.exit("File type error")
        else:
            sys.exit("Expected 2 arguments")
    except FileNotFoundError:
        print("File not found")
if __name__ == "__main__":
    main()
