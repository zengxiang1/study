#coding:utf-8
from collections import OrderedDict  
  
from pyexcel_xls import get_data  
from pyexcel_xls import save_data
from models import MemMember,RlCardtypeCard,MemCard
import insert

list = [];
  
def read_xls_file():  
    xls_data = get_data(r"E:/test.xls") 
    for sheet_n in xls_data.keys():
        for row in xls_data[sheet_n]:
        	mem = MemMember()
        	memCard = MemCard()
        	rlCard = RlCardtypeCard()
        	for rowi in range(len(row)):
        		#会员
        		if rowi==0:
        			mem.member_name=row[0]+row[1]
        		if rowi==2:
        			mem.sex=row[2]
        		if rowi==3:
        			mem.phone=row[3]
        		if rowi==4:
        			mem.card_id=row[4]
        		if rowi==5:
        			mem.birthday=row[5]
        		if rowi==7:
        			mem.remarks=row[7]
        		if rowi==6:
        			mem.mail=row[6]
        		if rowi==18:
        			mem.point=row[18]
        		#会员卡
        		if rowi==8:
        			memCard.mc_code=row[8]
        			rlCard.mc_code=row[8]
        		if rowi==13:
        			memCard.create_day=row[13]
        			rlCard.create_day=row[13]
        		if rowi==11:
        			rlCard.card_left_balance=row[11]
        		if rowi==12:
        			rlCard.card_left_num=row[12]
        		if rowi==10:
        			rlCard.card_type=row[10]
       		id=addMem(mem);
       		mem.club_id='15hmj5l8oul8gunp6rkjrtrl3qsdg2q5'
       		memCard.member_id=id
       		memCard.state=u'NOMAL'
       		addMemCard(memCard)
       		memCard.club_id=u'15hmj5l8oul8gunp6rkjrtrl3qsdg2q5'
       		rlCard.activate_day=90
       		rlCard.club_id=u'15hmj5l8oul8gunp6rkjrtrl3qsdg2q5'
       		addRlCard(rlCard)


if __name__ == '__main__':
	read_xls_file()  
	for mem in list:
		print mem.member_name
    