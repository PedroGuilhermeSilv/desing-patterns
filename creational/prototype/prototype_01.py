from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Document:
    header: str = None
    text_section: str = None
    signature: str = None
    footnote: str = None

    def clone(
        self,
    ) -> Document:
        return deepcopy(self)


pagina01 = Document("titulo", "lorem ipson", "Pedro", "copyrigth")

print("Page 01", pagina01)
pagina02 = pagina01.clone()
pagina02.header = "New header"
print("Page 01", pagina01)
print("Page 02", pagina02)
