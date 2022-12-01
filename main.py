from PIL import Image, ImageFont, ImageDraw

names = []

with open('names.txt') as f:
    content = f.readlines()
    for item in content:
        names.append(item[:-1].title())       

for title_text in names:
    title_font = ImageFont.truetype(r'font_type.ttf', 180)
    title_color = (0,0,0)

    template = Image.open(r'template.png')
    WIDTH, HEIGHT = template.size
    draw = ImageDraw.Draw(template)
    name_width, name_height = draw.textsize(title_text, font=title_font)
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30), title_text, fill=title_color , font=title_font)

    template.save("./out/" + title_text +".png")
    print('Saving Certificate of:', title_text)
