m=[[]]*11;1.upto(gets.to_i){|n|$<.map{|l|a,b=l.split.map &:to_i;m[a]|=[b];m[b]|=[a]};p (m[n].flat_map{|o|m[o]}-m[n]-[n]|[]).size}