import os
from PIL import Image
import imagehash
import urllib.request
import requests
import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import InvalidElementStateException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from datetime import datetime






print('E-Bidding Solution (Version : 0.91.01) Automatic Captcha Filler (Without Login)')
print('---------------------------------')
print('---------------------------------')

#u=input("Enter Username :  ")
#p=input("Enter Password :  ")
print("\n")

state_flag=0


print('Please Select Pack Type : ')
print('1. For Bulk Enter a \n2. For Bag Enter b ')
tempp=input('Enter Your Choice  : ')
if tempp=='a' or tempp=='1':
	pack_type_v='Bulk'
	print('Bulk Pack Type Selected.')
	
elif tempp=='b' or tempp=='2':
	pack_type_v='Bag'
	print('Bag Pack Type Selected.')

	
else:
	print('Sorry, Invalid Input  :( ')
	exit()

state_name=input('Want To Select UP (y/n) ?  ')

if state_name=='y' or  state_name=='Y':
	state_flag=1
	print("Destination State : UTTAR PRADESH Seleted. ")

	
secondary_flag=0

secondary=input('Want To Use as Secondary bot (y/n) ? ')
if secondary=='y' or  secondary=='Y':
	secondary_flag=1
	print("Secondary Mode Seleted. ")
	





CAPTCHA = {
	"f1fb050000e3ffff": "nwp3n",
	"efbfb1c11188c378": "253nb",
	"ff86161f1b3040df": "26156",
	"7f7d81850103fffe": "2mnch",
	"ff1d85818107ffff": "3fby7",
	"ffa71011189edcff": "4D7YS",
	"fdf080808400d1ff": "4NV3A",
	"1f6fe10001e3fffe": "5ykwc",
	"fffc9ea08290bfff": "6ne3",
	"00667e7e7e5e0200": "7PhLQ",
	"feb9818101c1bfff": "7wh8r",
	"ff0d01c9cd01efff": "7YB2U",
	"ffff81818181ffff": "83tsU",
	"f931858101871bbb": "9M4BP",
	"ffff8d81818187f7": "9w5ya6",
	"00203c7e7e3c0800": "=bg=",
	"00107eeefef70200": "aNG4bg",
	"fbfb81818181dbff": "arch",
	"ddc0d804170f87ff": "AWSKH",
	"fefdd1070001bdfe": "b6Y97j",
	"bd816160460081ff": "CUU5",
	"ff833c182d00ffff": "d573r",
	"ffbe01000000feff": "dcen4",
	"ffdf80000303ffff": "dister",
	"00f87e3efe400000": "DXHm",
	"ffffcb010181f1f7": "e5hb",
	"00327ecefe7e0000": "eG7ak",
	"be8913018b81ff0f": "f8233",
	"ffffa7818181ffff": "fa636d",
	"ff7f0201410184ff": "fdamc",
	"007f000183c1e7ff": "fegpc",
	"ffffe380888081c1": "fish",
	"00767e7e7c5c0000": "FMr7",
	"0084fefefe7e1800": "frmgZW",
	"007e7e7e7a4e0000": "fTE9",
	"0044febefe7e0000": "GhKdW",
	"003afefefecec000": "gXFLd",
	"00387e7e7e7a0200": "H6Wg",
	"f7f13000151fdfff": "HE3X6",
	"005a6e7e7e7e0000": "hh7ZqY",
	"feece8999880b1fb": "ic8",
	"00107efefe7e0200": "kHKNg",
	"0038fe7e6e380000": "MZ9N",
	"ff93018381e5e7ff": "neynt",
	"0fc000a30107ffff": "rcke4",
	"00f67efeea6a0000": "RFV9",
	"0000fefefefe0000": "RthDY",
	"f7f39181818381ff": "rule",
	"ed8c90dbd38089ff": "SKARD",
	"ff9d05010000aaff": "Stack",
	"00eafe7e7e7a0000": "TEXR4Q",
	"1d1f9b9191e383df": "TK58P",
	"00003a7efefe1400": "u@JbgE",
	"ffff810181cfdfff": "v4xBg",
	"ffe981818100efff": "Wjk5L",
	"004e7e7e7f180038": "Xud9K",
	"ffdd010101e1eefe": "y4gp6",
	"fff00f0f0ff0f1ff": "14",
	"c181818f898780ff": "59CTR",
	"007c7efe7e7c0000": "699EN",
	"bd80c1808480a1ff": "6AR8R",
	"f7850101010bfbff": "865301",
	"7f3780048521ffff": "8n8cg",
	"ffcdc9c183a3f3ff": "a861",
	"ff40031918036dff": "B4T9S",
	"0000ffffff000000": "ChanceNaLo",
	"bffc81004501ffff": "crmce",
	"00243676762e00ff": "dk3g",
	"fff3f1a1058f9fdf": "dsjcbka",
	"4b443498005b50ff": "DT6JX",
	"fe58d0908204d4ff": "DWXM5",
	"ffb3818181c5ffff": "e3TJ6Jdp",
	"00787eff7e5e0000": "EMJkb",
	"00787e7e7e6e0200": "EYLq",
	"ff7f00000083ffff": "FoxLearn",
	"00f0b6eefed20000": "G4Q=m",
	"003076fefe764000": "gWek",
	"cf878381818187ef": "has",
	"00b8fefe7e7e0000": "hEDra",
	"00e10001011dffff": "herrd",
	"00007e7e7e460000": "hNM6g",
	"f7305456574440ff": "ibE2",
	"ffece080838fff3f": "just",
	"000e1f3fcfc08080": "jw62k",
	"0070fcfc5c7c0800": "K9gt",
	"ffefc10f2080c1f7": "KiLL",
	"0060fefe7e5e0800": "KNghk",
	"bf85832331a121ff": "MCSXH",
	"ffff00000004ffff": "mmbhb",
	"ff858381838387c7": "need",
	"fffff9310081c7ff": "overlooks",
	"00feefefff460000": "QTTDb",
	"ffef000000e7ffff": "ry2n4",
	"00e27e7e7e320000": "TLu=V",
	"00dafe6e7e7a0000": "TWGPnZ",
	"fffde10101013fff": "usual",
	"ffe7a5040009d9f7": "V6T9JBCDS",
	"0060ffffff520000": "VFh@4@",
	"007efefefe480000": "WVHVR",
	"ffdfc18101013dff": "xDHYN",
	"004e7e7e7e7e3000": "XgDD",
	"fffd01000101fffe": "xhkn4",
	"ff370303032337ff": "XkCWpBTS",
	"9b8085808480b9ff": "XKWDN",
	"ded8a1000153ffff": "y5n87",
	"ff818383c3c3ffff": "YPFF",
	"ffef6001a93bffff": "YPIF",
	"ffe1010001f1ffff": "yyh22",
	"00407e7e7efe0000": "ZrLU",
	"ef6f10000001fdff": "ex5mp",
	"ff7f070000c0ffff": "ydn63",
"ff3b8080002bffff": "2mw6m",
"0fb480830028ffff": "2nnc7",
"009bcf81c128ffff": "2nw6c",
"7e8983018921fcff": "3763y",
"fef98100018ddfff": "3gk72",
"7efc81879300cf3f": "3kr47",
"ffa583018481fbfe": "3p8b5",
"fffd85808003efff": "3ygb3",
"ffa100000b83ffff": "6b25f",
"3f9f8150000f7fff": "72cme",
"9f98e0810173ffff": "77cch",
"7f9f27818081ffff": "7rckd",
"7c0185012101fffe": "852g8",
"deb880818125fdff": "87pbg",
"bfbf8f011100feff": "8k2yk",
"1fb3810101b9ffff": "8nydx",
"fff783800081cf3f": "c46kr",
"3fd7cf0101a9dfc0": "c4x7w",
"7fff81010181ffff": "cghp4",
"80f8af070183ffff": "ckm27",
"fdfd8301040beffc": "cmrr5",
"ffffaf8000afe3fe": "d6b64",
"ffb905010861cf7f": "f4y53",
"00ffe2030901ffff": "fd67y",
"00ef08018181ffff": "fg8xm",
"ffff25010100ffff": "fwme4",
"feffb301c121d91f": "fyxmp",
"07dfbb100001ff7f": "g55gd",
"3fdf81808085bfff": "g8peb",
"00ff8b838393b780": "gcngc",
"1fe7c0010101bfbf": "gxenp",
"2083b9000501ffff": "hkx3y",
"ffff1d000080ffff": "khmcb",
"7fbf830101fdce00": "kmcb2",
"ffff3d810090ffff": "m66p4",
"efdf49010101efff": "mdpwb",
"ffff01030001cf9f": "mgkec",
"01fcef212901e3f8": "n3fp3",
"ffc4c00101017fff": "n44yd",
"ffffe1010901fffe": "nn83h",
"07c100080587ffff": "nnx77",
"f8f781010100f7ff": "nydgx",
"fedde12181017f7f": "p28h6",
"fef1ff0180003fff": "pn423",
"87fbac018020ffff": "pykeh",
"7cb98101819cffff": "rg4hh",
"ffff00010580e3ff": "w4yc6",
"07d98f2131a1efff": "w7pxm",
"feff91010181ffff": "wxrec",
"ffe1c08280a3df3f": "xr857",
"bff7218080b9ffff": "xy783"
}













