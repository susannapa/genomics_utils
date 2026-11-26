#use a lightweight Python 3.11 environment
FROM python:3.11-slim

WORKDIR /app

#copy files
COPY rare_variant_filter.py input_variants.csv ./

#run the filter on the example file (mount your own file to /data to use it instead)
ENTRYPOINT ["python", "rare_variant_filter.py"]
CMD ["input_variants.csv"]
