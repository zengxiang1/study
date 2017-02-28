# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Enum, Float, Integer, String, Table, text
from sqlalchemy.dialects.mysql.types import MEDIUMBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class AccountBill(Base):
    __tablename__ = 'account_bill'

    id = Column(Integer, primary_key=True)
    bill_date = Column(DateTime)
    pay_code = Column(String(255, u'utf8mb4_bin'))
    number = Column(Integer)
    bill_money = Column(Float(11, True))
    service_money = Column(Float(11, True))
    total_money = Column(Float(11, True))
    status = Column(Enum(u'APPLY', u'PAY', u'CONSUME'))
    apply_date = Column(DateTime)
    pay_date = Column(DateTime)
    deal_no = Column(String(64, u'utf8mb4_bin'))
    operate_id = Column(Integer)
    operate_name = Column(String(64, u'utf8mb4_bin'))
    club_id = Column(String(125, u'utf8mb4_bin'))
    create_by = Column(DateTime)
    update_by = Column(DateTime)
    apply_id = Column(Integer)
    apply_name = Column(String(255, u'utf8mb4_bin'))


class ActivityCalendar(Base):
    __tablename__ = 'activity_calendar'

    id = Column(Integer, primary_key=True)
    name = Column(String(255, u'utf8mb4_bin'))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    court_type_id = Column(Integer)
    court_id = Column(String(255, u'utf8mb4_bin'))
    remarks = Column(String(255, u'utf8mb4_bin'))
    club_id = Column(String(255, u'utf8mb4_bin'))


class BigtvBasicset(Base):
    __tablename__ = 'bigtv_basicset'

    id = Column(Integer, primary_key=True)
    present_number = Column(Integer)
    indoor_temperature = Column(String(16, u'utf8mb4_bin'))
    water_temperature = Column(String(16, u'utf8mb4_bin'))
    ph_value = Column(String(16, u'utf8mb4_bin'))
    bulletin = Column(MEDIUMBLOB)
    logo_url = Column(String(255, u'utf8mb4_bin'))
    club_id = Column(String(125, u'utf8mb4_bin'))


class BigtvInformation(Base):
    __tablename__ = 'bigtv_information'

    id = Column(Integer, primary_key=True)
    start_time = Column(String(8, u'utf8mb4_bin'))
    end_time = Column(String(8, u'utf8mb4_bin'))
    category = Column(Enum(u'TICKET', u'VIPREMIED', u'VIP', u'TRAINED'))
    club_id = Column(String(125, u'utf8mb4_bin'))


class BigtvInformationDeail(Base):
    __tablename__ = 'bigtv_information_deail'

    id = Column(Integer, primary_key=True)
    information_id = Column(Integer)
    title = Column(String(255, u'utf8mb4_bin'))
    subtitle = Column(String(255, u'utf8mb4_bin'))
    detail = Column(String(255, u'utf8mb4_bin'))
    subdetail = Column(String(255, u'utf8mb4_bin'))
    price = Column(String(10, u'utf8mb4_bin'))
    original_price = Column(String(10, u'utf8mb4_bin'))


class BillLog(Base):
    __tablename__ = 'bill_logs'

    id = Column(Integer, primary_key=True)
    order_code = Column(String(32))
    operate_id = Column(BigInteger)
    operate_name = Column(String(32))
    bill_money = Column(Float(12, True))
    update_at = Column(DateTime)
    create_at = Column(DateTime)
    bak = Column(String(32))
    order_name = Column(String(32))
    free_money = Column(Float(12, True))
    val_price = Column(Float(12, True))
    order_type = Column(Enum(u'2', u'3', u'4', u'5', u'6', u'19', u'18', u'20', u'8', u'7', u'21', u'22', u'1'))
    club_id = Column(String(125, u'utf8mb4_bin'))


class BsAddrWeixin(Base):
    __tablename__ = 'bs_addr_weixin'

    id = Column(Integer, primary_key=True)
    bs_weixin_id = Column(Integer)
    address_name = Column(String(125, u'utf8_bin'))
    address_value = Column(String(125, u'utf8_bin'))
    create_at = Column(DateTime)
    remarks = Column(String(255, u'utf8_bin'))


class BsArea(Base):
    __tablename__ = 'bs_area'

    areaid = Column(Integer, primary_key=True)
    area = Column(String(50), nullable=False)
    cityid = Column(Integer, nullable=False)


class BsCity(Base):
    __tablename__ = 'bs_city'

    cityid = Column(Integer, primary_key=True)
    city = Column(String(50), nullable=False)
    provinceid = Column(Integer, nullable=False)


class BsClub(Base):
    __tablename__ = 'bs_club'

    id = Column(String(50), primary_key=True)
    club_name = Column(String(60), nullable=False, server_default=text("''"))
    address = Column(String(60), server_default=text("''"))
    lat = Column(Float(asdecimal=True), server_default=text("'0'"))
    lng = Column(Float(asdecimal=True), server_default=text("'0'"))
    wx_openid = Column(String(255))
    website = Column(String(255))
    brief = Column(MEDIUMBLOB)
    cb_number = Column(String(255))
    province_id = Column(Integer)
    city_id = Column(Integer)
    area_id = Column(Integer)
    phone = Column(String(25))
    contacts = Column(String(56))
    contacts_phone = Column(String(125))
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    remarks = Column(String(255))
    domain_name = Column(String(125, u'utf8_bin'))
    haswx = Column(Integer)
    preStr = Column(String(125, u'utf8_bin'))


class BsClubSysinfo(Base):
    __tablename__ = 'bs_club_sysinfo'

    bid = Column(Integer, primary_key=True)
    domain_name = Column(String(125, u'utf8_bin'))
    data_name = Column(String(125, u'utf8_bin'))
    sys_version = Column(String(125, u'utf8_bin'))
    sys_server_addr = Column(String(255, u'utf8_bin'))
    oper_main_person = Column(String(125, u'utf8_bin'))
    oper_main_phone = Column(String(125, u'utf8_bin'))
    club_id = Column(String(50, u'utf8_bin'))
    front_end_version = Column(String(132, u'utf8_bin'))


class BsClubWeixin(Base):
    __tablename__ = 'bs_club_weixin'

    bid = Column(Integer, primary_key=True)
    app_id = Column(String(124, u'utf8_bin'))
    secrect = Column(String(125, u'utf8_bin'))
    mch_id = Column(String(15, u'utf8_bin'))
    wx_redirect_url = Column(String(125, u'utf8_bin'))
    QRcode = Column(String(124, u'utf8_bin'))
    club_preview = Column(String(125, u'utf8_bin'))
    club_id = Column(String(50, u'utf8_bin'))
    create_at = Column(DateTime)
    remarks = Column(String(255, u'utf8_bin'))
    club_full_address = Column(String(1255, u'utf8_bin'), server_default=text("'???????'"))
    club_base_url = Column(String(255, u'utf8_bin'))


class BsCourt(Base):
    __tablename__ = 'bs_court'

    id = Column(Integer, primary_key=True)
    court_name = Column(String(50), nullable=False, server_default=text("''"))
    court_type_id = Column(Integer)
    show_num = Column(Integer)
    club_id = Column(String(125, u'utf8mb4_bin'))


class BsCourtPricePlan(Base):
    __tablename__ = 'bs_court_price_plan'

    id = Column(Integer, primary_key=True)
    cpp_code = Column(String(20))
    cpp_name = Column(String(50))
    court_type_id = Column(Integer)
    daytype = Column(String(2))
    h1 = Column(Float(asdecimal=True))
    h2 = Column(Float(asdecimal=True))
    h3 = Column(Float(asdecimal=True))
    h4 = Column(Float(asdecimal=True))
    h5 = Column(Float(asdecimal=True))
    h6 = Column(Float(asdecimal=True))
    h7 = Column(Float(asdecimal=True))
    h8 = Column(Float(asdecimal=True))
    h9 = Column(Float(asdecimal=True))
    h10 = Column(Float(asdecimal=True))
    h11 = Column(Float(asdecimal=True))
    h12 = Column(Float(asdecimal=True))
    h13 = Column(Float(asdecimal=True))
    h14 = Column(Float(asdecimal=True))
    h15 = Column(Float(asdecimal=True))
    h16 = Column(Float(asdecimal=True))
    h17 = Column(Float(asdecimal=True))
    h18 = Column(Float(asdecimal=True))
    h19 = Column(Float(asdecimal=True))
    h20 = Column(Float(asdecimal=True))
    h21 = Column(Float(asdecimal=True))
    h22 = Column(Float(asdecimal=True))
    h23 = Column(Float(asdecimal=True))
    h24 = Column(Float(asdecimal=True))
    court_name = Column(String(120))
    club_id = Column(String(125, u'utf8mb4_bin'))


class BsCourtRel(Base):
    __tablename__ = 'bs_court_rel'

    id = Column(Integer, primary_key=True)
    court_id = Column(Integer)
    rl_court_id = Column(Integer)
    create_at = Column(DateTime)


class BsCourtType(Base):
    __tablename__ = 'bs_court_type'

    id = Column(Integer, primary_key=True)
    court_type_name = Column(String(50), nullable=False)
    sport_type = Column(String(50), nullable=False, server_default=text("''"))
    available = Column(Integer, server_default=text("'1'"))
    update_time = Column(DateTime)
    amount = Column(Integer)
    business_start_time = Column(String(10), server_default=text("''"))
    business_end_time = Column(String(10))
    web_reserve = Column(Integer)
    remind_minutes = Column(Integer, server_default=text("'15'"))
    timeout_buffer = Column(Integer, server_default=text("'0'"))
    start_delay_billing = Column(Integer)
    timeout_billing_type = Column(String(20), server_default=text("'REAL_TIME'"))
    min_consume = Column(Integer, server_default=text("'0'"))
    accounts_on_start = Column(Integer, server_default=text("'0'"))
    min_space = Column(Integer, server_default=text("'30'"))
    is_tour = Column(Integer, server_default=text("'1'"))
    club_id = Column(String(125, u'utf8mb4_bin'))


