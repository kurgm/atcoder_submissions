r,c,x,y,d,l=gets(p).split.map &:to_i;C=->n,r{n<r ?0:(n-r+1..n).inject(1,:*)/(1..r).inject(1,:*)};a=0;9.times{|g|a+=C[(x-g/3)*(y-g%3),d+l]*[g==4?4:1,-2][g%2]};p (r-x+1)*(c-y+1)*C[d+l,d]*(x==y&&y==1?1:a)%1000000007