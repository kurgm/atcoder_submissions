a,b,c,d,e,f,g,*h=`ul`.split.map &:to_i;puts h.each_slice(2).all?{|i,j|Math.hypot(i-a,j-b)+Math.hypot(i-c,j-d)>e*f}?:NO: :YES