class BsDayset(Base):
    __tablename__ = 'bs_dayset'

    id = Column(Integer, primary_key=True)
    datetype = Column(String(255, u'utf8_bin'))
    day = Column(Date)
    update_time = Column(DateTime)
    bak = Column(String(50, u'utf8_bin'))
    club_id = Column(String(125, u'utf8mb4_bin'))


class BsPriceProject(Base):
    __tablename__ = 'bs_price_project'

    id = Column(Integer, primary_key=True)
    name = Column(String(125, u'utf8_bin'), nullable=False)
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    remarks = Column(String(255, u'utf8_bin'))
    is_default = Column(Integer, nullable=False, server_default=text("'0'"))
    is_discount = Column(Integer, server_default=text("'1'"))
    court_type_id = Column(Integer, nullable=False)
    club_id = Column(String(180, u'utf8mb4_bin'))
    service_price = Column(Float(12, True))
    is_valid = Column(Integer, server_default=text("'0'"))
    is_net = Column(Integer, server_default=text("'0'"))


class BsProvince(Base):
    __tablename__ = 'bs_province'

    provinceid = Column(Integer, primary_key=True)
    province = Column(String(50), nullable=False)


class ClubBank(Base):
    __tablename__ = 'club_bank'

    id = Column(Integer, primary_key=True)
    name = Column(String(255, u'utf8mb4_bin'))
    account = Column(String(255, u'utf8mb4_bin'))
    bank = Column(String(255, u'utf8mb4_bin'))
    club_id = Column(String(125, u'utf8mb4_bin'))


class ClubCommission(Base):
    __tablename__ = 'club_commission'

    id = Column(Integer, primary_key=True)
    start_point = Column(Integer)
    end_point = Column(Integer)
    level = Column(Float(11, True))
    sign_date = Column(DateTime)
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    club_id = Column(String(125, u'utf8mb4_bin'))


class CourseCoach(Base):
    __tablename__ = 'course_coach'

    id = Column(Integer, primary_key=True)
    code = Column(String(125, u'utf8_bin'), server_default=text("''"))
    name = Column(String(125, u'utf8_bin'))
    sex = Column(Integer, server_default=text("'1'"))
    age = Column(Integer)
    phone = Column(String(60, u'utf8_bin'))
    height = Column(Integer)
    weight = Column(Float(12, True))
    remarks = Column(String(125, u'utf8_bin'))
    sport_type_id = Column(Integer)
    st_code = Column(String(50, u'utf8_bin'))
    st_name = Column(String(50, u'utf8_bin'))
    introduce = Column(String(255, u'utf8_bin'))


class CourseCoachRele(Base):
    __tablename__ = 'course_coach_rele'

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer)
    remarks = Column(String(255, u'utf8_bin'))
    coach_id = Column(Integer)
    create_at = Column(DateTime)
    update_at = Column(DateTime)


class CourseInfo(Base):
    __tablename__ = 'course_info'

    id = Column(Integer, primary_key=True)
    code = Column(String(125, u'utf8_bin'))
    class_number = Column(Integer)
    name = Column(String(125, u'utf8_bin'))
    max_member = Column(Integer)
    time_introduce = Column(String(255, u'utf8_bin'))
    apply_end_time = Column(DateTime)
    apply_start_time = Column(DateTime)
    start_time = Column(Date)
    end_time = Column(Date)
    introduce = Column(String(255, u'utf8_bin'))
    is_net_application = Column(Integer, server_default=text("'1'"))
    tuition_introduce = Column(String(255, u'utf8_bin'))
    tuition = Column(Float(12, True))
    net_tuition = Column(Float(12, True))
    create_at = Column(DateTime)
    sport_type_id = Column(Integer)
    st_code = Column(String(50, u'utf8_bin'))
    st_name = Column(String(50, u'utf8_bin'))
    lessons_address = Column(String(255, u'utf8_bin'))
    has_apply_number = Column(Integer)
    update_at = Column(DateTime)
    type = Column(Integer, server_default=text("'1'"))
    remarks = Column(String(255, u'utf8_bin'))
    route_introduce = Column(String(255, u'utf8_bin'))
    url = Column(String(255, u'utf8_bin'))
    coach_name = Column(String(25, u'utf8_bin'))
    coach_sex = Column(Integer, server_default=text("'1'"))
    city_id = Column(Integer)


class CourseStudentInfo(Base):
    __tablename__ = 'course_student_info'

    id = Column(Integer, primary_key=True)
    name = Column(String(125, u'utf8_bin'), nullable=False)
    age = Column(Integer)
    parent_name = Column(String(125, u'utf8_bin'))
    parent_phone = Column(String(125, u'utf8_bin'))
    parent_cell_phone = Column(String(125, u'utf8_bin'), nullable=False)
    open_id = Column(String(64, u'utf8_bin'))
    remarks = Column(String(255, u'utf8_bin'))
    create_at = Column(DateTime)
    card_id = Column(String(255, u'utf8_bin'))


class CourseStudentRele(Base):
    __tablename__ = 'course_student_rele'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    course_id = Column(Integer)
    is_affirm = Column(Integer, server_default=text("'0'"))
    remarks = Column(String(255, u'utf8_bin'), server_default=text("''"))
    create_at = Column(DateTime)
    source = Column(Enum(u'CLUB', u'WX'))
    update_at = Column(DateTime)
    verify_code = Column(String(25, u'utf8_bin'))


class CourseTicketCode(Base):
    __tablename__ = 'course_ticket_code'

    id = Column(Integer, primary_key=True)
    code = Column(String(25, u'utf8_bin'))
    state = Column(Integer, server_default=text("'0'"))
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    remarks = Column(String(255, u'utf8_bin'))
    type = Column(Integer, server_default=text("'0'"))
    sure_time = Column(DateTime)


class CourseTicketRele(Base):
    __tablename__ = 'course_ticket_rele'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    ticket_id = Column(Integer)
    order_code = Column(String(50, u'utf8_bin'))
    course_id = Column(Integer)
    verify_code = Column(String(50, u'utf8_bin'))
    is_affirm = Column(Integer, server_default=text("'0'"))
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    remarks = Column(String(50, u'utf8_bin'))
    state = Column(Integer, server_default=text("'0'"))
    phone = Column(String(255, u'utf8_bin'))
    student_name = Column(String(50, u'utf8mb4_bin'))


class CourseTicket(Base):
    __tablename__ = 'course_tickets'

    id = Column(Integer, primary_key=True)
    ticket_typeid = Column(Integer)
    ticket_typename = Column(String(50, u'utf8_bin'))
    ticket_number = Column(Integer)
    ticket_maxnum = Column(Integer)
    ticket_selled = Column(Integer)
    ticket_price = Column(Float(11, True))
    ticket_sellprice = Column(Float(11, True))
    remark = Column(String(50, u'utf8_bin'))


class CourtConsumeRecord(Base):
    __tablename__ = 'court_consume_record'

    id = Column(Integer, primary_key=True)
    court_type_id = Column(Integer)
    court_codes = Column(String(100, u'utf8mb4_bin'))
    court_name = Column(String(255, u'utf8mb4_bin'))
    total_order_code = Column(String(125, u'utf8mb4_bin'))
    real_order_code = Column(String(125, u'utf8mb4_bin'))
    operate_id = Column(Integer)
    operate_name = Column(String(45, u'utf8mb4_bin'))
    remarks = Column(String(100, u'utf8mb4_bin'))
    mc_code = Column(String(125, u'utf8mb4_bin'))
    member_id = Column(Integer)
    playername = Column(String(20, u'utf8mb4_bin'))
    create_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))


class CourtConsumeRecordDetail(Base):
    __tablename__ = 'court_consume_record_detail'

    id = Column(Integer, primary_key=True)
    record_id = Column(Integer)
    goods_id = Column(Integer)
    good_name = Column(String(125, u'utf8mb4_bin'))
    pay_code = Column(String(125, u'utf8mb4_bin'))
    num = Column(Integer)
    create_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    order_code = Column(String(125, u'utf8mb4_bin'))
    total_order_code = Column(String(125, u'utf8mb4_bin'))
    sell_money = Column(Float(12, True))
    unit_price = Column(Float(12, True))
    remark = Column(String(100, u'utf8mb4_bin'))
    card_type_id = Column(Integer)
    point_lv = Column(Float(asdecimal=True))
    rl_card_id = Column(Integer)
    qr_code = Column(String(255, u'utf8mb4_bin'))


class DataExport(Base):
    __tablename__ = 'data_export'

    id = Column(Integer, primary_key=True)
    name = Column(String(256, u'utf8_bin'))
    operator_name = Column(String(256, u'utf8_bin'))
    operator_id = Column(Integer)
    create_at = Column(DateTime)
    type = Column(Enum(u'0', u'2', u'3', u'6', u'5', u'4', u'1'))
    status = Column(Integer)
    path = Column(String(256, u'utf8_bin'))
    club_id = Column(String(125, u'utf8mb4_bin'))


class EquipRecord(Base):
    __tablename__ = 'equip_record'

    id = Column(Integer, primary_key=True)
    card_no = Column(String(32, u'utf8mb4_bin'), nullable=False)
    equip_id = Column(String(32, u'utf8mb4_bin'), nullable=False)
    name = Column(String(255, u'utf8mb4_bin'))
    deposit = Column(Float(11, True))
    rent = Column(Float(11, True))
    num = Column(Integer, server_default=text("'1'"))
    type = Column(Integer)
    status = Column(Integer, server_default=text("'1'"))
    operator_id = Column(Integer)
    operator_name = Column(String(255, u'utf8mb4_bin'))
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    club_id = Column(String(255, u'utf8mb4_bin'))


t_fitness_locker = Table(
    'fitness_locker', metadata,
    Column('code', String(255, u'utf8mb4_bin')),
    Column('kind', String(255, u'utf8mb4_bin')),
    Column('ftickh', String(255, u'utf8mb4_bin'))
)


