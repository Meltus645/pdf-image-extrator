from app import ImageExtractor

filepath =input("[+] Enter pdf file path: ")
extractor =ImageExtractor(filepath)
extractor.extract()