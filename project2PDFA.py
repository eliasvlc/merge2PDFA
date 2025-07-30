import os
import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import subprocess
import tempfile
import sys


def merge_pdfs(pdf1, pdf2, output_path):
    pdf_merger = PyPDF2.PdfMerger()
    pdf_merger.append(pdf2)
    pdf_merger.append(pdf1)
    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)

def convert_to_pdfa(input_path, output_path):
    # Detectar si estamos ejecutando como .exe con PyInstaller
    if getattr(sys, 'frozen', False):
        ghostscript_path = os.path.join(sys._MEIPASS, "gswin64c.exe")
    else:
        ghostscript_path = "gswin64c"  # Usa lo que tengas instalado o en PATH

    try:
        subprocess.run([
            ghostscript_path,
            "-dPDFA",
            "-dBATCH",
            "-dNOPAUSE",
            "-dNOOUTERSAVE",
            "-sProcessColorModel=DeviceCMYK",
            "-sDEVICE=pdfwrite",
            "-sPDFACompatibilityPolicy=1",
            f"-sOutputFile={output_path}",
            input_path
        ], check=True)
        print(f"✅ PDF/A generado: {output_path}")
    except subprocess.CalledProcessError:
        print(f"❌ Error al convertir {input_path} a PDF/A")


def select_folder():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory()

def select_file():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

def continue_prompt():
    root = tk.Tk()
    root.withdraw()
    return messagebox.askyesno("Continuar", "¡Completado!\n¿Deseas generar más uniones PDF?")

def main():
    continue_generation = True
    while continue_generation:
        # Mostrar instrucciones siempre antes de iniciar el proceso
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo(
            "Cómo funciona",
            "📝 Instrucciones:\n\n"
            "- Selecciona una carpeta con varios PDFs.\n"
            "- Luego elige un PDF único que se unirá a cada uno.\n"
            "- Se generarán nuevos PDFs combinados y convertidos a PDF/A.\n"
            "- Solo se conservarán los archivos PDF/A finales.\n\n"
            "¡Haz clic en 'Aceptar' para comenzar!"
        )

        folder_path = select_folder()
        if not folder_path:
            continue_generation = continue_prompt()
            continue

        unique_pdf = select_file()
        if not unique_pdf:
            continue_generation = continue_prompt()
            continue

        output_folder = os.path.join(folder_path, os.path.basename(folder_path))
        os.makedirs(output_folder, exist_ok=True)

        for filename in os.listdir(folder_path):
            if filename.endswith(".pdf") and filename != os.path.basename(unique_pdf):
                pdf_path = os.path.join(folder_path, filename)
                output_pdfa_path = os.path.join(output_folder, filename)

                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                    temp_merged_path = tmp_file.name
                merge_pdfs(pdf_path, unique_pdf, temp_merged_path)
                convert_to_pdfa(temp_merged_path, output_pdfa_path)
                os.remove(temp_merged_path)

        continue_generation = continue_prompt()


if __name__ == "__main__":
    main()