class GoodPutin(Base):
    __tablename__ = 'good_putin'

    id = Column(Integer, primary_key=True)
    ticket_id = Column(String(50))
    good_id = Column(Integer)
    good_code = Column(String(50))
    good_name = Column(String(50))
    good_bar = Column(String(50))
    good_unit = Column(String(124))
    warehouse_id = Column(Integer)
    warehouse_name = Column(String(50))
    good_number = Column(Integer)
    purchase_price = Column(Float(12, True))
    deposit_rate = Column(Float(12, True))
    deduction = Column(Float(12, True))
    purchase_amount = Column(Float(12, True))
    operate_id = Column(Integer)
    bar = Column(String(255))
    operante_name = Column(String(50))
    putin_date = Column(Date)
    avaliable = Column(Integer, server_default=text("'1'"))
    create_at = Column(DateTime)
    from_warehouse_id = Column(Integer)
    from_warehouse_name = Column(String(255, u'utf8mb4_bin'))
    club_id = Column(String(125, u'utf8mb4_bin'))
    bill_type = Column(Integer)
    old_num = Column(Integer)
    diff_num = Column(Integer)


class GoodsBackRecord(Base):
    __tablename__ = 'goods_back_record'

    id = Column(Integer, primary_key=True)
    goods_id = Column(Integer)
    order_code = Column(String(125, u'utf8_bin'))
    old_order_code = Column(String(125, u'utf8_bin'))
    avilable = Column(Integer, server_default=text("'0'"))
    remarks = Column(String(255, u'utf8_bin'))
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    club_id = Column(String(111, u'utf8mb4_bin'))


class GoodsDetail(Base):
    __tablename__ = 'goods_detail'

    id = Column(Integer, primary_key=True)
    amount = Column(Integer, server_default=text("'1'"))
    unit_price = Column(Float(20, True), server_default=text("'0.00'"))
    order_code = Column(String(32))
    bar = Column(String(125, u'utf8_bin'))
    update_by = Column(DateTime)
    create_by = Column(DateTime)
    goods_id = Column(Integer)
    code_number = Column(Enum(u'GOODS', u'RMGOODS', u'ACTIVE', u'OTHER', u'CHARGE', u'TICKET'))
    hand_card = Column(String(25, u'utf8_bin'))
    cardtype_id = Column(Integer)
    tk_type_id = Column(Integer)
    discount_price = Column(Float(20, True), server_default=text("'0.00'"))
    num = Column(Integer, server_default=text("'0'"))
    rl_card_id = Column(Integer)
    point_lv = Column(Float(12, True), server_default=text("'1.00'"))
    club_id = Column(String(125, u'utf8mb4_bin'))
    ticket_card_id = Column(Integer)


class GoodsMessage(Base):
    __tablename__ = 'goods_message'

    id = Column(Integer, primary_key=True)
    good_code = Column(String(50))
    good_name = Column(String(50))
    good_simple = Column(String(50))
    good_bar = Column(String(50))
    good_model = Column(String(50))
    type_id = Column(Integer)
    type_name = Column(String(50))
    warehouse_id = Column(Integer)
    warehouse_name = Column(String(50))
    min_inventory = Column(Integer, server_default=text("'0'"))
    max_inventory = Column(Integer, server_default=text("'0'"))
    good_unit = Column(Enum(u'KG', u'HALF_KG', u'GE', u'?', u'PACKAGE', u'ITEM', u'DOUBLE', u'BUCKET', u'OBEY', u'DEPUTY', u'BRANCH', u'NEXT', u'PIECE', u'BOX', u'BAG', u'CUP', u'TUBE', u'ROOT', u'PAY', u'TAI', u'TAO', u'KUAI', u'JUAN', u'?', u'?', u'?', u'?', u'?', u'?', u'?', u'?', u'?', u'?', u'?', u'?', u'BOTTLE'))
    ex_price = Column(Float(12, True), server_default=text("'0.00'"))
    sell_price = Column(Float(12, True), server_default=text("'0.00'"))
    is_discount = Column(Integer, server_default=text("'1'"))
    is_effective = Column(Integer, server_default=text("'1'"))
    is_exchange = Column(Integer, server_default=text("'1'"))
    exchange_integral = Column(Integer, server_default=text("'1'"))
    is_manage = Column(Integer, server_default=text("'1'"))
    is_handprice = Column(Integer)
    bar = Column(String(255))
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    sell_num = Column(Float(25, True), server_default=text("'0.00'"))
    club_id = Column(String(125, u'utf8mb4_bin'))


class GoodsOrder(Base):
    __tablename__ = 'goods_order'

    id = Column(Integer, primary_key=True)
    order_code = Column(String(32), nullable=False)
    goods_name = Column(String(15, u'utf8_bin'))
    amount = Column(Integer, server_default=text("'0'"))
    sell_price = Column(Float(20, True), server_default=text("'0.00'"))
    unit_price = Column(Float(20, True), server_default=text("'0.00'"))
    ordertype = Column(Enum(u'7', u'8', u'9', u'10', u'11', u'12', u'13', u'4', u'2', u'1', u'6', u'15', u'16', u'17', u'14', u'18', u'19', u'21', u'20', u'5', u'3', u'22', u'23'))
    rl_card_id = Column(Integer)
    create_by = Column(DateTime)
    update_by = Column(DateTime)
    order_state = Column(Integer, server_default=text("'1'"))
    remark = Column(String(255, u'utf8_bin'))
    operate_name = Column(String(255, u'utf8_bin'), server_default=text("''"))
    operate_id = Column(BigInteger)
    member_id = Column(Integer)
    num = Column(Integer, server_default=text("'0'"))
    days = Column(Integer)
    mc_code = Column(String(11, u'utf8_bin'), server_default=text("''"))
    member_cost = Column(Float(10, True))
    free_price = Column(Float(10, True))
    code_number = Column(Enum(u'GOODS', u'RMGOODS', u'ACTIVE', u'OTHER', u'CHARGE', u'TICKET'))
    point = Column(Integer, server_default=text("'0'"))
    fee_minus = Column(Float(11, True))
    wh_id = Column(Integer)
    club_id = Column(String(125, u'utf8mb4_bin'))
    max_account = Column(Float(11, True))
    hand_card_id = Column(String(125, u'utf8mb4_bin'))
    card_type_id = Column(Integer)
    auth_userid = Column(Integer)
    auth_username = Column(String(64, u'utf8mb4_bin'))


class GoodsType(Base):
    __tablename__ = 'goods_type'

    id = Column(Integer, primary_key=True)
    type_code = Column(String(50))
    type_name = Column(String(50))
    type_level = Column(String(50))
    type_parentId = Column(Integer)
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    bar = Column(String(255))
    is_effective = Column(Integer)
    club_id = Column(String(125, u'utf8mb4_bin'))


class HardCard(Base):
    __tablename__ = 'hard_card'

    id = Column(Integer, primary_key=True)
    code = Column(String(32, u'utf8_bin'))
    attribute = Column(Enum(u'HAND_CARD'), server_default=text("'HAND_CARD'"))
    name = Column(String(32, u'utf8_bin'))
    state = Column(Integer, server_default=text("'1'"))
    phy_code = Column(String(32, u'utf8_bin'))
    berf = Column(String(128, u'utf8_bin'), server_default=text("''"))
    bar = Column(String(64, u'utf8_bin'))
    parent_id = Column(Integer)
    club_id = Column(String(125, u'utf8mb4_bin'))


class HdFaceConfig(Base):
    __tablename__ = 'hd_face_config'

    id = Column(Integer, primary_key=True)
    name = Column(String(255, u'utf8mb4_bin'))
    koalaIp = Column(String(15, u'utf8mb4_bin'))
    cameraIp = Column(String(15, u'utf8mb4_bin'))
    gateSerial = Column(String(255, u'utf8mb4_bin'))
    club_id = Column(String(255, u'utf8mb4_bin'))


class LightAuto(Base):
    __tablename__ = 'light_auto'

    id = Column(Integer, primary_key=True)
    light_name = Column(String(125, u'utf8mb4_bin'))
    light_order = Column(String(125, u'utf8mb4_bin'))
    light_ip = Column(String(125, u'utf8mb4_bin'))
    club_id = Column(String(125, u'utf8mb4_bin'))


class LightAutoLine(Base):
    __tablename__ = 'light_auto_line'

    id = Column(Integer, primary_key=True)
    light_order_name = Column(String(125, u'utf8mb4_bin'))
    light_order_line = Column(String(125, u'utf8mb4_bin'))
    light_order_close = Column(String(125, u'utf8mb4_bin'))
    light_order_open = Column(String(125, u'utf8mb4_bin'))
    light_id = Column(Integer)


class LightAutoRecord(Base):
    __tablename__ = 'light_auto_record'

    id = Column(Integer, primary_key=True)
    cron_name = Column(String(125, u'utf8mb4_bin'))
    reserve_id = Column(String(126, u'utf8mb4_bin'))
    expression = Column(String(125, u'utf8mb4_bin'))
    is_execute = Column(Integer, server_default=text("'0'"))
    light_order = Column(String(40, u'utf8mb4_bin'))
    create_at = Column(DateTime)
    club_id = Column(String(125, u'utf8mb4_bin'))


class LightCourtSet(Base):
    __tablename__ = 'light_court_set'

    id = Column(Integer, primary_key=True)
    court_id = Column(Integer)
    light_id = Column(Integer)
    line_id = Column(Integer)


class LightRecord(Base):
    __tablename__ = 'light_record'

    id = Column(Integer, primary_key=True)
    court_id = Column(Integer)
    ligth_line_id = Column(Integer)
    operate = Column(Integer)
    operate_id = Column(Integer)
    operate_name = Column(String(125, u'utf8mb4_bin'))
    create_at = Column(DateTime)
    club_id = Column(String(125, u'utf8mb4_bin'))
    during_time = Column(String(125, u'utf8mb4_bin'))


