import cgi;
import re;
from operator import attrgetter;

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
	
given_string = "I think %s is a perfectly normal thing to do in public."
def sub1(s):
	return given_string%s
	
given_string2 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."
def sub_m(name, nickname):
	return given_string2 %{'name':name,'nickname':nickname};
	
def escape_html(s):
	s = s.replace("&","&amp;");
	s = s.replace(">","&gt;");
	s = s.replace("<","&lt;");
	s = s.replace("\"","&quot;");	
	return s;
	
def rot13(input_str):
	new_char = '';
	output_str = '';
	for char in input_str:
		new_char = getrot13('a','z',char);
		new_char = getrot13('A','Z',new_char);
		output_str += new_char;
	return output_str;
		
def getrot13(start_char, end_char, current_char):
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
		
		
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$");
PASS_RE = re.compile(r"^.{3,20}$");
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$");


def write_to_form(name_content="", email_content="" ,name_message="" ,password_message="" ,verify_message="" ,email_message=""):		
		#self.response.out.write(signupform %{'name_content':name_content, 'name_message':name_message,'email_content':email_content,'password_message':password_message,'verify_message':verify_message,'email_message':email_message});
		print(name_content);
	
		
def valid_username(username):
	return USER_RE.match(username);
	
def valid_password(password):
	return PASS_RE.match(password);
	
def valid_email(email):
	return EMAIL_RE.match(email);
	
	
		
def signup_post():
	name_input = "maniasf";
	password_input = "pass";
	verify_input = "notpass";
	email_input = "asfds";
	name_content="";
	email_content="";
	name_message="";
	password_message="";
	verify_message="";
	email_message="";
	if(not valid_username(name_input)):
		name_message="That's not a valid username";
		name_content=name_input;
	if(not valid_password(password_input)):
		password_message="That's not a valid password";
	if(password_input != verify_input):
		verify_message="Your passwords didn't match";
	if(not valid_email(email_input)):
		email_message="That's not a valid Email Address";
		email_content=email_input;
	write_to_form(name_content=name_content, email_content=email_content, name_message=name_message, password_message=password_message, verify_message=verify_message, email_message=email_message);
from collections import namedtuple

# make a basic Link class
Link = namedtuple('Link', ['id', 'submitter_id', 'submitted_time', 'votes',
                           'title', 'url'])

