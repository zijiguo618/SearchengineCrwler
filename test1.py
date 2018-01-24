# -*- coding: utf-8 -*-
# import test_recur
import time
import datetime
import test_DB
# import DBkeywords
import re
# import getbaidu
# import currentdate
# import getbing
# import getsearch
# import getaol
# import getask
# import getlycos
# import getgoogle
# import loadinglisenter
# import DBkeywords
# test_recur.main()
# print time.time()
# date = currentdate.getdate()
# # suspect(engine,engine_id,ID,site,score,date):
## def bing(ID,tittle,site,abstract,html,cdate,ac):
# ID =DBkeywords.findkeywordID('funding')
# tittle = "Funding available - Department of Communities, Child"
# site = "https://www.communities.qld.gov.au/gateway/funding-grants/funding-available"
# abstract = "Funding available from the department. ... The department is currently inviting applications for the following funding programs"
# html ="""Funding available - Department of Communities, Child Safety and Disability Services (Queensland Government) <iframe style=""display:none;visibility:hidden"" width="0" height="0" src=""//www.googletagmanager.com/ns.html?id=GTM-TCQL3Q""></iframe>Skip links and keyboard navigationSkip to contentSkip to navigationSkip to footerUse tab and cursor keys to move around the page (more information)Department of Communities, Child Safety and Disability ServicesSite mapContact usHelpSearch Department of Communities, Child Safety and Disability Services HomeCommunityChild SafetyDisabilityMulticulturalOur servicesChild Safety ServicesCommunity ServicesDisability ServicesWomen's ServicesMulticultural Affairs QueenslandReform and renewalChild and familyDisability servicesDomestic and family violenceSocial ServicesFunding and grantsDepartmental sponsorshipFunding availableLegislative safeguards for fundingHuman Services Quality FrameworkStreamlined agreementsInvestment specificationsOutcomes Co-designNon-Government organisation access to interpreting servicesOutput funding and reportingOnline Acquittal Support Information System (OASIS)CareersWhat we offerCareer choices"""
# new_string = re.sub('[^a-zA-Z0-9\n\.]', ' ', html)
# ac ="AU"
# common = '"'
# test_DB.bing(1284,'test','test','test','test',date,'ac')
# suspect(engine,engine_id,ID,site,score,cdate,message,tittle,abstract):
# def bing(ID,tittle,site,abstract,html,cdate,ac):
# trust ='http://baike.baidu.com'
url ="www.helloworld.com"
if(url.startswith("https://")):
	print url[8:len(url)]
elif(url.startswith("http://")):
	print url[7:len(url)]
else: 
	print url


# url = 'http://baike.baidu.com/ncasuhdals'
# if trust in url:
# 	print "ok"

# li=DBkeywords.loadsunsearchedkeywords('bing')

# for l in li:
# 	print l[0]