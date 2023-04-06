# change the base image with the one that contains the cuda toolkit compatible with your machine
FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime
WORKDIR /app

# install requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy the accelerate-configuration file
COPY /accelerate_config.yaml /.cache/hugginface/accelerate/default_config.yaml

# entrypoint is uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

