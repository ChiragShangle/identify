import script

def linker(language, search_keyword, face_search=None, file_format=None, file=None):
    if not face_search:
        obj = script.ArchiveIdentifier(language=language, search_keyword = search_keyword, file_format = file_format, file=file)
        obj.run()
        obj.search_and_display()
