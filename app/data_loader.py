"""
data_loader.py
-------------
Este módulo se encarga de cargar y procesar el archivo PDF del gimnasio.
Convierte el contenido del PDF en un formato estructurado que puede ser 
utilizado por el sistema RAG (Retrieval Augmented Generation).

Principales funciones:
- load_data(): Carga y procesa el PDF, dividiendo el contenido en secciones
"""

# Importaciones necesarias para el procesamiento de PDFs y logging
import pdfplumber  # Para extraer texto de PDFs



def load_data():
    """
    Carga y procesa el PDF del gimnasio, extrayendo su contenido y 
    organizándolo en secciones estructuradas.

    Returns:
        list: Lista de diccionarios con el siguiente formato:
            {
                "text": str (contenido completo de la sección),
                "title": str (título de la sección)
            }
            
    Proceso:
    1. Abre el PDF usando pdfplumber.
    2. Extrae el texto completo.
    3. # TAREA DEL WORKSHOP: Dividir el contenido en secciones basadas en títulos numerados.
    4. Organiza el contenido en una estructura de datos manejable.
    """
    try:
        data = []
        current_section = ""
        current_title = ""
        pdf_path = "data/Gym_dream.pdf" # Definir ruta para fácil modificación
        
        print(f"Intentando abrir el PDF: {pdf_path}")
        with pdfplumber.open(pdf_path) as pdf:
            print(f"PDF '{pdf_path}' abierto correctamente. Extrayendo texto...")
            
            # Código original para extraer todo el texto del PDF y concatenarlo
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
            
            # Dividir el texto en líneas para procesamiento
            sections = text.split("\n")
            
            # Procesar cada línea del texto
            for line in sections:
                line = line.strip()
                if line:
                    if line.startswith(("1.","2.","3.","4.","5.","6.","7.","8.","9.","10.")):
                        if current_section:
                            data.append({
                                "text": f"{current_title}\n{current_section.strip()}",
                                "title": current_title
                            })

                            #Iniciar sección
                            current_title = line
                            current_section = ""
                    else:
                        current_section += line + "\n"
            if current_section:
                data.append({
                    "text": f"{current_title}\n{current_section.strip()} ",
                    "title": current_title
                })

                
            # Guardar la última sección procesada (para no perder la última parte)
            
            
        # Mostrar las secciones procesadas para verificación
        print("\n=== Secciones procesadas ===")
        for i, item in enumerate(data, 1):
            print(f"\nSección {i}:")
            print(item["text"])
        
        return data
        
    except Exception as e:
        # En caso de error, registrar y devolver lista vacía
        print(f"ERROR al cargar datos: {str(e)}")
        return []

# Punto de entrada para ejecución directa del script
if __name__ == "__main__":
    print("Ejecutando carga de datos directamente...")
    result = load_data()
    print(f"\nResultado final: {len(result)} secciones cargadas")