class MemCard(Base):
    __tablename__ = 'mem_card'

    id = Column(Integer, primary_key=True)
    mc_type = Column(String(50), server_default=text("''"))
    member_id = Column(Integer, nullable=False)
    mc_code = Column(String(25), nullable=False, server_default=text("''"))
    available = Column(Integer, server_default=text("'1'"))
    update_time = Column(DateTime)
    mc_code_mac = Column(String(50), server_default=text("''"))
    mc_code_virtual = Column(String(50), server_default=text("''"))
    state = Column(Enum(u'LOSE_VALUE', u'NOMAL', u'STOP', u'NO_EXESIT', u'BACK'), server_default=text("'NOMAL'"))
    stop_begin = Column(Date)
    stop_end = Column(Date)
    change_code = Column(String(25))
    club_id = Column(String(125, u'utf8mb4_bin'))
    salesman_id = Column(Integer)
    salesman_name = Column(String(32, u'utf8mb4_bin'))


class MemCardManager(Base):
    __tablename__ = 'mem_card_manager'

    id = Column(Integer, primary_key=True)
    mc_code = Column(String(50))
    mc_code_mac = Column(String(100))
    state = Column(Integer, server_default=text("'0'"))
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    remarks = Column(String(255))
    club_id = Column(String(125, u'utf8mb4_bin'))


class MemCardType(Base):
    __tablename__ = 'mem_card_type'

    id = Column(Integer, primary_key=True)
    card_type_name = Column(String(50), nullable=False)
    card_type_desc = Column(String(200))
    free_price = Column(Float(10, True), server_default=text("'0.00'"))
    value_type = Column(Enum(u'DATELINE', u'NUM', u'CASH'), nullable=False)
    available = Column(Integer, server_default=text("'1'"))
    update_time = Column(DateTime)
    create_time = Column(DateTime)
    val_days = Column(Integer, nullable=False, server_default=text("'124'"))
    point_rate = Column(String(11))
    point_method = Column(Enum(u'CONSUME_CHARGE', u'CONSUME', u'CHARGE', u'NO'), server_default=text("'CHARGE'"))
    bak = Column(String(100))
    card_cost = Column(Integer, server_default=text("'0'"))
    net_handle = Column(Integer)
    card_id = Column(Integer)
    sell_price = Column(Float(10, True), server_default=text("'0.00'"))
    val_price = Column(Float(10, True), server_default=text("'0.00'"))
    val_num = Column(Integer, server_default=text("'0'"))
    put_off_style = Column(Enum(u'CHARGE_LEFT_DAY', u'CHARGE_DAY'), server_default=text("'CHARGE_DAY'"))
    active_style = Column(Enum(u'TIMEING', u'USERED', u'OPEN'))
    active_days = Column(Integer)
    club_id = Column(String(125, u'utf8mb4_bin'))
    is_net = Column(Integer, server_default=text("'0'"))
    description = Column(String(10000, u'utf8mb4_bin'))
    activate_day = Column(Integer, server_default=text("'0'"))
    is_limit = Column(Integer, server_default=text("'0'"))
    limit_day = Column(String(45, u'utf8mb4_bin'))
    limit_time = Column(String(100, u'utf8mb4_bin'))
    is_face_reco = Column(Integer, server_default=text("'0'"))


class MemIcon(Base):
    __tablename__ = 'mem_icon'

    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, nullable=False)
    head_url = Column(MEDIUMBLOB)
    create_at = Column(DateTime)
    club_id = Column(String(125, u'utf8mb4_bin'))
    state = Column(Integer, server_default=text("'0'"))
    update_data = Column(Integer, server_default=text("'0'"))


class MemMember(Base):
    __tablename__ = 'mem_member'

    id = Column(Integer, primary_key=True)
    member_name = Column(String(50), nullable=False, server_default=text("''"))
    sex = Column(String(6), server_default=text("''"))
    card_id = Column(String(20))
    phone = Column(String(128))
    birthday = Column(String(20))
    passwd = Column(String(50))
    mail = Column(String(50))
    wx_nick = Column(String(50))
    wx_openid = Column(String(50))
    wx_img = Column(String(1000))
    point = Column(Integer, server_default=text("'0'"))
    available = Column(Integer, server_default=text("'1'"))
    update_time = Column(DateTime)
    create_time = Column(DateTime)
    remarks = Column(String(120))
    prompt_message = Column(String(120), server_default=text("''"))
    is_curson = Column(Integer, server_default=text("'0'"))
    bind_id = Column(Integer)
    club_id = Column(String(125, u'utf8mb4_bin'))
    left_money = Column(Float(12, True), server_default=text("'0.00'"))
    mem_kind = Column(Integer, server_default=text("'0'"))
    ic_phy_card = Column(String(255, u'utf8mb4_bin'), server_default=text("''"))


class MemPayMsgTotal(Base):
    __tablename__ = 'mem_pay_msg_total'

    id = Column(Integer, primary_key=True)
    mc_code = Column(String(11, u'utf8mb4_bin'))
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    pay_number = Column(Integer)
    msg_number = Column(Integer)
    club_id = Column(String(125, u'utf8mb4_bin'))


class MemRecord(Base):
    __tablename__ = 'mem_record'

    id = Column(Integer, primary_key=True)
    mc_code = Column(String(25), nullable=False, server_default=text("''"))
    operate_type = Column(Enum(u'5', u'4', u'3', u'2', u'7', u'6', u'8', u'9', u'10', u'11', u'12', u'14', u'13', u'16', u'17', u'18', u'20', u'19', u'21', u'22', u'23', u'24', u'25', u'26', u'27', u'29', u'1'))
    created_at = Column(DateTime)
    update_at = Column(DateTime)
    mem_id = Column(Integer)
    bill_money = Column(Float(11, True), server_default=text("'0.00'"))
    bar = Column(String(64))
    operate_id = Column(BigInteger)
    operate_name = Column(String(32))
    num = Column(Integer, server_default=text("'0'"))
    days = Column(Integer, server_default=text("'0'"))
    free_money = Column(Float(12, True), server_default=text("'0.00'"))
    rl_id = Column(Integer)
    left_money = Column(Float(12, True), server_default=text("'0.00'"))
    operate_type_name = Column(String(125))
    left_num = Column(Integer, server_default=text("'0'"))
    remarks = Column(String(255, u'utf8mb4_bin'), server_default=text("''"))
    mem_type_id = Column(Integer)
    club_id = Column(String(125, u'utf8mb4_bin'))
    order_code = Column(String(22, u'utf8mb4_bin'))


class MemTypeMsg(Base):
    __tablename__ = 'mem_type_msg'

    id = Column(Integer, primary_key=True)
    mem_type_id = Column(Integer)
    msg_type = Column(Enum(u'court', u'birthday', u'consume'))


class MemberAccount(Base):
    __tablename__ = 'member_account'

    id = Column(Integer, primary_key=True)
    mc_code = Column(String(10, u'utf8mb4_bin'))
    member_name = Column(String(10, u'utf8mb4_bin'))
    total_money = Column(Float(10, True), server_default=text("'0.00'"))
    pay_money = Column(Float(10, True))
    left_money = Column(Float(10, True), server_default=text("'0.00'"))
    operate_id = Column(Integer)
    operate_name = Column(String(10, u'utf8mb4_bin'))
    club_id = Column(String(125, u'utf8mb4_bin'))
    create_at = Column(DateTime)
    pay_code = Column(String(10, u'utf8mb4_bin'))
    order_code = Column(String(100, u'utf8mb4_bin'))
    status = Column(Integer)
    rl_id = Column(Integer)
    card_type_name = Column(String(10, u'utf8mb4_bin'))
    balance_money = Column(Float(10, True), server_default=text("'0.00'"))
    member_id = Column(Integer)


t_memcardlog = Table(
    'memcardlog', metadata,
    Column('cardno', String(255, u'utf8mb4_bin')),
    Column('name', String(255, u'utf8mb4_bin')),
    Column('total', String(255, u'utf8mb4_bin')),
    Column('totalbalance', String(255, u'utf8mb4_bin')),
    Column('time', String(255, u'utf8mb4_bin')),
    Column('timebalance', String(255, u'utf8mb4_bin')),
    Column('logdate', String(255, u'utf8mb4_bin')),
    Column('usertime', String(255, u'utf8mb4_bin')),
    Column('memo', String(255, u'utf8mb4_bin'))
)


class Notice(Base):
    __tablename__ = 'notice'

    id = Column(Integer, primary_key=True)
    title = Column(String(255, u'utf8mb4_bin'))
    body = Column(String(1024, u'utf8mb4_bin'))
    category = Column(Enum(u'club', u'sys'))
    create_date = Column(DateTime)
    username = Column(String(255, u'utf8mb4_bin'))
    club_id = Column(String(255, u'utf8mb4_bin'))


class OperateRecord(Base):
    __tablename__ = 'operate_record'

    id = Column(Integer, primary_key=True)
    name = Column(String(32, u'utf8_bin'))
    code = Column(String(32, u'utf8_bin'))
    operate_name = Column(String(32, u'utf8_bin'))
    operate_id = Column(BigInteger)
    create_at = Column(DateTime)
    bar = Column(String(125, u'utf8_bin'), server_default=text("'??'"))
    ip = Column(String(125, u'utf8_bin'))
    club_id = Column(String(125, u'utf8mb4_bin'))


