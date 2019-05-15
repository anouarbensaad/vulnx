#!/bin/bash
if [[$UID -ne 0]];
then
    echo "YOU MUST RUN WITH ROOT";
else 
    exit;
    