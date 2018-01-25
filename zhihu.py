#-*-coding:utf-8-*-
import requests
import re
import datetime
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/59.0.3071.115 Safari/537.36'}
s = requests.Session()
url = 'https://movie.douban.com/subject/26322999/'

#def body():
r = s.get(url)
#r.decode="gbk"
t1 = r.content
p1 = r'<span class="rating_per">(.*)</span>'
text = re.findall(p1,t1)
p2 = '<span property="v:votes">(.*)</span>'
t2 = re.search(p2,t1)
p3 = '<title>.*</title>'
t3 = re.search(p3,t1)
print '                九州·海上牧云记（豆瓣）'
print '    评分人数: %s' % t2.group(1)
people = float(t2.group(1))
#    return text

f1 = open('zhihu.data','r')
d1 = f1.read()
f1.close()
d2 = d1.split('\n')
a = 0
for i in d2:
    if a == 0:
        times = i
    elif a == 1:
        peoples = i
    elif a == 2:
        star = i
    a += 1
time1 = datetime.datetime.now()
time2 = datetime.datetime.strptime(times,'%Y-%m-%d %H:%M:%S.%f')
time3 = time1 - time2
b = 0
for l in str(time3).split(':'):
    if b == 0:
        h = l
    elif b == 1:
        m = l
    elif b == 2:
        s = l
    b += 1

z = float(people) - float(peoples)
for v in star.split('  '):
    if v[0:6] == '五星':
        s5 = v[8:len(v)]
    elif v[0:6] == '四星':
        s4 = v[8:len(v)]
    elif v[0:6] == '三星':
        s3 = v[8:len(v)]
    elif v[0:6] == '二星':
        s2 = v[8:len(v)]
    elif v[0:6] == '一星':
        s1 = v[8:len(v)]

def li(data):
    all = '    '
    score = 0
    l = 0
    print '    时间: %s' % str(datetime.datetime.now())[0:16]+'\n'
    for i in data:
        l += 1
        num = re.sub('%','',i)
        n1 = float(num)/100
    #   i n1 += n1
        if l == 1:
            all += '五星: ' + str(int(people * n1))
            S5 = (float(people * n1) - float(s5)) / z
            n1 *= 10
            print '    五星: %s' % i
        elif l == 2:
            all += '  四星: ' + str(int(people * n1))
            S4 = (float(people * n1) - float(s4)) / z
            n1 *= 8
            print '    四星: %s' % i
        elif l == 3:
            all += '  三星: ' + str(int(people * n1))
            S3 = (float(people * n1) - float(s3)) / z
            n1 *= 6
            print '    三星: %s' % i
        elif l == 4:
            all += '  二星: ' + str(int(people * n1))
            S2 = (float(people * n1) - float(s2)) / z
            n1 *= 4
            print '    二星: %s' % i 
        elif l == 5:
            all += '  一星: ' + str(int(people * n1))
            S1 = (float(people * n1) - float(s1)) / z
            n1 *= 2
            print '    一星: %s' % i
        score += n1
    print '\n    评分: %s' % score
    z1 = '    五星: ↑'+str(S5*100)[0:2]+'%'
    z2 = '  四星: ↑'+str(S4*100)[0:2]+'%'
    z3 = '  三星: ↑'+str(S3*100)[0:2]+'%'
    z4 = '  二星: ↑'+str(S2*100)[0:3]+'%'
    z5 = '  一星: ↑'+str(S1*100)[0:3]+'%\n'
    print '    距上次刷新: '+h+' 时 '+m+' 分 '+s[0:2]+' 秒'
    print all
    print z1+z2+z3+z4+z5
    page =  str(datetime.datetime.now())+'\n' + str(people)+ '\n' + all
    f = open('zhihu.data','w+')
    f.write(page)
    f.close()
li(text)
'''
while True:
    try:
        li(text)
        time.sleep(60)
    except KeyboardInterrupt:
        break
'''