depot_input=input('Enter The Depot Name : ')



#url="http://ebidding.velvish.com/index.php?u={}&p={}".format(u,p)
url='http://ebidding.velvish.com/index.php?u=sscm&p=San930!@'

user='2901448'
password='@2091998'


options=Options()
options.add_experimental_option("excludeSwitches", ['enable-automation'])
options.add_argument('start-maximized')


driver=webdriver.Chrome(options=options)
driver.get(url)

#____________Login Start __________________________

login_form_username =WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "USERNAME_FIELD-inner")))
login_form_password=driver.find_element_by_id('PASSWORD_FIELD-inner')
login_button=driver.find_element_by_xpath("//span[@class='sapMBtnContent sapMLabelBold sapUiSraDisplayBeforeLogin']")
login_form_username.send_keys(user)
login_form_password.send_keys(password) 
login_button.click()
print('Login Successfully')

#____________Login End ____________________________



#____________Clicking on E bidding ____________________________


try:
	e_bidding = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@id='__content6-icon-image']")))
except TimeoutException:
	driver.refresh()
	e_bidding = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//span[@id='__content6-icon-image']")))


e_bidding.click()



#___________Switching the Tab_____________________
p=driver.current_window_handle
chwd=driver.window_handles

for w in chwd:
	#switch focus to child window
	if(w!=p):
		driver.switch_to.window(w)
		break



