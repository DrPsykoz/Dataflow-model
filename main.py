import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

DEBUG_MODE = True

GCP_PROJECT_ID = "MY_PROJECT_ID"
GCP_PROJECT_REGION = "us-central1"
GCP_BUCKET = "MY_GCP_BUCKET"

TEMPLATE_NAME = "MY_NEW_TEMPLATE"

TEMP_LOCATION_GCS = "gs://{GCP_BUCKET}/temp/"
STAGING_LOCATION_GCS = "gs://{GCP_BUCKET}}/staging/"
TEMPLATE_LOCATION_GCS = f"gs://{GCP_BUCKET}/templates/{TEMPLATE_NAME}"

class MyCustomTransform(beam.DoFn):
    def process(self, element):
        yield element.upper()

beam_options = {
    "project": GCP_PROJECT_ID,
    "region": GCP_PROJECT_REGION,
    "runner": "DirectRunner" if DEBUG_MODE else "DataflowRunner",
    "temp_location": TEMP_LOCATION_GCS,
    "staging_location": STAGING_LOCATION_GCS,
    "template_location": TEMPLATE_LOCATION_GCS,
    "setup_file": "./setup.py",
    "save_main_session": True
}
    
with beam.Pipeline(options=PipelineOptions(flags=[], **beam_options)) as pipeline:
  result = (
    pipeline | 'Create a sample data' >> beam.Create(["Hello", "Hello", "Hello"])
             | 'Add World to my data' >> beam.Map(lambda word: f"{word} World")
             | 'Transform to UPPERCASE' >> beam.ParDo(MyCustomTransform())   
             | 'Print in console' >> beam.ParDo(print) 
  )