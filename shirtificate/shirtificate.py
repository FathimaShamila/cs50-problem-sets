from fpdf import FPDF
from PIL import Image,ImageDraw,ImageFont
def main():
    name = input("Enter name:")
    name_text = name + " took CS50"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica",style = "B", size = 40)
    pdf.cell(text = 'CS50 Shirtificate',align = 'C',center = True)
    pdf.image("shirtificate.png",x = 20,y = 60,keep_aspect_ratio = True)
    pdf.set_xy(60,120)
    pdf.cell(0,10,name_text)
    pdf.output("shirtificate.pdf")



if __name__ == "__main__":
    main()
