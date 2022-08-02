class ItalicStr(str):
    def _repr_html_(self):
        return f'<i>{self}</i>'
    
ItalicStr('Hello World')