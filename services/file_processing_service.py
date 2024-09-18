# services/file_processing_service.py
from file_processing import extract_text_from_pdf, extract_text_from_excel

class FileProcessingService:
    def __init__(self, chroma_service):
        self.chroma_service = chroma_service

    def process_initial_files(self, files_to_process):
        texts = []

        for file_info in files_to_process:
            file_path = file_info['path']
            file_type = file_info['type']

            if file_type == 'pdf':
                text = extract_text_from_pdf(file_path)
            elif file_type == 'excel':
                text = extract_text_from_excel(file_path)
            else:
                raise ValueError(f"Tipo de archivo no soportado: {file_type}")

            texts.append(text)

        # Vectorizar y almacenar los textos usando ChromaService
        self.chroma_service.add_texts(texts)
