import re
import pandas as pd
import numpy as np
from datetime import datetime

def extract_features(url):
    return [
        len(url),
        url.count('@'),
        url.count('.'),
        url.count('-'),
        url.count('/'),
        1 if re.search(r'https?://', url) else 0,
        1 if re.search(r'\d+', url) else 0
    ]

def extract_features_from_dataframe(urls):
    return pd.DataFrame([extract_features(url) for url in urls])

