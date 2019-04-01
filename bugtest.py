from bs4 import BeautifulSoup
import html5lib
import urllib.request



def get_HTML(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    return html
def get_the_tiezi(url):
		response = urllib.request.urlopen(url)
		HTML = response.read()
		soup = BeautifulSoup(HTML, "html.parser") # the html input and the parser name
		getTitle(soup)
		element = soup.findAll("div",attrs={'class':'l_post l_post_bright j_l_post clearfix'}) # the text that we are looking for
	#	print(element)
		for tag in element:
			 print("--------------------------------------------------------------------")
			 getAuthor(tag)
			 getContext(tag)
			 getLevel(tag)
			 getDate(tag)
			 #print("\n\n\n")
def getTitle(soup):
	title =soup.find( "h3",attrs={'class':'core_title_txt pull-left text-overflow'}) 
	print("\n",title.text)
def getAuthor(tag):
	 subauthor =tag.find( "a",attrs={'class':'p_author_name j_user_card'}) 
	 print("\n",subauthor.text)
def getContext(tag):
	 subcontext =tag.find( "div",attrs={'class':'d_post_content j_d_post_content'}) 
	 print("\n",subcontext.text)
def getLevel(tag):
	 sublevel =tag.findAll( "span",attrs={'class':'tail-info'}) 
	 print("\n",sublevel[0].text)
def getDate(tag):
	 subtime =tag.findAll( "span",attrs={'class':'tail-info'}) 
	 print("\n",subtime[1].text)



url="https://tieba.baidu.com/p/4963823261"

get_the_tiezi(url)


