sudo docker run -it --gpus=all --ipc=host \
 -v $(pwd):/app \
 -p 80:80 \
 dream:v0