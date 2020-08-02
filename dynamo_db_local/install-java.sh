# Install OpenJDK-8
sudo apt-get update && \
    apt-get install --assume-yes  \
    openjdk-8-jdk \
    ant && \
    apt-get clean;

# Fix certificate issues
sudo apt-get update && \
    apt-get install --assume-yes ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

# Setup JAVA_HOME -- useful for docker commandline
export JAVA_HOME='/usr/lib/jvm/java-8-openjdk-amd64/'
