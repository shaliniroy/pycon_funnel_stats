import urllib2
from bs4 import BeautifulSoup
x = urllib2.urlopen("http://in.pycon.org/funnel/2013/")
y = x.read()
c=[]
i,j=0,0
name, fname = [], []
soup = BeautifulSoup(y)
b = soup.find_all('td')
for z in b:
    c.append(z.get_text())
l = len(soup.find_all(colspan="8"))
while j<l:
    while i<11:
        name.append(c.pop(0))
        i+=1
    fname.append(name)
    name=[]
    j+=1
    i=0
sum=sum1=sum2=sum3=inter=beg=adv=sum4=sum5=sum6=sum7=sum8=sum9=sum0=sci=soft=infr=web=emb=cor=work=sum4b=sum5b=sum6b=sum7b=sum8b=sum9b=sum0b=scib=softb=infrb=webb=embb=corb=workb=sum4a=sum5a=sum6a=sum7a=sum8a=sum9a=sum0a=scia=softa=infra=weba=emba=cora=worka=0
v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
for u in fname:
    sum=sum+int(u[8])
    if u[7]== "Intermediate":
        sum1=sum1+int(u[8])
        inter+=1
        if u[5]== "Scientific Computing":
	    sum4=sum4+int(u[8])
	    sci+=1
	    v1.append(u)
	if u[5]== "Software Development Tools":
	    sum5=sum5+int(u[8])
	    soft+=1
	    v2.append(u)
	if u[5]== "Infrastructure":
	    sum6=sum6+int(u[8])
	    infr+=1
	    v3.append(u)
	if u[5]== "Web Development":
	    sum7=sum7+int(u[8])
	    web+=1
	    v4.append(u)
	if u[5]== "Embedded/Real-time Python":
	    sum8=sum8+int(u[8])
	    emb+=1
	    v5.append(u)
	if u[5]== "Core Python":
            sum9=sum9+int(u[8])
	    cor+=1
	    v6.append(u)
	if u[5]== "Workshops":
	    sum0=sum0+int(u[8])
	    work+=1
	    v7.append(u)
    if u[7]== "Beginner":
        sum2=sum2+int(u[8])
        beg+=1
	if u[5]== "Scientific Computing":
            sum4b=sum4b+int(u[8])
            scib+=1
	    v8.append(u)
        if u[5]== "Software Development Tools":
            sum5b=sum5b+int(u[8])
            softb+=1
	    v9.append(u)
        if u[5]== "Infrastructure":
            sum6b=sum6b+int(u[8])
            infrb+=1
	    v10.append(u)
        if u[5]== "Web Development":
            sum7b=sum7b+int(u[8])
            webb+=1
	    v11.append(u)
        if u[5]== "Embedded/Real-time Python":
            sum8b=sum8b+int(u[8])
            embb+=1
	    v12.append(u)
        if u[5]== "Core Python":
            sum9b=sum9b+int(u[8])
            corb+=1
	    v13.append(u)
        if u[5]== "Workshops":
            sum0b=sum0b+int(u[8])
            workb+=1
	    v14.append(u)
    if u[7]== "Advanced":
        sum3=sum3+int(u[8])
        adv+=1
	if u[5]== "Scientific Computing":
            sum4a=sum4a+int(u[8])
            scia+=1
	    v15.append(u) 
        if u[5]== "Software Development Tools":
            sum5a=sum5a+int(u[8])
            softa+=1
	    v16.append(u)
        if u[5]== "Infrastructure":
            sum6a=sum6a+int(u[8])
            infra+=1
	    v17.append(u)
        if u[5]== "Web Development":
            sum7a=sum7a+int(u[8])
            weba+=1
	    v18.append(u)
        if u[5]== "Embedded/Real-time Python":
            sum8a=sum8a+int(u[8])
            emba+=1
	    v19.append(u)
        if u[5]== "Core Python":
            sum9a=sum9a+int(u[8])
            cora+=1
	    v20.append(u)
        if u[5]== "Workshops":
            sum0a=sum0a+int(u[8])
            worka+=1
	    v21.append(u)

if sum!=0:
    overallaveragelikes = sum/l
    print "Over all average likes=",overallaveragelikes
else:
    print "There is no proposal for talks"

if sum1!=0:
    avgvotesforinter= sum1/inter
    print "Average votes for intermediate level=",avgvotesforinter
else:
    print "There is no proposal under Intermediate level"
if sum2!=0:
    avgvotesforbeg= sum2/beg
    print "Average votes for beginner level=",avgvotesforbeg
else:
    print "There is no proposal under Beginner level"

if sum3!=0:
    avgvotesforadv= sum3/adv
    print "Average votes for advanced level=",avgvotesforadv
else:
    print "There is no proposal under advancel level"

if sum4!=0:
    avgvotesforinterforsci = sum4/sci
    print "Average votes for intermediate level for Scientific Computing=",avgvotesforinterforsci
