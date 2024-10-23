from zipfile import ZipFile

with ZipFile('../Python/images.zip', 'r') as zip:
    zip.extract('images/6X6.PNG', '../Python/images3')
