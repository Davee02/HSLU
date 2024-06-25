url = "https://docs.docugatetest.cloud"
loader = RecursiveUrlLoader(
    url=url, max_depth=10, extractor=lambda x: bs4.BeautifulSoup(x, "html.parser").text
)
docs = loader.load()