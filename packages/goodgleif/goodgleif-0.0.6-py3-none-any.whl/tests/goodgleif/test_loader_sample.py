from pathlib import Path

import pandas as pd

from goodgleif.loader import build_small_csv


def test_build_small_csv(tmp_path: Path):
    # Create a tiny CSV resembling GLEIF
    src = tmp_path / "gleif.csv"
    df = pd.DataFrame(
        [
            {"LEI": "X1", "Entity.LegalName": "Alpha Inc", "Entity.LegalAddress.Country": "US"},
            {"LEI": "X2", "Entity.LegalName": "Beta LLC", "Entity.LegalAddress.Country": "GB"},
        ]
    )
    df.to_csv(src, index=False)

    out = tmp_path / "gleif_small.csv"
    built = build_small_csv(csv_path=src, out_path=out, n=1)

    assert built.exists()
    df_out = pd.read_csv(built)
    assert len(df_out) == 1


