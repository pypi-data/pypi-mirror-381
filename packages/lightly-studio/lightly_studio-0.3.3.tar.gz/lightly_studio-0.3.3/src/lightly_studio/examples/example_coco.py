"""Example of how to add samples in coco format to a dataset."""

import lightly_studio as ls

# Create a DatasetLoader from a path
dataset = ls.Dataset.create()
dataset.add_samples_from_coco(
    annotations_json="/path/to/your/dataset",
    images_path="/path/to/your/dataset",
    annotation_type=ls.AnnotationType.INSTANCE_SEGMENTATION,
)

ls.start_gui()