else:
    print "There is no proposal for intermediate level for Scientific Computing"

if sum5!=0:
    avgvotesforinterforsoft = sum5/soft
    print "Average votes for intermediate level for Software Development Tools=",avgvotesforinterforsoft
else:
    print "There is no proposal for intermediate level for Software Development Tools"

if sum6!=0:
    avgvotesforinterforinfr = sum6/infr
    print "Average votes for intermediate level for Infrastructure=",avgvotesforinterforinfr
else:
    print "There is no proposal for intermediate level for Infrastructure"

if sum7a!=0:
    avgvotesforinterforweb = sum7/web
    print "Average votes for intermediate level for Web Development=",avgvotesforinterforweb
else:
    print "There is no proposal for intermediate level for Web Development"

if sum8!=0:
    avgvotesforinterforemb = sum8/emb
    print "Average votes for intermediate level for Embedded/Real-time Python=",avgvotesforinterforemb
else:
    print "There is no proposal for intermediate level for Embedded/Real-time Python"

if sum9!=0:
    avgvotesforinterforcor = sum9/cor
    print "Average votes for intermediate level for Core Python=",avgvotesforinterforcor
else:
    print "There is no proposal for intermediate level for Core Python"

if sum0!=0:
    avgvotesforinterforwork = sum0/work
    print "Average votes for intermediate level for Workshops=",avgvotesforinterforwork
else:
    print "There is no proposal for intermediate level for Workshops"

if sum4b!=0:
    avgvotesforinterforscib = sum4b/scib
    print "Average votes for Beginner level for Scientific Computing=",avgvotesforinterforscib
else:
    print "There is no proposal for Beginner level for Scientific Computing"

if sum5b!=0:
    avgvotesforinterforsoftb = sum5b/softb
    print "Average votes for Beginner level for Software Development Tools=",avgvotesforinterforsoftb
else:
    print "There is no proposal for Beginner level for Software Development Tools"

if sum6b!=0:
    avgvotesforinterforinfrb = sum6b/infrb
    print "Average votes for Beginner level for Infrastructure=",avgvotesforinterforinfrb
else:
    print "There is no proposal for Beginner level for Infrastructure"

if sum7b!=0:
    avgvotesforinterforwebb = sum7b/webb
    print "Average votes for Beginner level for Web Development=",avgvotesforinterforwebb
else:
    print "There is no proposal for Beginner level for Web Development"

if sum8b!=0:
    avgvotesforinterforembb = sum8b/embb
    print "Average votes for Beginner level for Embedded/Real-time Python=",avgvotesforinterforembb
else:
    print "There is no proposal for Beginner level for Embedded/Real-time Python"

if sum9b!=0:
    avgvotesforinterforcorb = sum9b/corb
    print "Average votes for Beginner level for Core Python=",avgvotesforinterforcorb
else:
    print "There is no proposal for Beginner level for Core Python"

if sum0b!=0:
    avgvotesforinterforworkb = sum0b/workb
    print "Average votes for Beginner level for Workshops=",avgvotesforinterforworkb
else:
    print "There is no proposal for Beginner level for Workshops"

if sum4a!=0:
    avgvotesforinterforscia = sum4a/scia
    print "Average votes for Advanced level for Scientific Computing=",avgvotesforinterforscia
else:
    print "There is no proposal for advanced level for Scientific Computing"

if sum5a!=0:
    avgvotesforinterforsofta = sum5a/softa
    print "Average votes for Advanced level for Software Development Tools=",avgvotesforinterforsofta
else:
    print "There is no proposal for advanced level for Software Development Tools"

if sum6a!=0:
    avgvotesforinterforinfra = sum6a/infra
    print "Average votes for Advanced level for Infrastructure=",avgvotesforinterforinfra
else:
    print "There is no proposal for advanced level for Infrastructure"

if sum7a!=0:
    avgvotesforinterforweba = sum7a/weba
    print "Average votes for Advanced level for Web Development=",avgvotesforinterforweba
else:
    print "There is no proposal for advanced level for Web Developement"

if sum8a!=0:
    avgvotesforinterforemba = sum8a/emba
    print "Average votes for Advanced level for Embedded/Real-time Python=",avgvotesforinterforemba
else:
    print "There is no proposal for advanced level for Embedded/Real-time Python"

if sum9a!=0:
    avgvotesforinterforcora = sum9a/cora
    print "Average votes for Advanced level for Core Python=",avgvotesforinterforcora
else:
    print "There is no proposal for advanced level for Core Python"

if sum0a!=0:
    avgvotesforinterforworka = sum0a/worka
    print "Average votes for Advanced level for Workshops=",avgvotesforinterforworka
else:
    print "There is no proposal for advanced level for Workshops"

