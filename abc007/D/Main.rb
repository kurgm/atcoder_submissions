f=->i{r=(x=i.to_s).size;x.chars{|y|i-=((z=y.to_i)-z/5)*8**r-=1;"49"[y]&&break};i};gets=~/ /;p f[$'.to_i+1]-f[$`.to_i]