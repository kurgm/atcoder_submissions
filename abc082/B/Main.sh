read s;read t;s=`echo $s|fold -w1|sort`;t=`echo $t|fold -w1|sort -r`;[ "$s" \< "$t" ]&&echo Yes||echo No