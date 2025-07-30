# 🔄 PDF Merger + PDF/A Converter (GUI con Tkinter)

Este programa te permite combinar múltiples archivos PDF con un archivo PDF adicional específico, y luego convertir automáticamente cada resultado al estándar **PDF/A** (ideal para archivado a largo plazo).

## ✨ Funcionalidades

- 📁 Selección de una carpeta con múltiples archivos PDF.
- ➕ Selección de un PDF adicional que se añadirá a cada uno.
- 🔗 Unión automática: se genera un nuevo PDF que une el archivo original con el archivo adicional.
- 🧾 Conversión de cada PDF combinado a **PDF/A** utilizando **Ghostscript**.
- 🗑️ Eliminación automática de archivos temporales: solo se conservan los archivos finales en formato PDF/A.
- 🔁 Interfaz de bucle: puedes repetir el proceso fácilmente las veces que desees.
- 🪧 Instrucciones claras antes de cada ejecución.

## 🖥️ Requisitos

### 📦 Dependencias de Python

Instala las siguientes bibliotecas:

pip install PyPDF2

Si se ejecuta desde el propio codigo o desde el ejecutable .exe se debe tener en cuenta mantener en el mismo directorio que el archivo .py lo siguiente:

- gsdll64.dll
- gsdll64.lib
- gswin64c.exe

El ejecutable se encuentra en la siguiente direccion:
- https://drive.google.com/drive/folders/1bzcrcuS0w3mK-gdIhvel4dYdp9WQbT_Q?usp=sharing
