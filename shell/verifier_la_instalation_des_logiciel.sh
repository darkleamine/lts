#!/bin/bash
chmod +x verifier_la_instalation_des_logiciel.sh $2
    echo $1 $2 $3
  apt-cache pkgnames  > log_install.txt
   var=$(grep -c $1 log_install.txt)
#  -gt == supereur
# -eq == equivalant
 if [ $var -eq "1" ];
  then
    echo "package non installier";echo ./$2 $3;
    ./$2 $3;
  else   echo "package  installier";fi
