import PyPDF2

def dividir_pdf(pdf_path):
    # Abrir el PDF 
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        # Itera sobre cada página del PDF
        for page_number in range(len(reader.pages)):
            # Crear un nuevo PDF para cada página
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[page_number])

            # Guardar el PDF de una página unicamente
            output_pdf_path = f"pagina_{page_number + 1}.pdf"
            with open(output_pdf_path, "wb") as output_file:
                writer.write(output_file)
            print(f"Se ha creado {output_pdf_path}")

# función para dividir el PDF
dividir_pdf("pdf_vehiculos.pdf")
