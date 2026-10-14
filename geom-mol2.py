from pathlib import Path

from ccdc.io import MoleculeWriter
from ccdc.search import SMARTSSubstructure, TextNumericSearch

from bsubpc.strings import TEMPLATE_SMARTS

outdir = Path('mol2')
outdir.mkdir()

with open('dois.txt') as f:
    dois = [line.strip() for line in f if line.strip()]

template = SMARTSSubstructure(TEMPLATE_SMARTS)

for doi in dois:
    query = TextNumericSearch()
    query.add_doi(doi, mode='exact')
    hits = query.search()
    assert len(hits) > 0
    for hit in hits:
        refcode = hit.identifier
        matching = [c for c in hit.molecule.components if template.match_molecule(c)]
        if matching:
            outpath = outdir / f'{refcode}.mol2'
            with MoleculeWriter(outpath) as writer:
                writer.write(matching[0])
