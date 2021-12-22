#!/bin/bash

# user doesn't input parameter
if [ $# -eq 0 ]; then 
	echo "please input filename or exit code..."
	exit 0
fi

# user input 'push' 
if [ "$1" == "push" ]; then
	IFS_B="$IFS"
	IFS=$'\n'
	arr=(`cat /home/lee/alist`)
	for i in ${arr[@]}
	do
		name="$(echo "${i}" | cut -d',' -f1)"
		commit="$(echo "${i}" | cut -d',' -f2)"
		
		cd /home/lee/Algorithm_Study
		
		git add "${name}"

		git commit -m "[ADD] "${name}""
		
		if [ ! -z "${commit}" ]; 
		then
			
			git commit --amend --no-edit --date ""${commit}" 2021 10:11:11 KST";
		fi
		
		git push	
	done

	IFS="$IFS_B"
	cat /dev/null > /home/lee/alist
	exit 0
fi

touch /home/lee/alist

if [ $# -eq 2 ]; 
then
	echo "${1},${2}" >> /home/lee/alist
else
	echo "${1}," >> /home/lee/alist
fi

code /home/lee/Algorithm_Study/${1}

exit 0
