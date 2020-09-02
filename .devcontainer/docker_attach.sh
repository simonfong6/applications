DIRECTORY_NAME="applications"
IMAGE_NAME="applications.fyi.image"
CONTAINER_NAME="applications.fyi.container"
HOST_PORT="3001"
CONTAINER_PORT="8000"


docker container run \
    -it \
    --rm \
    --name $CONTAINER_NAME \
    --user vscode \
    --mount type=bind,source=/home/ubuntu/projects/$DIRECTORY_NAME,target=/workspace/$DIRECTORY_NAME \
    --workdir /workspace/$DIRECTORY_NAME \
    --publish $HOST_PORT:$CONTAINER_PORT \
    --network applications \
    $IMAGE_NAME /bin/bash && pip3 install -r requirements.txt
