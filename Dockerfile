#use a lightweight Python 3.11 environment
FROM python:3.11-slim

WORKDIR /app

#copy files
COPY rare_variant_filter.py .
COPY input_variants.csv .
#install dependencies
RUN pip install --no-cache-dir pandas
#run a demo
CMD ["python", "-c", "from rare_variant_filter import filter_rare_variants; import pandas as pd; df=pd.read_csv('input_variants.csv'); print('Demo container ready')"]
