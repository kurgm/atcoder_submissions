a,*b=$<.map &:split;puts [0].product(*b).any?{|q|1>eval(q*?^)}?:Found: :Nothing