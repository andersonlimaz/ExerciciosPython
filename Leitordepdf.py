import PyPDF2
#Abrindo o arquivo em modo leitura e lendo o binário
pdf_file = open('pdf_sample_2.pdf', 'rb')
#Após pegar o binário, pegamos os dados de PDF desse Binario
dados_do_pdf = PyPDF2.PdfReader(pdf_file)

print(len(dados_do_pdf.pages))
#setando a variavel pagina1 com o objeto pagina1
pagina1 = dados_do_pdf.pages[0]
#pagando o texto extraido da pagina1 
texto_pagina1 = pagina1.extract_text()

print(texto_pagina1)