f=->x,r=0{s=0;x-=q=x%10;q.times{|i|s+=10**r-((x+i).to_s=~/[49]/?0:8**r)};x>9?s+f[x/10,r+1]:s};a,b=gets.split;p f[b.to_i+1]-f[a.to_i]