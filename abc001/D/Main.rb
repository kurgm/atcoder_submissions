a=[u=0]*481;$<.each{|l|l=~/-/;a[$`.to_i/5]+=1;a[(e=$'.to_i+4)/5+e%100/60*8]-=1};481.times{|i|$><<"%04d%c"%[i*5,u>0??-:$/]if(v=u)>0!=0<u+=a[i]}