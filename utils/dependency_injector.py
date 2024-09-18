# utils/dependency_injector.py
from services.api_service import ApiService
from services.chroma_service import ChromaService
from services.file_processing_service import FileProcessingService
from intents.api_intent import ApiIntent
from intents.chroma_query_intent import ChromaQueryIntent
from conversation.action_handler import ActionHandler

def build_action_handler():
    # Crear servicios
    chroma_service = ChromaService()
    api_service = ApiService()
    file_processing_service = FileProcessingService(chroma_service)

    # Procesar archivos iniciales
    files_to_process = [
        {'path': 'data/Encomiendas_Express-B.pdf', 'type': 'pdf'},
        #{'path': 'data/datos.xlsx', 'type': 'excel'}
    ]
    file_processing_service.process_initial_files(files_to_process)

    # Crear intents
    chroma_query_intent = ChromaQueryIntent(chroma_service)
    api_intent = ApiIntent(api_service)

    # Lista de intents
    intents = [chroma_query_intent, api_intent]

    # Crear y devolver el ActionHandler
    return ActionHandler(intents)
