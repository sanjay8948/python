import PyPDF2
my_file=open('sanju.pdf','rb')
pdf_reader=PyPDF2.PdfFileReader(my_file)

#print(pdf_reader.numPages)
#page_one=pdf_reader.getPage(0)
#print(page_one.extractText())

#read pdf file

#for i in range(pdf_reader.numPages):
#    page=pdf_reader.getPage(i)
#    print(page.extractText())
#    print('\n')


#write to pdf

print(pdf_reader.numPages)
page_one=pdf_reader.getPage(0)

output_file=open('new_pdf.pdf','wb')
pdf_writer=PyPDF2.PdfFileWriter()
pdf_writer.addPage(page_one)
pdf_writer.write(output_file)

my_file.close()
output_file.close()
    
