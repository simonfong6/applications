# https://certbot.eff.org/lets-encrypt/ubuntuxenial-nginx.html
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update

sudo apt-get install --assume-yes certbot python3-certbot-nginx
