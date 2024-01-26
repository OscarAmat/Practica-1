ingrese_archivo = input("Ingrese el nombre de archivo: ")

mime = ingrese_archivo.split('.')[-1]

lista_mime = {
    'gif': 'image/gif',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'zip': 'application/zip'}
obtener_mime = lista_mime.get(mime,"application/octet-stream")

print({obtener_mime})