print "Total Number of people applied for talks=",l
print "Total Number of proposals under intermediate level=",inter
print "Total Number of proposals under beginner level=",beg
print "Total Number of proposals under advanced level=",adv
# //Intermediate level//*/
print "Number of proposals for Scientific Computing=",sci
print "Number of proposals for Software Development Tools=",soft
print "Number of proposals for Infrastructure=",infr
print "Number of proposals for Web Developemnt=",web
print "Number of proposals for Embedded/Real-Time Python=",emb
print "Number of proposals for Core Python=",cor
print "Number of proposals for Workshops=",work
# //Beginner level// */
print "Number of proposals for Scientific Computing=",scib
print "Number of proposals for Software Development Tools=",softb
print "Number of proposals for Infrastructure=",infrb
print "Number of proposals for Web Developemnt=",webb
print "Number of proposals for Embedded/Real-Time Python=",embb
print "Number of proposals for Core Python=",corb
print "Number of proposals for Workshops=",workb
# //Advanced level//*/
print "Number of proposals for Scientific Computing=",scia
print "Number of proposals for Software Development Tools=",softa
print "Number of proposals for Infrastructure=",infra
print "Number of proposals for Web Developemnt=",weba
print "Number of proposals for Embedded/Real-Time Python=",emba
print "Number of proposals for Core Python=",cora
print "Number of proposals for Workshops=",worka
#like-wise arrangement along with level wise and section wise
##1
v11a,v11b = [],[]
for x in v1:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v1=sorted(v11b)
print len(v1)
v1=reversed(v1)
for x in v1:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"
##2
v11a,v11b = [],[]
for x in v2:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v2=sorted(v11b)
print len(v2)
v2=reversed(v2)
for x in v2:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"

##3
v11a,v11b = [],[]
for x in v3:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v3=sorted(v11b)
print len(v3)
v3=reversed(v3)
for x in v3:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"
##4
v11a,v11b = [],[]
for x in v4:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v4=sorted(v11b)
print len(v4)
v4=reversed(v4)
for x in v4:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"
##5
v11a,v11b = [],[]
for x in v5:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v5=sorted(v11b)
print len(v5)
v5=reversed(v5)
for x in v5:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"
##6
v11a,v11b = [],[]
for x in v6:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v6=sorted(v11b)
print len(v6)
v6=reversed(v6)
for x in v6:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"
##7
v11a,v11b = [],[]
for x in v7:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v7=sorted(v11b)
print len(v7)
v7=reversed(v7)
for x in v7:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"
##8
v11a,v11b = [],[]
for x in v8:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v8=sorted(v11b)
print len(v8)
v8=reversed(v8)
for x in v8:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"
##9
v11a,v11b = [],[]
for x in v9:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v9=sorted(v11b)
print len(v9)
v9=reversed(v9)
for x in v9:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"
##10
v11a,v11b = [],[]
for x in v10:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v10=sorted(v11b)
print len(v10)
v10=reversed(v10)
for x in v10:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"
##11
v11a,v11b = [],[]
for x in v11:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v11=sorted(v11b)
print len(v11)
v11=reversed(v11)
for x in v11:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"
##12
v11a,v11b = [],[]
for x in v12:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v12=sorted(v11b)
print len(v12)
v12=reversed(v12)
for x in v12:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"
##13
v11a,v11b = [],[]
for x in v13:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v13=sorted(v11b)
print len(v13)
v13=reversed(v13)
for x in v13:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"
##14
v11a,v11b = [],[]
for x in v14:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v14=sorted(v11b)
print len(v14)
v14=reversed(v14)
for x in v14:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"
##15
v11a,v11b = [],[]
for x in v15:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v15=sorted(v11b)
print len(v15)
v15=reversed(v15)
for x in v15:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"
##16
v11a,v11b,m = [],[],[]
for x in v16:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v16=sorted(v11b)
print len(v16)
v16=reversed(v16)
for x in v16:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"
##17
v11a,v11b = [],[]
for x in v17:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v17=sorted(v11b)
print len(v17)
v17=reversed(v17)
for x in v17:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"
##18
v11a,v11b = [],[]
for x in v18:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v18=sorted(v11b)
print len(v18)
v18=reversed(v18)
for x in v18:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"
##19
v11a,v11b = [],[]
for x in v19:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v19=sorted(v11b)
print len(v19)
v19=reversed(v19)
for x in v19:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"
##20
v11a,v11b = [],[]
for x in v20:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v20=sorted(v11b)
print len(v20)
v20=reversed(v20)
for x in v20:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"
##21
v11a,v11b = [],[]
for x in v21:
    v11a.append(int(x[8]))
    v11a.append(x[3])
    v11a.append(x[5])
    v11a.append(x[1])
    v11b.append(v11a)
    v11a=[]
v21=sorted(v11b)
print len(v21)
v21=reversed(v21)
for x in v21:
    print x[1], "has", x[0], "likes on the topic (", x[3], ")"
    print x