#_____________filling the form start ______________________

def ShowSearch():
	try:
		show_search = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Show Search')]")))
		show_search.click()
	except TimeoutException:
		driver.refresh()
		show_search = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[@id='__button0-inner']")))
		show_search.click()
	except NoSuchElementException:
		show_search = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Show Search')]")))
		show_search.click()
	except  ElementClickInterceptedException:
		time.sleep(5)
		show_search.click()
	except Exception as search_err:
		print(search_err)
		show_search = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[@id='__button0-inner']")))
		show_search.click()


def change_depo(depot_input,pack_type_v):
	
	depot_input_box=driver.find_element_by_xpath("//input[@id='__xmlview0--idUtclVCDepot-inner']")
	
	depot_input_box.send_keys(depot_input.upper())
	
	pack_type=driver.find_element_by_xpath("//input[@id='__xmlview0--idUtclVCPackType-inner']")
	pack_type.send_keys(pack_type_v)



	

	

def filling_form(depot_input,pack_type_v):
	arrow_after_search=driver.find_element_by_xpath("//span[@id='__xmlview0--ididUtclVCShipFromPlant-arrow']")
	arrow_after_search.click()


	first_avaible_search=driver.find_element_by_xpath("//span[@class='sapMSelectListCell sapMSelectListFirstCell']")
	first_avaible_search.click()
	
	change_depo(depot_input,pack_type_v)

	#changing State

	if(state_flag==1):
		driver.find_element_by_id("__xmlview0--idUtclVCState-arrow").click()
		WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "__item68-selectMulti-CbBg"))).click()
	
	search=driver.find_element_by_xpath("//bdi[@id='__button3-BDI-content']")       
	search.click()

	yes_search=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Yes')]")))
	yes_search.click()

ShowSearch()
print('clicked on show search')

filling_form(depot_input,pack_type_v)
print('Filled The form')




#####################################################################################################################

#first check whether exist or not.

####################################################################################################################
bidding_timer_ended=0
search=driver.find_element_by_xpath("//bdi[@id='__button3-BDI-content']")

			
			
def save_button():
	save_button=WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, "//bdi[@id='__xmlview0--idUtclsaveTxt-BDI-content']")))
	save_button.click()
	print('Clicked On save')                        



def clicking(START,END):
	for i in range(START,END):
		if len(driver.find_element_by_id("__text47-__xmlview0--idUtclVCVendorAssignmentTable-{}".format(i)).text)==0:
			try:
				bid_ip=driver.find_element_by_id("__xmlview0--idBidAmount-__xmlview0--idUtclVCVendorAssignmentTable-{}-inner".format(i)).send_keys("")
			except Exception as cld:
				print(cld)
				time.sleep(0.5)
				bid_ip=driver.find_element_by_id("__xmlview0--idBidAmount-__xmlview0--idUtclVCVendorAssignmentTable-{}-inner".format(i)).send_keys("")