# list of Links to work with
links = [
    Link(0, 60398, 1334014208.0, 109,
         "C overtakes Java as the No. 1 programming language in the TIOBE index.",
         "http://pixelstech.net/article/index.php?id=1333969280"),
    Link(1, 60254, 1333962645.0, 891,
         "This explains why technical books are all ridiculously thick and overpriced",
         "http://prog21.dadgum.com/65.html"),
    Link(23, 62945, 1333894106.0, 351,
         "Learn Haskell Fast and Hard",
         "http://yannesposito.com/Scratch/en/blog/Haskell-the-Hard-Way/"),
    Link(2, 6084, 1333996166.0, 81,
         "Announcing Yesod 1.0- a robust, developer friendly, high performance web framework for Haskell",
         "http://www.yesodweb.com/blog/2012/04/announcing-yesod-1-0"),
    Link(3, 30305, 1333968061.0, 270,
         "TIL about the Lisp Curse",
         "http://www.winestockwebdesign.com/Essays/Lisp_Curse.html"),
    Link(4, 59008, 1334016506.0, 19,
         "The Downfall of Imperative Programming. Functional Programming and the Multicore Revolution",
         "http://fpcomplete.com/the-downfall-of-imperative-programming/"),
    Link(5, 8712, 1333993676.0, 26,
         "Open Source - Twitter Stock Market Game - ",
         "http://www.twitstreet.com/"),
    Link(6, 48626, 1333975127.0, 63,
         "First look: Qt 5 makes JavaScript a first-class citizen for app development",
         "http://arstechnica.com/business/news/2012/04/an-in-depth-look-at-qt-5-making-javascript-a-first-class-citizen-for-native-cross-platform-developme.ars"),
    Link(7, 30172, 1334017294.0, 5,
         "Benchmark of Dictionary Structures", "http://lh3lh3.users.sourceforge.net/udb.shtml"),
    Link(8, 678, 1334014446.0, 7,
         "If It's Not on Prod, It Doesn't Count: The Value of Frequent Releases",
         "http://bits.shutterstock.com/?p=165"),
    Link(9, 29168, 1334006443.0, 18,
         "Language proposal: dave",
         "http://davelang.github.com/"),
    Link(17, 48626, 1334020271.0, 1,
         "LispNYC and EmacsNYC meetup Tuesday Night: Large Scale Development with Elisp ",
         "http://www.meetup.com/LispNYC/events/47373722/"),
    Link(101, 62443, 1334018620.0, 4,
         "research!rsc: Zip Files All The Way Down",
         "http://research.swtch.com/zip"),
    Link(12, 10262, 1334018169.0, 5,
         "The Tyranny of the Diff",
         "http://michaelfeathers.typepad.com/michael_feathers_blog/2012/04/the-tyranny-of-the-diff.html"),
    Link(13, 20831, 1333996529.0, 14,
         "Understanding NIO.2 File Channels in Java 7",
         "http://java.dzone.com/articles/understanding-nio2-file"),
    Link(15, 62443, 1333900877.0, 1244,
         "Why vector icons don't work",
         "http://www.pushing-pixels.org/2011/11/04/about-those-vector-icons.html"),
    Link(14, 30650, 1334013659.0, 3,
         "Python - Getting Data Into Graphite - Code Examples",
         "http://coreygoldberg.blogspot.com/2012/04/python-getting-data-into-graphite-code.html"),
    Link(16, 15330, 1333985877.0, 9,
         "Mozilla: The Web as the Platform and The Kilimanjaro Event",
         "https://groups.google.com/forum/?fromgroups#!topic/mozilla.dev.planning/Y9v46wFeejA"),
    Link(18, 62443, 1333939389.0, 104,
         "github is making me feel stupid(er)",
         "http://www.serpentine.com/blog/2012/04/08/github-is-making-me-feel-stupider/"),
    Link(19, 6937, 1333949857.0, 39,
         "BitC Retrospective: The Issues with Type Classes",
         "http://www.bitc-lang.org/pipermail/bitc-dev/2012-April/003315.html"),
    Link(20, 51067, 1333974585.0, 14,
         "Object Oriented C: Class-like Structures",
         "http://cecilsunkure.blogspot.com/2012/04/object-oriented-c-class-like-structures.html"),
    Link(10, 23944, 1333943632.0, 188,
         "The LOVE game framework version 0.8.0 has been released - with GLSL shader support!",
         "https://love2d.org/forums/viewtopic.php?f=3&amp;t=8750"),
    Link(22, 39191, 1334005674.0, 11,
         "An open letter to language designers: Please kill your sacred cows. (megarant)",
         "http://joshondesign.com/2012/03/09/open-letter-language-designers"),
    Link(21, 3777, 1333996565.0, 2,
         "Developers guide to Garage48 hackatron",
         "http://martingryner.com/developers-guide-to-garage48-hackatron/"),
    Link(24, 48626, 1333934004.0, 17,
         "An R programmer looks at Julia",
         "http://www.r-bloggers.com/an-r-programmer-looks-at-julia/")]


# links is a list of Link objects. Links have a handful of properties. For
# example, a Link's number of votes can be accessed by link.votes if "link" is a
# Link.

# QUIZ - implement the function link_by_id() that takes a link's ID and returns
# the link itself
def link_by_id(link_id):
   return link_index.get(link_id);
			
def build_link_index():
	link_dict = dict();
	for link in links:
		link_dict[link.id] = link;
	return link_dict;
		
def add_new_link(link):
	links.append(link);
	link_index[link.id] = link;

link_index = build_link_index();
new_link = Link(1234, 48626, 1333934004.0, 17,
         "Married to Java but Love python",
         "http://twitter.com/mani_samva");
add_new_link(new_link);
print link_by_id(1234);







