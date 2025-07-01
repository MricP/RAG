from langchain_community.document_loaders import PyPDFLoader
import asyncio
# "./docs-pdf/c-api.pdf"
async def loadPdf(filepath : str):
    loader = PyPDFLoader(filepath)
    pages = []
    async for page in loader.alazy_load():
        pages.append(page)
    return pages


if __name__ == "__main__":
    pages = asyncio.run(loadPdf("./docs-pdf/c-api.pdf"))
    for page in pages:
        print(page.page_content)
