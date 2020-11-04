#!usr/bin/bash

results=$(jps)

echo "${results}"
if [[ "${results}" == *"NodeManager"* ]]; then
echo "Hadoop is Running"
else
echo "Hadoop is NOT!! running"
fi






