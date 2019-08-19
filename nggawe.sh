#!/bin/bash

function nggawe() {
    cd
    python3 /home/rh/projects/project-init-automation/nggawe.py $1 $2
    cd /home/rh/projects/$1
    git init
    git remote add origin https://github.com/$2/$1.git
    echo "# $1" >> README.md
    git add .
    git commit -m "initial commit"
    git push -u origin master
}