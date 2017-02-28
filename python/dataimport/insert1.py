#!/usr/bin/python
#-*-coding:utf-8-*-

import copy
from models import MemMember,MemCard,RlCardtypeCard
from sqlalchemy import Table, Column, Integer, String, Date, Float, create_engine 
from sqlalchemy import func,and_
from sqlalchemy.orm import sessionmaker,make_transient
from sqlalchemy.orm.exc import NoResultFound,MultipleResultsFound
from sqlalchemy.ext.declarative import declarative_base

old_clubid='-7fod2i4nk3a4k083edv8l3ecangr2dcb'

def queryMem(session):
    print '====in queryMem'
    query = session.query(MemMember)
    mList=query.filter(MemMember.club_id==old_clubid).all()
    return mList


def addMem(mem,session):
    print '====in addMem'
    mem.club_id='ssss'
    mem.id=None
    
    session.add(mem)
    session.commit()
    return mem.id

def queryMemCard(session,oldmemid):
    print '====in queryMemCard=='
    query = session.query(MemCard)
    print 'oldmemid==',oldmemid

    try:
        mcard=query.filter(and_(MemCard.club_id==old_clubid,MemCard.member_id==oldmemid)).one()    
    except MultipleResultsFound, e:
        print e
        # Deal with it
        return None
    except NoResultFound, e:
        print '-------in  no resuultfoune'
        print e
        # Deal with that as well
        return None
    return mcard


def addMemCard(mem_card,session,newmemid):
    print '====in addMem  card==='
    mem_card.club_id='ssss'
    mem_card.id=None
    mem_card.member_id=newmemid

    session.add(mem_card)
    session.commit()
    return mem_card.id

def addRlCard(rlCard,session):
    print '====in rl  card==='
    rlCard.id=None
    session.add(rlCard)
    session.commit()
    return rlCard.id



engine = create_engine('mysql+mysqldb://root:yundonggo@127.0.0.1:3306/data_import?charset=utf8')
DBSession = sessionmaker(bind=engine)
session = DBSession()

#coding:utf-8
from collections import OrderedDict  
  
from pyexcel_xls import get_data  
from pyexcel_xls import save_data
from models import MemMember,RlCardtypeCard,MemCard
import insert

list = [];
  
def read_xls_file(session):  
    xls_data = get_data(r"/root/python/test.xls") 
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
                if rowi==15
                    rlCard.activate_day=row[15]
                 if rowi==19
                    rlCard.salesman_name=row[19]
              #  if rowi==12:
               #     rlCard.card_left_num=row[12]
                if rowi==10:
                    rlCard.card_type_Id=row[10]
            id=addMem(mem,session);
            mem.club_id='15hmj5l8oul8gunp6rkjrtrl3qsdg2q5'
            memCard.member_id=id
            memCard.state=u'NOMAL'
            addMemCard(memCard,session,id)
            memCard.club_id=u'15hmj5l8oul8gunp6rkjrtrl3qsdg2q5'
            rlCard.activate_day=90
            rlCard.club_id=u'15hmj5l8oul8gunp6rkjrtrl3qsdg2q5'
            addRlCard(rlCard,session)


read_xls_file(session)
    
