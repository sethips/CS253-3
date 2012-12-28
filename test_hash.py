import hashlib
import hmac
import random
import string

SECRET = 'imsosecret'
def hash_str(s):
    #return hashlib.md5(s).hexdigest()
	return hmac.new(SECRET,s).hexdigest()


def make_secure_val(s):
	return "%s|%s" %(s,hash_str(s))


def check_secure_val(h):
	val = h.split('|')[0]
	if(h == make_secure_val(val)):
		return val

def make_salt():	
	return ''.join(random.choice(string.letters) for x in range(5))
	
#input_str = make_secure_val("1")
#input_str = "hello,dummyhashedvalueofhello"
#print input_str
#print check_secure_val(input_str)
def make_pw_hash(name, pw, salt= None):
	if not salt:
		salt = make_salt()
	return hashlib.sha256(name+pw+salt).hexdigest()+','+salt
	
def valid_pw(name, pw, h):
	salt = h.split(',')[1]
	return (h == make_pw_hash(name,pw,salt))
	
h = make_pw_hash("mani","pass")
print h
print valid_pw("mani","pass",h)