class OrderBase(Base):
    __tablename__ = 'order_base'

    id = Column(Integer, primary_key=True)
    court_type_id = Column(Integer, nullable=False)
    court_type_name = Column(String(64, u'utf8_bin'))
    order_code = Column(String(32, u'utf8_bin'))
    member_id = Column(Integer)
    court_num = Column(Integer)
    username = Column(String(32, u'utf8_bin'))
    mobile = Column(String(100, u'utf8_bin'))
    member_card_id = Column(Integer)
    member_card_number = Column(String(32, u'utf8_bin'))
    member_card_type_id = Column(Integer)
    deposit = Column(Integer)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    status = Column(Integer)
    created_time = Column(DateTime)
    updated_time = Column(DateTime)
    operator_id_open = Column(Integer)
    operator_name_open = Column(String(10, u'utf8_bin'))
    operator_id_close = Column(Integer)
    operator_name_close = Column(String(10, u'utf8_bin'))
    operator_date = Column(Date)
    amount = Column(Float(16, True), server_default=text("'0.00'"))
    pay_type = Column(String(16, u'utf8_bin'))
    remark = Column(String(256, u'utf8_bin'))
    open_time = Column(DateTime)
    close_time = Column(DateTime)
    order_from = Column(Integer)
    vetify_code = Column(Integer)
    order_qr_code = Column(String(256, u'utf8_bin'))
    sport_code = Column(String(32, u'utf8_bin'))
    val_price = Column(Float(12, True))
    total_order_code = Column(String(255, u'utf8_bin'))
    court_id = Column(Integer)
    club_id = Column(String(125, u'utf8mb4_bin'))
    order_type = Column(Integer, server_default=text("'0'"))
    bill_money = Column(Float(16, True))
    auth_userid = Column(Integer)
    auth_username = Column(String(64, u'utf8mb4_bin'))


class OrderCourt(Base):
    __tablename__ = 'order_court'

    id = Column(Integer, primary_key=True)
    order_code = Column(String(32, u'utf8_bin'))
    court_id = Column(Integer)
    count_name = Column(String(32, u'utf8_bin'))
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    club_id = Column(String(125, u'utf8mb4_bin'))


class OrderReleCode(Base):
    __tablename__ = 'order_rele_code'

    id = Column(Integer, primary_key=True)
    order_code = Column(String(125, u'utf8_bin'))
    total_order_code = Column(String(125, u'utf8_bin'))
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    week_day = Column(Integer)
    club_id = Column(String(125, u'utf8mb4_bin'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)


class OrderReserve(Base):
    __tablename__ = 'order_reserve'

    id = Column(Integer, primary_key=True)
    court_type_id = Column(Integer, nullable=False)
    order_code = Column(String(32, u'utf8_bin'))
    court_num = Column(Integer)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    username = Column(String(32, u'utf8_bin'))
    mobile = Column(String(128, u'utf8_bin'))
    status = Column(String(25, u'utf8_bin'))
    court_id = Column(Integer)
    created_at = Column(DateTime)
    club_id = Column(String(125, u'utf8mb4_bin'))


class OtherExpense(Base):
    __tablename__ = 'other_expense'

    id = Column(Integer, primary_key=True)
    pro_name = Column(String(55, u'utf8mb4_bin'))
    pro_type = Column(Integer, server_default=text("'1'"))
    remark = Column(String(111, u'utf8mb4_bin'))
    simple = Column(String(111, u'utf8mb4_bin'))
    club_id = Column(String(111, u'utf8mb4_bin'))


class PayStyle(Base):
    __tablename__ = 'pay_style'

    id = Column(Integer, primary_key=True)
    pay_code = Column(String(125))
    create_by = Column(DateTime)
    update_by = Column(DateTime)
    bill_money = Column(Float(asdecimal=True))
    bill_id = Column(Integer)
    club_id = Column(String(125, u'utf8mb4_bin'))


class PbSportType(Base):
    __tablename__ = 'pb_sport_type'

    id = Column(Integer, primary_key=True)
    st_code = Column(String(50), nullable=False, server_default=text("''"))
    st_name = Column(String(50), nullable=False, server_default=text("''"))
    available = Column(Integer, server_default=text("'1'"))
    update_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))


t_pos_bills = Table(
    'pos_bills', metadata,
    Column('billcode', String(255, u'utf8mb4_bin')),
    Column('billdate', String(255, u'utf8mb4_bin')),
    Column('memno', String(255, u'utf8mb4_bin')),
    Column('name', String(255, u'utf8mb4_bin')),
    Column('billtotal', String(255, u'utf8mb4_bin')),
    Column('totalpayable', String(255, u'utf8mb4_bin')),
    Column('paymethod', String(255, u'utf8mb4_bin')),
    Column('paydesp', String(255, u'utf8mb4_bin')),
    Column('fRemark', String(255, u'utf8mb4_bin'))
)


t_pos_sales = Table(
    'pos_sales', metadata,
    Column('billcode', String(255, u'utf8mb4_bin')),
    Column('saledate', String(255, u'utf8mb4_bin')),
    Column('itemname1', String(255, u'utf8mb4_bin')),
    Column('saleprice', String(255, u'utf8mb4_bin')),
    Column('quantity', String(255, u'utf8mb4_bin')),
    Column('saletotal', String(255, u'utf8mb4_bin')),
    Column('memno', String(255, u'utf8mb4_bin')),
    Column('paymethod', String(255, u'utf8mb4_bin'))
)


class ProjectCollectSet(Base):
    __tablename__ = 'project_collect_set'

    sid = Column(Integer, primary_key=True)
    value = Column(String(125, u'utf8_bin'))
    project_id = Column(Integer)
    is_need = Column(Integer, server_default=text("'1'"))
    instruction = Column(String(125, u'utf8_bin'))
    remarks = Column(String(255, u'utf8_bin'))


class ProjectDetailInfo(Base):
    __tablename__ = 'project_detail_info'

    did = Column(Integer, primary_key=True)
    projectid = Column(Integer)
    standard_name = Column(String(125))
    unit_price = Column(Float(12, True))
    validable = Column(Integer, server_default=text("'1'"))
    total_stock = Column(Integer, server_default=text("'0'"))
    remarks = Column(String(125, u'utf8_bin'))
    state = Column(Integer, server_default=text("'1'"))


class ProjectDistribution(Base):
    __tablename__ = 'project_distribution'

    id = Column(Integer, primary_key=True)
    sell_price = Column(Float(12, True), server_default=text("'0.00'"))
    channel = Column(Enum(u'self', u'yundongshi'))
    stock = Column(Integer, server_default=text("'0'"))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    disstate = Column(Integer, server_default=text("'0'"))
    describes = Column(String(255, u'utf8_bin'))
    remarks = Column(String(255, u'utf8_bin'))
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    project_detail_id = Column(Integer)


class ProjectInfo(Base):
    __tablename__ = 'project_info'

    pid = Column(Integer, primary_key=True)
    name = Column(String(125, u'utf8_bin'))
    factory_name = Column(String(125, u'utf8_bin'))
    project_type = Column(Enum(u'train', u'goods', u'active_event'))
    project_start_time = Column(DateTime)
    project_end_time = Column(DateTime)
    provinceid = Column(Integer)
    cityid = Column(Integer)
    areaid = Column(Integer)
    address = Column(String(255, u'utf8_bin'))
    describ = Column(MEDIUMBLOB)
    create_at = Column(DateTime)
    validable = Column(Integer, server_default=text("'1'"))
    state = Column(Integer, server_default=text("'1'"))
    remarks = Column(String(255, u'utf8_bin'))
    club_id = Column(String(125, u'utf8_bin'))
    edit_process = Column(Integer, server_default=text("'1'"))


class ProjectKeyInfo(Base):
    __tablename__ = 'project_key_info'

    kid = Column(Integer, primary_key=True)
    key_value = Column(String(255, u'utf8_bin'))
    connection_id = Column(Integer)
    belongs = Column(String(255, u'utf8_bin'))


class RlCardtypeBodybuild(Base):
    __tablename__ = 'rl_cardtype_bodybuild'

    id = Column(Integer, primary_key=True)
    cardtype_id = Column(Integer)
    club_id = Column(String(125))
    consume_project = Column(String(45))
    project_name = Column(String(45))
    project_include = Column(String(45))
    money = Column(Float(asdecimal=True))
    discount = Column(Float(asdecimal=True))
    available = Column(Integer)


class RlCardtypeCard(Base):
    __tablename__ = 'rl_cardtype_card'

    id = Column(Integer, primary_key=True)
    mc_code = Column(String(25), nullable=False, server_default=text("''"))
    card_type_Id = Column(Integer, nullable=False)
    card_left_balance = Column(Float(10, True), server_default=text("'0.00'"))
    create_day = Column(DateTime, nullable=False)
    card_left_num = Column(Integer, server_default=text("'0'"))
    end_day = Column(Date)
    available = Column(Integer, nullable=False, server_default=text("'1'"))
    update_by = Column(DateTime)
    card_cost = Column(Integer, server_default=text("'0'"))
    has_cost = Column(Integer, server_default=text("'0'"))
    state = Column(Integer, server_default=text("'1'"))
    fee_minus = Column(Float(11, True), server_default=text("'0.00'"))
    club_id = Column(String(125, u'utf8mb4_bin'))
    max_account = Column(Float(11, True))
    left_account = Column(Float(11, True), server_default=text("'0.00'"))
    activate_day = Column(Integer, server_default=text("'0'"))
    account_total_money = Column(Float(10, True), server_default=text("'0.00'"))
    balance_money = Column(Float(11, True), server_default=text("'0.00'"))


class RlCardtypeCourtype(Base):
    __tablename__ = 'rl_cardtype_courtype'

    id = Column(Integer, primary_key=True)
    court_type_id = Column(Integer, nullable=False)
    price_plan = Column(Integer)
    cardtype_id = Column(Integer)
    point_lv = Column(Float(asdecimal=True), server_default=text("'1'"))
    club_id = Column(String(125, u'utf8mb4_bin'))


class RlGoodCardtype(Base):
    __tablename__ = 'rl_good_cardtype'

    id = Column(Integer, primary_key=True)
    goods_id = Column(Integer)
    card_type_id = Column(Integer, nullable=False)
    point_lv = Column(Float(12, True), server_default=text("'1.00'"))
    bar = Column(String(255))
    goods_type_id = Column(Integer)
    price_plan = Column(String(255))
    club_id = Column(String(125, u'utf8mb4_bin'))


class RlMemberBodybuild(Base):
    __tablename__ = 'rl_member_bodybuild'

    id = Column(Integer, primary_key=True)
    mc_code = Column(String(45))
    card_type_id = Column(Integer)
    keynumber = Column(String(45))
    name = Column(String(45))
    sex = Column(Integer)
    register_time = Column(DateTime)
    left_time = Column(DateTime)
    statement = Column(Integer)
    club_id = Column(String(128))
    order_code = Column(String(128))


