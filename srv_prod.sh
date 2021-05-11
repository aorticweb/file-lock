#!/bin/bash
# Start Api for development with automatic code updates
# To change permissions
# chmod 767 ./srv_prod.sh
docker run -d --name file-lock -p 80:80 aorticweb/file-lock:dev 
echo "File-Lock running on localhost:80"
read -n1 -r -p "Press any key to kill the File-Lock instance..." key
docker kill file-lock > /dev/null 2> /dev/null
wait
docker rm file-lock > /dev/null 2> /dev/null
echo "File-Lock has been killed and removed succesfully"
