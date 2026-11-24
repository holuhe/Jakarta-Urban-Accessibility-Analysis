import pandas as pd
import re

def normalize(s, sub, key):
    if pd.isna(s):
        return None
    s = str(s).lower()
    s = re.sub(sub, key, s)
    s = re.sub(r"\s+", " ", s).strip()
    return s