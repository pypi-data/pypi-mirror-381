import os

from pypdf import PdfReader

from msgflux.data.parsers.base import BaseParser
from msgflux.data.parsers.types import PdfParser


@dataclass
class ParserResult:
    data: str
    score: Optional[float]
    images: Optional[List[str]]

@dataclass
class RetrieverResults:
    results: List[RetrieverResult]

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional


@dataclass
class ParsedFile:
    file_type: str

    filename: str
    title: Optional[str] = None
    created_at: Optional[datetime] = None
    tags: Optional[List[str]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)



# TODO: convert image ot base64
class PyPDFPdfParser(BaseParser, PdfParser):
    def pdf_parser(self):
        """Parser de PDF que converte o conteúdo em Markdown e extrai imagens.

        Args:
            path (str): Caminho do arquivo PDF.
            save_imgs (str, optional): Diretório para salvar as imagens extraídas.

        Returns:
            tuple: (conteúdo em Markdown, dicionário com imagens {nome: dados})
        """

        def _convert(path):
            md_content = ""
            image_dict = {}
            reader = PdfReader(path)
            num_pages = len(reader.pages)

            # Itera sobre cada página do PDF
            for idx in range(num_pages):
                page = reader.pages[idx]

                # Adiciona um comentário com o número da página (similar ao PPTX)
                md_content += f"\n\n<!-- Page number: {idx + 1} -->\n"

                text = page.extract_text(
                    extraction_mode="layout", layout_mode_space_vertically=False
                )
                md_content += text.strip() + "\n"

                for count, image_file_object in enumerate(page.images):
                    img_extension = image_file_object.name.split(".")[-1]
                    img_name = f"image_page{idx + 1}_{count}.{img_extension}"
                    img_data = image_file_object.data

                    image_dict[img_name] = img_data

                    md_content += f"\n![{img_name}]({img_name})\n"

            return md_content.strip(), image_dict

        return _convert(self)
