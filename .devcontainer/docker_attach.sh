DIRECTORY_NAME="applications"
IMAGE_NAME="applications.mothakes.com.image"
CONTAINER_NAME="applications.mothakes.com.container"
HOST_PORT="3001"
CONTAINER_PORT="3000"


docker container run \
    -it \
    --rm \
    --name $IMAGE_NAME \
    --user vscode \
    --mount type=bind,source=/home/ubuntu/Projects/$DIRECTORY_NAME,target=/workspace/$DIRECTORY_NAME \
    --workdir /workspace/$DIRECTORY_NAME \
    --publish $HOST_PORT:$CONTAINER_PORT \
    $IMAGE_NAME /bin/bash && pip3 install -r requirements.txt
