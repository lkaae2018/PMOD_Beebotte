#!/bin/bash

#cd linuxopg
sudo git add *
sudo git config --global user.email "lak@djhhadsten.dk"
sudo git config --global user.name "lkaae2018"
echo Navn til commiten?
read commit
sudo git commit -m $commit
sudo git push