class RlTkTypeCard(Base):
    __tablename__ = 'rl_tk_type_card'

    id = Column(Integer, primary_key=True)
    tk_type_id = Column(Integer)
    cardtype_id = Column(Integer)
    point_lv = Column(Float(11, True), server_default=text("'1.00'"))
    update_by = Column(DateTime)
    avaliable = Column(Integer, server_default=text("'1'"))
    bak = Column(String(125, u'utf8_bin'))
    club_id = Column(String(125, u'utf8mb4_bin'))
    is_default = Column(Integer, nullable=False, server_default=text("'0'"))


class SyncDk(Base):
    __tablename__ = 'sync_dk'

    id = Column(Integer, primary_key=True)
    cardid = Column(String(16, u'utf8_bin'), nullable=False, server_default=text("''"))
    cardno = Column(String(16, u'utf8_bin'), nullable=False, server_default=text("''"))
    jntotal = Column(Float(16, True), nullable=False, server_default=text("'0'"))
    balance = Column(Float(16, True), nullable=False, server_default=text("'0'"))
    tranamt = Column(Float(16, True), nullable=False, server_default=text("'0'"))
    order_code = Column(String(64, u'utf8_bin'), nullable=False, server_default=text("''"))
    status = Column(Integer, nullable=False)


class SyncGoodsCode(Base):
    __tablename__ = 'sync_goods_code'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(52, u'utf8_bin'))
    phone = Column(String(12, u'utf8_bin'))
    price = Column(Float(12, True), primary_key=True, nullable=False, server_default=text("'0.00'"))
    state = Column(Integer)
    code = Column(String(255, u'utf8_bin'))
    order_code = Column(String(52, u'utf8_bin'))
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    remarks = Column(String(255, u'utf8_bin'))
    is_send = Column(Integer, server_default=text("'1'"))


class SysAccountRecord(Base):
    __tablename__ = 'sys_account_record'

    id = Column(Integer, primary_key=True)
    mc_code = Column(String(125, u'utf8mb4_bin'))
    card_type_name = Column(String(125, u'utf8mb4_bin'))
    card_type_Id = Column(Integer)
    member_name = Column(String(125, u'utf8mb4_bin'))
    create_at = Column(DateTime)
    order_code = Column(String(125, u'utf8mb4_bin'))
    super_code = Column(Integer)
    super_name = Column(String(125, u'utf8mb4_bin'))
    operate_code = Column(Integer)
    operate_code_name = Column(String(125, u'utf8mb4_bin'))
    operate_id = Column(Integer)
    operate_name = Column(String(125, u'utf8mb4_bin'))
    sell_money = Column(Float(12, True), server_default=text("'0.000'"))
    unit_price = Column(Float(12, True), server_default=text("'0.000'"))
    total_num = Column(Integer, server_default=text("'1'"))
    remarks = Column(String(255, u'utf8mb4_bin'))
    club_id = Column(String(125, u'utf8mb4_bin'))
    goods_operate_id = Column(Integer, server_default=text("'1'"))
    member_id = Column(Integer)
    rl_id = Column(Integer)
    total_order_code = Column(String(255, u'utf8mb4_bin'))
    point = Column(String(255, u'utf8mb4_bin'))
    order_from = Column(Integer, server_default=text("'0'"))
    common_data = Column(String(255, u'utf8mb4_bin'))
    phone = Column(String(125, u'utf8mb4_bin'))
    auth_userid = Column(Integer)
    auth_username = Column(String(64, u'utf8mb4_bin'))


class SysAccountRecordDetail(Base):
    __tablename__ = 'sys_account_record_detail'

    account_id = Column(Integer)
    id = Column(Integer, primary_key=True)
    pay_code = Column(String(125, u'utf8mb4_bin'))
    super_type_id = Column(Integer)
    super_type_name = Column(String(125, u'utf8mb4_bin'))
    type_id = Column(Integer)
    type_name = Column(String(125, u'utf8mb4_bin'))
    num = Column(Integer, server_default=text("'1'"))
    remarks = Column(String(255, u'utf8mb4_bin'))
    create_at = Column(DateTime)
    club_id = Column(String(125, u'utf8mb4_bin'))
    order_code = Column(String(125, u'utf8mb4_bin'))
    sell_money = Column(Float(12, True), server_default=text("'0.000'"))
    unit_price = Column(Float(12, True), server_default=text("'0.000'"))
    top_type_id = Column(Integer)
    top_type_name = Column(String(125, u'utf8mb4_bin'))
    point_lv = Column(Float(12, True), server_default=text("'1.00'"))
    operate_id = Column(Integer)
    operate_name = Column(String(125, u'utf8mb4_bin'))
    total_order_code = Column(String(255, u'utf8mb4_bin'))
    common_data = Column(String(255, u'utf8mb4_bin'))
    backups_data = Column(String(255, u'utf8mb4_bin'))
    discount_price = Column(Float(12, True), server_default=text("'0.00'"))
    qr_code = Column(String(255, u'utf8mb4_bin'))
    salesman_id = Column(Integer)
    salesman_name = Column(String(32, u'utf8mb4_bin'))


class SysBarCode(Base):
    __tablename__ = 'sys_bar_code'

    id = Column(Integer, primary_key=True)
    code = Column(String(25, u'utf8_bin'))
    state = Column(Integer, server_default=text("'1'"))
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    remarks = Column(String(255, u'utf8_bin'))
    type = Column(Integer, server_default=text("'0'"))
    sure_time = Column(DateTime)


class SysBilllogsRecord(Base):
    __tablename__ = 'sys_billlogs_record'

    id = Column(Integer, primary_key=True)
    order_code = Column(String(125, u'utf8mb4_bin'))
    operate_id = Column(Integer)
    operate_name = Column(String(125, u'utf8mb4_bin'))
    create_at = Column(DateTime)
    pay_code = Column(String(125, u'utf8mb4_bin'))
    sell_money = Column(Float(12, True))
    state = Column(Integer, server_default=text("'1'"))
    club_id = Column(String(125, u'utf8mb4_bin'))
    bill_date = Column(DateTime)


class SysBusPicture(Base):
    __tablename__ = 'sys_bus_picture'

    sid = Column(Integer, primary_key=True)
    type = Column(String(255, u'utf8_bin'), nullable=False)
    customer_id = Column(String(50, u'utf8_bin'))
    icon_url = Column(String(125, u'utf8_bin'))
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    remarks = Column(String(125, u'utf8_bin'))


class SysClubLogin(Base):
    __tablename__ = 'sys_club_login'

    id = Column(Integer, primary_key=True)
    username = Column(String(125, u'utf8_bin'))
    password = Column(String(125, u'utf8_bin'))
    club_id = Column(Integer)
    remarks = Column(String(255, u'utf8_bin'))
    create_at = Column(DateTime)
    update_at = Column(DateTime)


class SysIconUrl(Base):
    __tablename__ = 'sys_icon_url'

    id = Column(Integer, primary_key=True)
    icon_url = Column(String(255, u'utf8_bin'))
    connection_id = Column(Integer)
    declares = Column(String(255, u'utf8_bin'))
    remarks = Column(String(125, u'utf8_bin'))
    belongs = Column(String(64, u'utf8_bin'))


class SysInfo(Base):
    __tablename__ = 'sys_info'

    id = Column(Integer, primary_key=True)
    scode = Column(String(30, u'utf8_bin'))
    sname = Column(String(100, u'utf8_bin'))
    svalue = Column(String(100, u'utf8_bin'))
    bak = Column(String(100, u'utf8_bin'))
    stype = Column(String(100, u'utf8_bin'))
    club_id = Column(String(125, u'utf8mb4_bin'))


class SysMessageInfo(Base):
    __tablename__ = 'sys_message_info'

    id = Column(Integer, primary_key=True)
    phone = Column(String(65, u'utf8mb4_bin'))
    type = Column(Integer)
    create_at = Column(DateTime)
    state = Column(Integer, server_default=text("'1'"))
    update_at = Column(DateTime)
    order_code = Column(String(125, u'utf8mb4_bin'))


class SysMsgInfo(Base):
    __tablename__ = 'sys_msg_info'

    id = Column(Integer, primary_key=True)
    phone = Column(String(25, u'utf8_bin'))
    vertify = Column(String(25, u'utf8_bin'))
    create_at = Column(DateTime)
    updat_at = Column(DateTime)
    remarks = Column(String(255, u'utf8_bin'))
    type = Column(Integer)


class SysOperateRecord(Base):
    __tablename__ = 'sys_operate_record'

    id = Column(Integer, primary_key=True)
    operate_type = Column(Integer)
    opertae_id = Column(Integer)
    operate_name = Column(String(125, u'utf8mb4_bin'))
    ip = Column(String(125, u'utf8mb4_bin'))
    create_at = Column(DateTime)
    club_id = Column(String(126, u'utf8mb4_bin'))
    operate_detail = Column(String(255, u'utf8mb4_bin'))
    operate_type_name = Column(String(255, u'utf8mb4_bin'))
    super_type = Column(Integer)
    super_type_name = Column(String(255, u'utf8mb4_bin'))


class SysOrganization(Base):
    __tablename__ = 'sys_organization'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    parent_id = Column(BigInteger)
    parent_ids = Column(String(100))
    available = Column(Integer, server_default=text("'0'"))
    wh_id = Column(Integer)
    club_id = Column(String(125, u'utf8mb4_bin'))


class SysResource(Base):
    __tablename__ = 'sys_resource'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    type = Column(String(50))
    url = Column(String(200))
    parent_id = Column(BigInteger)
    parent_ids = Column(String(100))
    permission = Column(String(100))
    available = Column(Integer, server_default=text("'0'"))


class SysRole(Base):
    __tablename__ = 'sys_role'

    id = Column(BigInteger, primary_key=True)
    role = Column(String(100))
    description = Column(String(100))
    resource_ids = Column(String(255))
    available = Column(Integer, server_default=text("'0'"))
    club_id = Column(String(125, u'utf8mb4_bin'))


