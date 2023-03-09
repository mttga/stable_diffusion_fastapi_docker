# change the base image with the one that contains the cuda toolkit compatible with your machine
FROM pytorch/pytorch:1.13.1-cuda11.6-cudnn8-devel
WORKDIR /app

# install requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# download the models
COPY models tmp/models
RUN python -c "from tmp.models.download_weigths import MODEL_REGISTRY"

# copy the accelerate-configuration file
COPY /accelerate_config.yaml /.cache/hugginface/accelerate/default_config.yaml

# entrypoint is uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

