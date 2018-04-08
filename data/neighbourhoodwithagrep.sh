#!/bin/bash


#while Grand Total: 0 match(es) found.

#  agrep -0 "^$word\$"" dictionary.txt


while read -r word
do
  for NEIGHBOUR in {0..10}
  do
    if ! [[ $(agrep -"$NEIGHBOUR" "^$word\$" dictionary.txt) == "Grand Total: 0 match(es) found." ]]
        then
            agrep -$NEIGHBOUR ^$word\$ dictionary.txt | head -1
            break
    fi

    # echo "^$word\$"
    # [  ] || echo found; break
  done
done < "$1"
