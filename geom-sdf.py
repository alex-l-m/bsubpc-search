from ccdc.io import MoleculeWriter
from ccdc.search import TextNumericSearch

with open("dois.txt") as f:
    dois = [line.strip() for line in f if line.strip()]

with MoleculeWriter("csd-geom.sdf") as writer:
    for doi in dois:
        query = TextNumericSearch()
        query.add_doi(doi, mode="exact")
        hits = query.search()
        assert len(hits) > 0
        for hit in hits:
            writer.write(hit.molecule)
