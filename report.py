from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_pdf(file_name):
    # Create a canvas object with the specified file name and page size
    c = canvas.Canvas(file_name, pagesize=letter)

    # Add text to the PDF
    c.drawString(100, 750, "Hello, World!")

    # Add more content (e.g., images, shapes) as needed

    # Save the PDF
    c.save()


if __name__ == "__main__":
    pdf_file_name = "example.pdf"
    generate_pdf(pdf_file_name)
    print(f"PDF file '{pdf_file_name}' generated successfully.")
