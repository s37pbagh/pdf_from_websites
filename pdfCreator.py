import os
import re
from fpdf import FPDF
from PIL import Image
import tempfile

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
folder_path = '/Users/parham/Desktop/untitledfolder/taqche'
from PyPDF2 import PdfMerger

def natural_keys(text):
    return [int(c) if c.isdigit() else c.lower() for c in re.split('(\d+)', text)]

def create_pdf_from_images(folder_path, crop_start, crop_end, batch_size=10):
    files = os.listdir(folder_path)
    files.sort(key=natural_keys)
    
    pdf_paths = []  # To keep track of the generated PDF files
    for i in range(0, len(files), batch_size):
        batch_files = files[i:i+batch_size]
        pdf = FPDF()
        pdf_filename = f"temp_{i//batch_size}.pdf"
        pdf_path = os.path.join(folder_path, pdf_filename)
        pdf_paths.append(pdf_path)
        
        for file in batch_files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                file_path = os.path.join(folder_path, file)
                with Image.open(file_path) as image:
                    if image.mode == 'RGBA':
                        image = image.convert('RGB')
                    
                    cropped_image = image.crop(crop_start + crop_end)
                    with tempfile.NamedTemporaryFile(suffix='.jpg') as tmpfile:
                        cropped_image.save(tmpfile, format='JPEG', quality=85)
                        pdf.add_page()
                        pdf.image(tmpfile.name, 10, 10, pdf.w - 20)  # Adjust as needed
                        
        pdf.output(pdf_path)
    
    # Merge the PDFs
    merger = PdfMerger()
    for pdf_path in pdf_paths:
        merger.append(pdf_path)
    
    merger.write(os.path.join(folder_path, "output.pdf"))
    merger.close()
    
    # Optionally, remove the temporary PDFs
    for pdf_path in pdf_paths:
        os.remove(pdf_path)
def name_fix():
    # Set the folder path
    folder_path = '/Users/parham/Desktop/untitledfolder/taqche'
    # Set the constant number to subtract
    constant_number = 89

    # Regular expression to find the number before the extension
    processed_mark = 'processed_'

    # Regular expression to find the number before the extension and ignore files already marked as processed
    pattern = re.compile(r'(\d+)(?=\.\w+$)')
    processed_pattern = re.compile(rf'^{processed_mark}')

    # List all files in the directory
    for filename in os.listdir(folder_path):
        # Skip files that have already been processed
        if processed_pattern.search(filename):
            print(f'Skipped "{filename}" as it has already been processed.')
            continue

        # Check if the filename matches the pattern for numbers
        match = pattern.search(filename)
        if match:
            start, end = match.span()
            # Extract the base name and extension
            base_name = filename[:start]
            number = int(match.group())
            extension = filename[end:]
            # Subtract the constant from the number
            new_number = max(0, number - constant_number)  # Ensure the new number is not negative
            new_filename = f"{processed_mark}{base_name}{new_number}{extension}"
            # Construct full file paths
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f'Renamed "{filename}" to "{new_filename}"')

ix, iy = 0, 0
jx, jy = 0, 0
def onclick_start(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    print(f"Coordinates: x={ix} y={iy}")
def onclick_end(event):
    global jx, jy,ix,jx,folder_path
    jx, jy = event.xdata, event.ydata
    print(f"Coordinates: x={ix} y={iy}")
    create_pdf_from_images(folder_path, (ix, iy), (jx, jy),50)

    
files = os.listdir(folder_path)
fig = plt.figure()
img = mpimg.imread(os.path.join(folder_path, files[0]))
imgplot = plt.imshow(img)

cid = fig.canvas.mpl_connect('button_press_event', onclick_start)


plt.show()
input("press enter to continue!")


files = os.listdir(folder_path)
fig = plt.figure()
img = mpimg.imread(os.path.join(folder_path, files[0]))
imgplot = plt.imshow(img)


cid = fig.canvas.mpl_connect('button_press_event', onclick_end)

plt.show()