class SysTotalInfo(Base):
    __tablename__ = 'sys_total_info'

    id = Column(Integer, primary_key=True)
    code = Column(String(125, u'utf8_bin'))
    name = Column(String(125, u'utf8_bin'))
    type = Column(String(125, u'utf8_bin'))
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    remarks = Column(String(255, u'utf8_bin'))


class SysUser(Base):
    __tablename__ = 'sys_user'

    id = Column(BigInteger, primary_key=True)
    organization_id = Column(BigInteger)
    username = Column(String(100))
    password = Column(String(100))
    salt = Column(String(100))
    role_ids = Column(String(100))
    locked = Column(Integer, server_default=text("'0'"))
    phone = Column(Integer)
    is_weixin = Column(Integer, server_default=text("'0'"))
    discourt = Column(Float, server_default=text("'1'"))
    open_id = Column(String(64))
    ware_house = Column(Integer)
    club_id = Column(String(125, u'utf8mb4_bin'))
    is_saleman = Column(Integer)
    name = Column(String(45, u'utf8mb4_bin'))
    is_available = Column(Integer)


class TempCourtRate(Base):
    __tablename__ = 'temp_court_rate'

    id = Column(Integer, primary_key=True)
    create_at = Column(DateTime)
    rate = Column(Float(12, True))
    court_type_id = Column(Integer)
    sport_type = Column(String(255, u'utf8mb4_bin'))
    club_id = Column(String(125, u'utf8mb4_bin'))


class TempDoorManager(Base):
    __tablename__ = 'temp_door_manager'

    code = Column(String(50, u'utf8mb4_bin'))
    id = Column(Integer, primary_key=True)
    inn = Column(Integer, server_default=text("'0'"))
    outt = Column(Integer, server_default=text("'0'"))


class TempLightManager(Base):
    __tablename__ = 'temp_light_manager'

    id = Column(Integer, primary_key=True)
    code = Column(String(50, u'utf8mb4_bin'))
    sport_type = Column(String(50, u'utf8mb4_bin'))


class TicketCard(Base):
    __tablename__ = 'ticket_card'

    id = Column(Integer, primary_key=True)
    card_nub = Column(String(100, u'utf8mb4_bin'))
    phy_num = Column(String(100, u'utf8mb4_bin'))
    status = Column(Integer, server_default=text("'1'"))
    enter_gate = Column(Integer, server_default=text("'0'"))
    outer_gate = Column(Integer, server_default=text("'0'"))
    create_at = Column(DateTime)
    type = Column(String(100, u'utf8mb4_bin'))
    club_id = Column(String(100, u'utf8mb4_bin'))


class TicketCardReader(Base):
    __tablename__ = 'ticket_card_reader'

    id = Column(Integer, primary_key=True)
    read_num = Column(String(255, u'utf8mb4_bin'))
    work = Column(Integer)
    in_out = Column(Integer, server_default=text("'0'"))
    out_reader = Column(Integer, server_default=text("'0'"))
    has_catch = Column(Integer)
    gate_id = Column(Integer)
    club_id = Column(String(125, u'utf8mb4_bin'))
    read_type = Column(Enum(u'ALL', u'CARD', u'MEMBER', u'QRCODE', u''), server_default=text("'ALL'"))
    relay = Column(Integer, server_default=text("'1'"))


class TicketCardStyle(Base):
    __tablename__ = 'ticket_card_style'

    id = Column(Integer, primary_key=True)
    code = Column(String(100, u'utf8mb4_bin'))
    name = Column(String(255, u'utf8mb4_bin'))
    club_id = Column(String(100, u'utf8mb4_bin'))
    is_manager = Column(Integer, server_default=text("'0'"))
    is_locker = Column(Integer)
    is_watercontrol = Column(Integer)
    is_accesscontrol = Column(Integer)


class TicketEquipRecord(Base):
    __tablename__ = 'ticket_equip_record'

    id = Column(Integer, primary_key=True)
    equip_name = Column(String(125, u'utf8mb4_bin'))
    op_tion = Column(Integer)
    ticket_id = Column(Integer)
    phy_num = Column(String(125, u'utf8mb4_bin'))
    create_at = Column(Date)
    card_id = Column(Integer)
    operate_id = Column(Integer)
    operate_name = Column(String(125, u'utf8mb4_bin'))
    club_id = Column(String(125, u'utf8mb4_bin'))


class TicketGate(Base):
    __tablename__ = 'ticket_gate'

    id = Column(Integer, primary_key=True)
    gate_name = Column(String(125, u'utf8mb4_bin'))
    gate_serial = Column(String(125, u'utf8mb4_bin'))
    ip_address = Column(String(125, u'utf8mb4_bin'))
    state = Column(Integer, server_default=text("'1'"))
    club_id = Column(String(125, u'utf8mb4_bin'))
    sex = Column(Enum(u'female', u'male'))


class TicketGateRecord(Base):
    __tablename__ = 'ticket_gate_record'

    id = Column(Integer, primary_key=True)
    card_id = Column(Integer)
    ticket_id = Column(Integer)
    op_tion = Column(Integer)
    state = Column(String(125, u'utf8mb4_bin'))
    phy_num = Column(String(125, u'utf8mb4_bin'))
    ticket_name = Column(String(125, u'utf8mb4_bin'))
    create_at = Column(Date)
    gate_name = Column(String(125, u'utf8mb4_bin'))
    club_id = Column(String(125, u'utf8mb4_bin'))


class TicketGateSet(Base):
    __tablename__ = 'ticket_gate_set'

    id = Column(Integer, primary_key=True)
    gate_id = Column(Integer)
    ticket_id = Column(Integer)


class TicketNuberInfo(Base):
    __tablename__ = 'ticket_nuber_info'

    id = Column(Integer, primary_key=True)
    create_at = Column(Date)
    in_number = Column(Integer, server_default=text("'0'"))
    out_number = Column(Integer, server_default=text("'0'"))
    club_id = Column(String(125, u'utf8mb4_bin'))


class TicketOperateInfo(Base):
    __tablename__ = 'ticket_operate_info'

    id = Column(Integer, primary_key=True)
    operate_type = Column(Enum(u'frontdesk', u'aio', u'qrcode', u'card', u'member'))
    gate_serial = Column(String(125, u'utf8mb4_bin'))
    detail_id = Column(Integer)
    gate_type = Column(Enum(u'out', u'in'), server_default=text("'in'"))
    card_nub = Column(String(125, u'utf8mb4_bin'))
    club_id = Column(String(255, u'utf8mb4_bin'))
    create_at = Column(DateTime)
    sex = Column(String(125, u'utf8mb4_bin'))
    card_type_name = Column(String(125, u'utf8mb4_bin'))
    ticket_name = Column(String(125, u'utf8mb4_bin'))
    mc_code = Column(String(125, u'utf8mb4_bin'))
    member_name = Column(String(125, u'utf8mb4_bin'))


class TicketRealTimeInfo(Base):
    __tablename__ = 'ticket_real_time_info'

    id = Column(Integer, primary_key=True)
    outer_gate = Column(Integer, server_default=text("'0'"))
    enter_gate = Column(Integer, server_default=text("'0'"))
    inner_time = Column(DateTime)
    outter_time = Column(DateTime)
    replace_time = Column(Integer, server_default=text("'0'"))
    card_nub = Column(String(125, u'utf8mb4_bin'))
    club_id = Column(String(125, u'utf8mb4_bin'))
    create_at = Column(Date)


class TicketRealTimeInfoCard(Base):
    __tablename__ = 'ticket_real_time_info_card'

    id = Column(Integer, primary_key=True)
    outer_gate = Column(Integer, server_default=text("'0'"))
    enter_gate = Column(Integer, server_default=text("'0'"))
    inner_time = Column(DateTime)
    outter_time = Column(DateTime)
    replace_time = Column(Integer, server_default=text("'0'"))
    card_nub = Column(String(125, u'utf8mb4_bin'))
    club_id = Column(String(125, u'utf8mb4_bin'))
    create_at = Column(Date)


class TicketSellCard(Base):
    __tablename__ = 'ticket_sell_card'

    ticket__id = Column(Integer)
    id = Column(Integer, primary_key=True)
    phy_num = Column(String(125, u'utf8mb4_bin'))
    create_at = Column(DateTime)
    club_id = Column(String(125, u'utf8mb4_bin'))
    card_nub = Column(String(125, u'utf8mb4_bin'))
    card_id = Column(Integer)
    mc_code = Column(String(125, u'utf8mb4_bin'))
    card_type_name = Column(String(125, u'utf8mb4_bin'))


class TicketSellCardInfo(Base):
    __tablename__ = 'ticket_sell_card_info'

    id = Column(Integer, primary_key=True)
    create_at = Column(DateTime)
    club_id = Column(String(125, u'utf8mb4_bin'))
    mc_code = Column(String(125, u'utf8mb4_bin'))
    card_type_name = Column(String(125, u'utf8mb4_bin'))
    consume_style_name = Column(String(125, u'utf8mb4_bin'))
    ticket_name = Column(String(125, u'utf8mb4_bin'))
    consume_overtime_style = Column(String(125, u'utf8mb4_bin'))
    start_time = Column(String(125, u'utf8mb4_bin'))
    end_time = Column(String(125, u'utf8mb4_bin'))
    buffer_time = Column(String(125, u'utf8mb4_bin'))
    minutes = Column(Integer)
    charge = Column(Float(12, True))
    card_nub = Column(String(125, u'utf8mb4_bin'))
    start_time_style = Column(String(125, u'utf8mb4_bin'))
    end_time_style = Column(String(125, u'utf8mb4_bin'))
    validate_minutes = Column(Integer, server_default=text("'0'"))
    is_clean = Column(String(125, u'utf8mb4_bin'))
    detail_id = Column(Integer)
    qr_code = Column(String(125, u'utf8mb4_bin'))
    ticket_id = Column(Integer)
    gate_serial = Column(String(255, u'utf8mb4_bin'))


