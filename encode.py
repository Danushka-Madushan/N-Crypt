import random
import binascii

Special = [' ', '~`!@','$%^&','*()-','_+={','}[]|','\\/:;','"\'<>', ',.?#']
KeyList = ['', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
NumList = ['01', '23', '45', '67', '89']

CRC = lambda e:str(binascii.crc32(e.encode('utf-8')))

def RandKey(a):
	j = []
	for x in range(len(a)):
		j.append(x)
		random.shuffle(j)
	e = j.index(0)
	j.insert(0, 0)
	j.pop(e+1)
	return j

def ArrKey(j, a):
	e = j.index(0)
	j.insert(0, 0)
	j.pop(e+1)
	s = []
	for x in range(len(j)):
		s.append(a[j[x]])
	return s

def Randomize(str):
	e = ''
	for x in range(len(str)):
		j = random.randint(1, 4)
		e+= str[:j]+':'
		str = str[j:]
		if str == '':
			break
	return e[:-1][::-1]

def val(num):
	while True:
		a = random.randint(1, num-1)
		b = random.randint(a, num-1)
		if a+b == num:
			return [str(a), str(b)]

def encode(t, k, n, s):
	x, w = RandKey(k), RandKey(n)
	k, n, s = ArrKey(x, k), ArrKey(w, n), ArrKey(x, s)
	i, j = 1, ''
	for h in t:
		if h.isalnum():
			d = [n, 1] if h.isdigit() else [k, 0]
			p = 1 if h.isupper() else 0
			if p == 1:
				h = h.lower()
			for a in d[0]:
				if h in a:
					v = d[0].index(a)+1
					for r in a:
						if h == r:
							if d[1] == 1:
								j+= '1'+str(v)+str(i)
							else:
								j+= str(v)+str(p)+str(i)
							i = 1
							break
						else:
							i+=1
		else:
			for a in s:
				if h in a:
					v = s.index(a)+1
					for r in a:
						if h == r:
							j+= '0'+str(v)+str(i)
							i = 1
							break
						else:
							i+=1
	e, a = '', ''
	for x in x:e+=str(x)
	for x in w:a+=str(x)
	z = val(len(CRC(j)))
	return z[0]+':'+Randomize(j)+':'+Randomize(e[1:]+a[1:])+':'+Randomize(CRC(j))+':'+z[1]

def decode(t, k, n, s):
	e, j = [], ''
	for g in t.split(':'):j+=g
	a, j = j[:1], j[1:]
	b, j = j[-1:], j[:-1]
	r, j = j[len(j)-(int(a)+int(b)):][::-1], j[:len(j)-(int(a)+int(b))]
	b, j = j[len(j)-12:], j[:len(j)-12]
	w, x = [], []
	for g in '0'+b[:4][::-1]:w.append(int(g))
	for g in '0'+b[4:][::-1]:x.append(int(g))
	j = j[::-1]
	if r == CRC(j):pass
	else:
		return '0 - CRC FAIL'
	k, n, s = ArrKey(x, k), ArrKey(w, n), ArrKey(x, s)
	for g in range(len(j)):
		e.append(j[:3])
		j = j[3:]
		if j == '':
			break
	for h in e:
		v = lambda a,b,c:a[int(b)-1][int(c)-1]
		if h[0] == '1':
			i = v(n, h[1], h[2])
		elif h[0] == '0':
			i = v(s, h[1], h[2])
		else:
			p = lambda a,b: a.upper() if b=='1' else a.lower()
			u, r = h[0], h[2]
			i = p(k[int(u)-1][int(r)-1], h[1])
		j+=i
	return j
