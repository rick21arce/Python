import pdfkit

pdfkit.from_file(
    input='assets/pagina.html',
    output_path='saida.pdf',
    css='assets/estilo.css',
    option={
        'page-size' : 'A4',
        'margin-top': '0.5in',
        'margin-right': '0.5in',
        'margin-bottom': '0.5in',
        'margin-left': '0.5in',
        'encoding': 'UTF-8'

    }
)