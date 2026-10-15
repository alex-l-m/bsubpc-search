from pathlib import Path

import pandas as pd
from ccdc.search import SMARTSSubstructure, TextNumericSearch
from ccdc.io import MoleculeWriter

from bsubpc.strings import TEMPLATE_SMARTS

outdir = Path('mol2')
outdir.mkdir()

with open('dois.txt') as f:
    dois = [line.strip() for line in f if line.strip()]

template = SMARTSSubstructure(TEMPLATE_SMARTS)

rows = []
for doi in dois:
    query = TextNumericSearch()
    query.add_doi(doi, mode='exact')
    hits = query.search()
    assert len(hits) > 0
    for hit in hits:
        matching = [c for c in hit.molecule.components if template.match_molecule(c)]
        if matching:
            outmol = matching[0]
            refcode = hit.identifier
            outpath = outdir / f'{refcode}.mol2'
            with MoleculeWriter(outpath) as writer:
                writer.write(outmol)
            rows.append(dict(doi=doi, deposition_number=hit.entry.ccdc_number, refcode=refcode,
                             mol2_path=str(outpath), formal_charge=outmol.formal_charge,
                             disorder_string=hit.entry.disorder_details))

pd.DataFrame(rows).to_csv('entries.csv', index=False)
