gets p;r=*1..13;p r.index{|t|r.combination(t).all?{|u|!u.combination(2).all?{|x|~/
#{x*?\s}/}}}