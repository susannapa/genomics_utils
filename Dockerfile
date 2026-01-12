#use a lightweight Python 3.11 environment
FROM python:3.11-slim

WORKDIR /app

#copy files
COPY rare_variant_filter.py .
COPY input_variants.csv .
#install dependencies
RUN pip install --no-cache-dir pandas
#run the variant filter script
CMD ["python", "-c", "from rare_variant_filter import filter_rare_variants; import pandas as pd; df = pd.read_csv('input_variants.csv'); variants = df.to_dict(orient='records'); filtered = filter_rare_variants(variants); print('Filtered variants:'); print(filtered)"]
