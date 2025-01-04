def get_file_category(obj):
    if obj.object_name.endswith((".txt", ".pdf", ".xlsx", ".xls", ".csv", ".docx", ".doc", ".pptx", ".ppt")):
        return "Documentos"
    elif obj.object_name.endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):
        return "Imagen"
    elif obj.object_name.endswith((".mp3", ".wav", ".flac", ".aac", ".ogg")):
        return "Audio"
    elif obj.object_name.endswith((".mp4", ".mkv", ".avi", ".mov", ".wmv")):
        return "Video"
    elif obj.object_name.endswith((".zip", ".tar", ".rar", ".7z")):
        return "Comprimido"
    elif obj.object_name.endswith((".json", ".xml", ".yaml")):
        return "Datos"
    elif obj.is_dir:
        return "Carpeta"
    else:
        return "Otro"
