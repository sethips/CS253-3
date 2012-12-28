#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import re

form="""
<form method="post">
	What's your birthday?
	<br>
	<lable>
	Month
	<input type="text" name="month">
	</lable>
	<lable>
	Day
	<input type="text" name="day">
	</lable>
	<lable>
	Year
	<input type="text" name="year">
	</lable>
	<div style="color: red">%(error)s</div>
	<br>
	<input type="submit">
</form>
"""
months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']


rot13form="""
<html>
	<form action="/rot13" method="post">
		<textarea name="text">%(content)s</textarea>
		<br>
		<br>
		<input type="submit">
	</form>
</html>
"""

signupform="""
<html>
	<form action="/signup" method="post">
		Name <input type="input" name="username" value="%(name_content)s"> %(name_message)s <br>
		Password <input type="password" name="password"> %(password_message)s <br>
		Confirm Password <input type="password" name="verify"> %(verify_message)s <br>
		email address (optional) <input type="input" name="email" value="%(email_content)s"> %(email_message)s <br><br>
		<input type="submit">
	</form>
</html>
"""


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$");
PASS_RE = re.compile(r"^.{3,20}$");
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$");

def valid_month(month):
	if(month.capitalize() in months):
		return month.capitalize();
	
def valid_day(day):
	try:
		day = int(day);
		if(day>0 and day<32):
			return day;
	except:
		return;
		
def valid_year(year):
	if(year.isdigit()):
		year = int(year);
		if(year>=1900 and year<=2020):
			return year;



		
class MainHandler(webapp2.RequestHandler):
	def write_form(self, error=""):
		self.response.out.write(form %{'error':error});	
	def get(self):
		self.write_form();
	def post(self):
		validmonth = valid_month(self.request.get("month"));
		validday = valid_day(self.request.get("day"));
		validyear = valid_year(self.request.get("year"));
		if(validmonth and validday and validyear):
			self.response.out.write("Thanks");
		else:
			self.write_form("Invalid Data. Please re enter");

			
class Rot13Handler(webapp2.RequestHandler):	
	def write_form(self, content=""):
		content = cgi.escape(content,quote=True);
		self.response.out.write(rot13form %{'content':content});
		
		
	def rot13(self, input_str):
		new_char = '';
		output_str = '';
		for char in input_str:
			new_char = self.getrot13('a','z',char);
			new_char = self.getrot13('A','Z',new_char);
			output_str += new_char;
		return output_str;
			
	def getrot13(self, start_char, end_char, current_char):
		start_ascii = ord(start_char);	
		end_ascii = ord(end_char);	
		current_ascii = ord(current_char);	
		if((current_ascii < start_ascii) or (current_ascii > end_ascii)):		
			return current_char;
		else:
			output_ascii = current_ascii + 13;
			if(output_ascii > end_ascii):
				output_ascii = start_ascii + (output_ascii - end_ascii) - 1;
			return chr(output_ascii);
			
	def get(self):
		self.write_form();		
		
	def post(self):
		input_content = self.request.get("text");
		output_content = self.rot13(input_content);
		self.write_form(output_content);
		
	
class SignupHandler(webapp2.RequestHandler):
	def write_form(self, name_content="", email_content="" ,name_message="" ,password_message="" ,verify_message="" ,email_message=""):				
		self.response.out.write(signupform %{'name_content':name_content, 'name_message':name_message,'email_content':email_content,'password_message':password_message,'verify_message':verify_message,'email_message':email_message});
	
		
	def valid_username(self,username):
		return USER_RE.match(username);
		
	def valid_password(self,password):
		return PASS_RE.match(password);
		
	def valid_email(self,email):
		return EMAIL_RE.match(email);
		
	def get(self):
		self.write_form();		
		
	def post(self):
		name_input = self.request.get("username");
		password_input = self.request.get("password");
		verify_input = self.request.get("verify");
		email_input = self.request.get("email");
		name_content=name_input;
		email_content=email_input;
		name_message="";
		password_message="";
		verify_message="";
		email_message="";
		success = True;
		if(not self.valid_username(name_input)):
			name_message="That's not a valid username";		
			success = False;
		if(not self.valid_password(password_input)):
			password_message="That's not a valid password";
			success = False;
		if(password_input != verify_input):
			verify_message="Your passwords didn't match";
			success = False;
		if((email_input != "") and (not self.valid_email(email_input))):
			email_message="That's not a valid Email Address";			
			success = False;
		if(success):
			self.redirect("/welcome?username=%(username)s" %{'username':name_input});
		else:
			self.write_form(name_content=name_content, email_content=email_content, name_message=name_message, password_message=password_message, verify_message=verify_message, email_message=email_message);
	
	
class WelcomeHandler(webapp2.RequestHandler):
	def write_form(self, name=""):
		self.response.out.write("Welcome, %(name)s!" %{'name':name});	
	def get(self):
		self.write_form(self.request.get("username"));
		
		
app = webapp2.WSGIApplication([('/', MainHandler), ('/rot13', Rot13Handler), ('/signup', SignupHandler), ('/welcome', WelcomeHandler)],
                              debug=True)
							  
							  
							  