class TimeoutEquip(Base):
    __tablename__ = 'timeout_equip'

    id = Column(Integer, primary_key=True)
    code = Column(String(50, u'utf8mb4_bin'))
    name = Column(String(50, u'utf8mb4_bin'))
    deposit = Column(Float(50, True))
    rent = Column(Float(50, True))
    isrequire_return = Column(Integer, server_default=text("'1'"))
    type = Column(Enum(u'SKATE'), server_default=text("'SKATE'"))
    time_equip = Column(Integer, server_default=text("'0'"))
    club_id = Column(String(125, u'utf8mb4_bin'))
    much_lead = Column(Integer, server_default=text("'0'"))


class TimeoutSchema(Base):
    __tablename__ = 'timeout_schema'

    id = Column(Integer, primary_key=True)
    name = Column(String(50, u'utf8mb4_bin'))
    consume_style_name = Column(Enum(u'ONECE', u'AVALUE_DATE', u'BUTTON_AGAIN', u'AVALUE_COURT'), server_default=text("'ONECE'"))
    start_time = Column(Enum(u'STARTBY__BUY', u'STARTBY_EQUIP', u'STARTBY_MECHINE'), server_default=text("'STARTBY_MECHINE'"))
    end_time = Column(Enum(u'ENDBY_EQUIP', u'ENDBY_TICKET', u'ENDBY_MECHINE'), server_default=text("'ENDBY_MECHINE'"))
    buffer_time = Column(Integer, server_default=text("'0'"))
    minutes = Column(Integer)
    charge = Column(Float(11, True))
    club_id = Column(String(125, u'utf8mb4_bin'))


class TimeoutTkEquip(Base):
    __tablename__ = 'timeout_tk_equip'

    id = Column(Integer, primary_key=True)
    tktype_id = Column(Integer)
    equip_id = Column(Integer)


class TkTicketItem(Base):
    __tablename__ = 'tk_ticket_item'

    id = Column(Integer, primary_key=True)
    item_name = Column(String(50, u'utf8_bin'), nullable=False, server_default=text("''"))
    update_time = Column(DateTime)
    sport_type = Column(String(120, u'utf8_bin'), nullable=False, server_default=text("''"))
    available = Column(Integer, nullable=False, server_default=text("'1'"))
    club_id = Column(String(125, u'utf8mb4_bin'))
    validate_hand = Column(Integer, server_default=text("'0'"))


class TkTicketPriceSet(Base):
    __tablename__ = 'tk_ticket_price_set'

    id = Column(Integer, primary_key=True)
    ticket_type_id = Column(Integer)
    ticket_overtime_style = Column(Enum(u'HALF_HOUR_TIME', u'REAL_TIME', u'ONE_HOUR_TIME'))
    priceday = Column(Float(12, True))
    day_type = Column(String(12, u'utf8_bin'), server_default=text("''"))
    net_priceday = Column(Float(12, True), server_default=text("'0.00'"))
    club_id = Column(String(125, u'utf8mb4_bin'))


class TkTicketType(Base):
    __tablename__ = 'tk_ticket_type'

    id = Column(Integer, primary_key=True)
    ticket_number = Column(String(125, u'utf8_bin'), nullable=False)
    ticket_name = Column(String(20, u'utf8_bin'), nullable=False)
    consume_style_name = Column(Enum(u'AVALUE_COURT', u'BUTTON_AGAIN', u'AVALUE_DATE', u'ONECE'))
    consume_overtime_style = Column(Enum(u'BY_INTO_MECHINE', u'BY_COURT', u'BY_EQUPIMENT', u'BY_BUY'))
    varliable = Column(Integer, server_default=text("'1'"))
    validate_minutes = Column(Integer)
    value_view = Column(Integer, server_default=text("'1'"))
    memeber_value = Column(Integer, server_default=text("'1'"))
    ticket_kind = Column(Enum(u'SPECCAL', u'ACTIVE', u'ORDINARY'), server_default=text("'ACTIVE'"))
    ticket_item_id = Column(Integer)
    is_del = Column(Integer, nullable=False, server_default=text("'0'"))
    is_net = Column(Integer, server_default=text("'0'"))
    start_time = Column(String(11, u'utf8mb4_bin'))
    end_time = Column(String(11, u'utf8mb4_bin'))
    timeout_id = Column(Integer)
    club_id = Column(String(125, u'utf8mb4_bin'))


class TrainCoach(Base):
    __tablename__ = 'train_coach'

    level = Column(String(125, u'utf8mb4_bin'))
    name = Column(String(125, u'utf8mb4_bin'))
    id = Column(Integer, primary_key=True)
    phone = Column(String(125, u'utf8mb4_bin'))
    introduction = Column(MEDIUMBLOB)
    sex = Column(Integer, server_default=text("'0'"))
    icon = Column(String(125, u'utf8mb4_bin'))
    club_id = Column(String(125, u'utf8mb4_bin'))


class TytgRecord(Base):
    __tablename__ = 'tytg_record'

    id = Column(Integer, primary_key=True)
    mc_code = Column(String(30, u'utf8mb4_bin'))
    member_name = Column(String(30, u'utf8mb4_bin'))
    sell_money = Column(Float(10, True), server_default=text("'0.00'"))
    left_money = Column(Float(10, True), server_default=text("'0.00'"))
    num = Column(Integer, server_default=text("'0'"))
    left_num = Column(Integer, server_default=text("'0'"))
    creat_at = Column(Date)
    operate_type_name = Column(String(100, u'utf8mb4_bin'))
    club_id = Column(String(125, u'utf8mb4_bin'))
    super_code = Column(String(10, u'utf8mb4_bin'))
    order_code = Column(String(30, u'utf8mb4_bin'))
    pay_code = Column(String(10, u'utf8mb4_bin'))
    total_money = Column(Float(10, True), server_default=text("'0.00'"))
    unit_money = Column(Float(10, True), server_default=text("'0.00'"))
    common_data = Column(String(100, u'utf8mb4_bin'))
    member_id = Column(Integer)


class WarehouseSet(Base):
    __tablename__ = 'warehouse_set'

    id = Column(Integer, primary_key=True)
    warehouse_code = Column(String(50))
    warehouse_name = Column(String(50))
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    bar = Column(String(255))
    club_id = Column(String(125, u'utf8mb4_bin'))


class WarehouseStock(Base):
    __tablename__ = 'warehouse_stock'

    id = Column(Integer, primary_key=True)
    wh_id = Column(Integer)
    in_stock = Column(Integer)
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    bar = Column(String(255, u'utf8_bin'))
    goods_id = Column(Integer)
    club_id = Column(String(125, u'utf8mb4_bin'))


class WeixinCert(Base):
    __tablename__ = 'weixin_cert'

    id = Column(Integer, primary_key=True)
    name = Column(String(125, u'utf8_bin'))
    value = Column(MEDIUMBLOB)
    club_id = Column(String(125, u'utf8mb4_bin'))


class WeixinUser(Base):
    __tablename__ = 'weixin_user'

    id = Column(Integer, primary_key=True)
    subscribe = Column(Integer)
    nickname = Column(String(32, u'utf8_bin'))
    open_id = Column(String(64, u'utf8_bin'))
    sex = Column(String(6, u'utf8_bin'))
    city = Column(String(125, u'utf8_bin'))
    province = Column(String(125, u'utf8_bin'))
    country = Column(String(125, u'utf8_bin'))
    headimgurl = Column(String(256, u'utf8_bin'))
    unionid = Column(String(64, u'utf8_bin'))
    sex_id = Column(Integer)
    subscribe_time = Column(BigInteger)


class WxBaseInfo(Base):
    __tablename__ = 'wx_base_info'

    id = Column(Integer, primary_key=True)
    app_id = Column(String(255, u'utf8_bin'))
    secret = Column(String(255, u'utf8_bin'))
    text_welcome = Column(String(255, u'utf8_bin'))
    base_url = Column(String(255, u'utf8_bin'))
    redirect_url = Column(String(255, u'utf8_bin'))
    mch_id = Column(String(255, u'utf8_bin'))
    active_redirect_url = Column(String(255, u'utf8mb4_bin'))
    club_id = Column(String(128, u'utf8mb4_bin'))


class YdsClientApplicateInfo(Base):
    __tablename__ = 'yds_client_applicate_info'

    id = Column(Integer, primary_key=True)
    club_name = Column(String(125, u'utf8mb4_bin'))
    applicant_name = Column(String(125, u'utf8mb4_bin'))
    applicant_phone = Column(String(125, u'utf8mb4_bin'))
    applicant_date = Column(DateTime)
    applicant_info = Column(MEDIUMBLOB)
    handle_progress = Column(Integer, server_default=text("'0'"))


class YdsRecharge(Base):
    __tablename__ = 'yds_recharge'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    bill_money = Column(Float(11, True))
    sell_money = Column(Float(11, True))
    startdate = Column(Date)
    enddate = Column(Date)
    remark = Column(String(100))
    free_money = Column(Float(11, True))
    create_at = Column(DateTime)
    club_id = Column(String(125, u'utf8mb4_bin'))
    state = Column(Integer, server_default=text("'1'"))


class YdsRechargeRecord(Base):
    __tablename__ = 'yds_recharge_record'

    id = Column(Integer, primary_key=True)
    yds_id = Column(Integer)
    mem_id = Column(Integer)
    create_at = Column(Date)
    bill_money = Column(Float(12, True))
    sell_money = Column(Float(12, True))
    free_money = Column(Float(12, True))
    remark = Column(String(125, u'utf8mb4_bin'))


class YdsReportShow(Base):
    __tablename__ = 'yds_report_show'

    id = Column(Integer, primary_key=True)
    value = Column(String(20, u'utf8mb4_bin'))
    name = Column(String(20, u'utf8mb4_bin'))
    code = Column(String(20, u'utf8mb4_bin'))
    report_type = Column(String(20, u'utf8mb4_bin'))
    date_type = Column(String(20, u'utf8mb4_bin'), server_default=text("'1'"))
    club_id = Column(String(125, u'utf8mb4_bin'))
