#!/usr/bin/env bash

function create-component() {
  INDEX_TEMPLATE_URL="https://gist.githubusercontent.com/simonfong6/26a3d94fb82aa62dc2c54b30ffbac6d3/raw/5a14c9c55dd807f766bb2e67c3160b14ffa871a4/index.js"
  COMPONENT_TEMPLATE_URL="https://gist.githubusercontent.com/simonfong6/814cfe57832df5d018e401f57d68a22f/raw/ab83c3b5eba23910f355a94c413da1578ded90a7/ComponentName.jsx"

  INDEX_FILE_NAME="index.js"
  COMPONENT_FILE_NAME="ComponentName.jsx"

  TEMPLATE_STRING="{{ComponentName}}"

  COMPONENT_NAME=$1

  if [ -z "$COMPONENT_NAME" ]; then
    echo "No component given, exiting..."
    exit -1
  fi

  if [ -d "$COMPONENT_NAME" ]; then
    echo "Directory already $COMPONENT_NAME exists."
    echo "Please delete if you want to recreate."
    exit -1
  fi

  echo "Creating component '$COMPONENT_NAME'"

  # Create directory to store the component in.
  mkdir -p $COMPONENT_NAME
  cd $COMPONENT_NAME

  curl -s "$INDEX_TEMPLATE_URL" -o "$INDEX_FILE_NAME"
  curl -s "$COMPONENT_TEMPLATE_URL" -o "$COMPONENT_FILE_NAME"

  # Replace all template occurences.
  sed -i "s/$TEMPLATE_STRING/$COMPONENT_NAME/g" "$INDEX_FILE_NAME"
  sed -i "s/$TEMPLATE_STRING/$COMPONENT_NAME/g" "$COMPONENT_FILE_NAME"

  mv "$COMPONENT_FILE_NAME" "$COMPONENT_NAME.jsx"
}

create-component $1