'''

def searching_Again():
	try:                                
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//bdi[.='Search']"))).click()
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//bdi[.='Yes']"))).click()
	except ElementClickInterceptedException:
		return
	except Exception as e:
		print(e)
		return
'''
	

def searching_Again():
	try:                                
		search=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//bdi[.='Search']")))
		search.click()
		#yes_search=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//bdi[.='Yes']")))
		yes_search=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//bdi[.='Yes']")))
		yes_search.click()
		time.sleep(0.5)
		return
	except ElementClickInterceptedException:
		print('ElementClickInterceptedException Founded')
		time.sleep(0.5)
		return
	except Exception as e:
		print(e)
		time.sleep(0.5)
		return



wcn=0
################################################################################################################################################################
def Captcha_filler():
	try:
		y_search=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//bdi[.='Yes']")))

		captcha=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "CaptchaImage")))
		print("CaptchaImage Founded")
		captcha_img_path=captcha.get_attribute('src')
		print("CaptchaImage SCR Founded")
		saving_path="img/temp.png"
		urllib.request.urlretrieve(captcha_img_path,saving_path)
		
		key=str(imagehash.average_hash(Image.open(saving_path)))
		try:
			captcha_in_loc=''' var xpath_for_cin = "//input[@placeholder='Enter Captcha']";
							var qff = document.evaluate(xpath_for_cin, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
							qff.value="%s";
							qff.focus();'''%(CAPTCHA[key])
			driver.execute_script(captcha_in_loc)
			print("Captcha Filled_________")
			y_search.click()
			ok_inend=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//bdi[.='OK']")))
			ok_inend.click()
			return
		except KeyError:
			global wcn
			wcn=wcn+1
			print("New Captcha Founded")
			os.rename(r'img/{}'.format('temp.png'),r'img/WrongCaptcha_{}_.png'.format(wcn))
			in_box=WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Captcha']")))
			in_box.send_keys("X")
			ActionChains(driver).click(in_box).perform()
			while True:
				if keyboard.is_pressed('enter'):
					y_search.click()
					break
		'''except Exception as dde:
			print("Error at below keyerror",dde)
			return'''
	except Exception as cerf:
		print(cerf)
		return 
			
#############################################################################################################################################################			
def Save_Seach():
	END,START,TEND=0,0,-1
	if(secondary_flag==1):
		x_yz=input("Press Enter to start the Bot ")
	while True:
		
		END=len(driver.find_elements_by_class_name("sapMRbBInn"))
		if(END!=0):
			if(TEND!=-1):
				START=TEND
			if(TEND!=END):
				print("bid ready to fill", datetime.now())
				   
				bid_clickable=-1
				while bid_clickable==-1:
					try:
						temp_b=driver.find_element_by_id("__xmlview0--idBidAmount-__xmlview0--idUtclVCVendorAssignmentTable-{}-inner".format(START))
						temp_b.send_keys("")
						bid_clickable=1
					except Exception as bnce:
						print("bid is not clickable",bnce)
						time.sleep(0.5)

				fill_js='''
				for(let i=%d;i<%d;i++)
					{ 
						if(document.getElementById(`__xmlview0--idBidAmount-__xmlview0--idUtclVCVendorAssignmentTable-${i}-inner`).value=='0')
						{
							document.getElementById(`__xmlview0--idBidAmount-__xmlview0--idUtclVCVendorAssignmentTable-${i}-inner`).focus();
							document.getElementById(`__xmlview0--idBidAmount-__xmlview0--idUtclVCVendorAssignmentTable-${i}-inner`).value =
							document.getElementById(`__text45-__xmlview0--idUtclVCVendorAssignmentTable-${i}`).textContent;
							document.getElementById(`__xmlview0--idBidAmount-__xmlview0--idUtclVCVendorAssignmentTable-${i}-inner`).focus();
						}
					}
					'''%(START,END)

				print("bid filled",datetime.now())


				save_clickable=-1
				while save_clickable==-1:
									try:
										driver.execute_script(fill_js)
										bttt=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, '__xmlview0--idUtclsaveTxt-BDI-content')))
										bttt.click()
										print("Clicked On Save",datetime.now())
										save_clickable=0
									except Exception as ekk:
										print("Exception when clicking the save",ekk)
										time.sleep(0.5)
				Captcha_filler()
				TEND=END
				searching_Again()
			else:
				searching_Again()
		else:
			searching_Again()
###############################################################################################################################################################
				
Save_Seach()
