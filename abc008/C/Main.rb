c,*a=$<.map &:to_i;s=0;a.map{|x|i=a.count{|y|x%y<1};s+=(-~i/2).to_f/i};p s