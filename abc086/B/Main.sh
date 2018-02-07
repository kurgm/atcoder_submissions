a=`tr -d \ `;for ((;++i*i<a;));do :;done;echo 'Yes 
No'|sed $[(i*i>a)+1]p\;d