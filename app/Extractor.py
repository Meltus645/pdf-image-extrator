import fitz, os
from PIL import Image

class ImageExtractor:
    filer_eady =False

    def __init__(self, pdf_filepath:str, image_dir =None):
        try:
            print("[+] Opening file")
            self.pdf =fitz.open(pdf_filepath)
            self.pdf_pages_count =len(self.pdf)
            self.image_dir =image_dir if image_dir else '_'.join(pdf_filepath.split('/')[-1].split('.')[:-1])
            self.filer_eady =True
        except Exception as e: print(f"[-] {e}") 

    def extract(self):
        if self.filer_eady:
            if not os.path.exists(self.image_dir): os.mkdir(self.image_dir)
            else: 
                if len(os.listdir(self.image_dir)) >0: raise OSError("A non empty directory with simillar name already exists")

            self.images =[]
            print("[+] Extracting images")
            for page in range(self.pdf_pages_count):
                content =self.pdf[page]
                self.images.extend(content.get_images())
            
            if len(self.images) >0:  
                self.save()
                print(f"[+] {len(self.images)} image(s) extracted to {self.image_dir}/")
            else: 
                print("No image found")
                os.removedirs(self.image_dir)
        else: print("[-] No file to open")
    
    def save(self):
        for i, image in enumerate(self.images):
            x_ref =image[0]
            img =self.pdf.extract_image(x_ref)
            img_bytes =img.get('image')
            img_ext =img.get('ext')
            filename =f"{self.image_dir}/IMG_{i+1 if i+1 >9 else '0'+str(i+1)}.{img_ext}"
            with open(filename, 'wb') as im: im.write(img_bytes)