a,b,c,d,e,f,g,*h=`ul`.split.map &:to_i;k=->l,m{(l*l+m*m)**0.5};puts h.each_slice(2).all?{|i,j|k[i-a,j-b]+k[i-c,j-d]>e*f}?:NO: :YES