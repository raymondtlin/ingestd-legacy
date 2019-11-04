class RawMSG(object):
    __slots__ = ["key", "value"]

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value


class CMP(object):

    __slots__ = [
        "pts", "rec_type", "company_name", "cik", "status", "industry_id",
        "sp_rating", "founding_date", "addr_line1", "addr_line2",
        "postal_code", "city", "state_province", "country", "ceo_name"
    ]

    def __init__(self,
                 pts=None,
                 rec_type=None,
                 company_name=None,
                 cik=None,
                 status=None,
                 industry_id=None,
                 sp_rating=None,
                 founding_date=None,
                 addr_line1=None,
                 addr_line2=None,
                 postal_code=None,
                 city=None,
                 state_province=None,
                 country=None,
                 ceo_name=None):
        self.pts = pts
        self.rec_type = rec_type
        self.company_name = company_name
        self.cik = cik
        self.status = status
        self.industry_id = industry_id
        self.sp_rating = sp_rating
        self.founding_date = founding_date
        self.addr_line1 = addr_line1
        self.addr_line2 = addr_line2
        self.postal_code = postal_code
        self.city = city
        self.state_province = state_province
        self.country = country
        self.ceo_name = ceo_name


class SEC(object):
    __slots__ = [
        "pts", "rec_type", "symbol", "issue_type", "status", "name", "ex_id",
        "shares_out", "first_trade_date", "first_trade_exchange", "dividend",
        "company_name"
    ]

    def __init__(self,
                 pts=None,
                 rec_type=None,
                 symbol=None,
                 issue_type=None,
                 status=None,
                 name=None,
                 ex_id=None,
                 shares_out=None,
                 first_trade_date=None,
                 first_trade_exchange=None,
                 dividend=None,
                 company_name=None):
        self.pts = pts
        self.rec_type = rec_type
        self.symbol = symbol
        self.issue_type = issue_type
        self.status = status
        self.name = name
        self.ex_id = ex_id
        self.shares_out = shares_out
        self.first_trade_date = first_trade_date
        self.first_trade_exchange = first_trade_exchange
        self.dividend = dividend
        self.company_name = company_name


class FIN(object):
    __slots__ = [
        "pts", "rec_type", "year", "quarter", "qtr_start_date", "posting_date",
        "revenue", "earnings", "eps", "diluted_eps", "margin", "inventory",
        "assets", "liabilities", "sh_out", "diluted_sh_out", "co_name_or_cik"
    ]

    def __init__(self,
                 pts=None,
                 rec_type=None,
                 year=None,
                 quarter=None,
                 qtr_start_date=None,
                 posting_date=None,
                 revenue=None,
                 earnings=None,
                 eps=None,
                 diluted_eps=None,
                 margin=None,
                 inventory=None,
                 assets=None,
                 liabilities=None,
                 sh_out=None,
                 diluted_sh_out=None,
                 co_name_or_cik=None):
        self.pts = pts
        self.rec_type = rec_type
        self.year = year
        self.quarter = quarter
        self.qtr_start_date = qtr_start_date
        self.posting_date = posting_date
        self.revenue = revenue
        self.earnings = earnings
        self.eps = eps
        self.diluted_eps = diluted_eps
        self.margin = margin
        self.inventory = inventory
        self.assets = assets
        self.liabilities = liabilities
        self.sh_out = sh_out
        self.diluted_sh_out = diluted_sh_out
        self.co_name_or_cik = co_name_or_cik


class Acct(object):
    __slots__ = [
        "cdc_flag", "cdc_dsn", "ca_id", "ca_b_id", "ca_c_id", "ca_name",
        "ca_tax_st", "ca_st_id"
    ]

    def __init__(self,
                 cdc_flag=None,
                 cdc_dsn=None,
                 ca_id=None,
                 ca_b_id=None,
                 ca_c_id=None,
                 ca_name=None,
                 ca_tax_st=None,
                 ca_st_id=None):
        self.ca_b_id = ca_b_id
        self.ca_c_id = ca_c_id
        self.cdc_dsn = cdc_dsn
        self.ca_id = ca_id
        self.ca_name = ca_name
        self.ca_tax_st = ca_tax_st
        self.ca_st_id = ca_st_id


class Customer(object):
    __slots__ = [
        "C_ID", "C_TAX_ID", "C_ST_ID", "C_L_NAME", "C_F_NAME", "C_M_NAME",
        "C_GNDR", "C_TIER", "C_DOB", "C_ADLINE1", "C_ADLINE2", "C_ZIPCODE",
        "C_CITY", "C_STATE_PROV", "C_CTRY", "C_CTRY_1", "C_AREA_1",
        "C_LOCAL_1", "C_EXT_1", "C_CTRY_2", "C_AREA_2", "C_LOCAL_2", "C_EXT_2",
        "C_CTRY_3", "C_AREA_3", "C_LOCAL_3", "C_EXT_3", "C_EMAIL_1",
        "C_EMAIL_3", "C_LCL_TX_ID", "C_NAT_TX_ID"
    ]

    def __init__(self,
                 C_ID,
                 C_TAX_ID=None,
                 C_ST_ID=None,
                 C_L_NAME=None,
                 C_F_NAME=None,
                 C_M_NAME=None,
                 C_GNDR=None,
                 C_TIER=None,
                 C_DOB=None,
                 C_ADLINE1=None,
                 C_ADLINE2=None,
                 C_ZIPCODE=None,
                 C_CITY=None,
                 C_STATE_PROV=None,
                 C_CTRY=None,
                 C_CTRY_1=None,
                 C_AREA_1=None,
                 C_LOCAL_1=None,
                 C_EXT_1=None,
                 C_CTRY_2=None,
                 C_AREA_2=None,
                 C_LOCAL_2=None,
                 C_EXT_2=None,
                 C_CTRY_3=None,
                 C_AREA_3=None,
                 C_LOCAL_3=None,
                 C_EXT_3=None,
                 C_EMAIL_1=None,
                 C_EMAIL_3=None,
                 C_LCL_TX_ID=None,
                 C_NAT_TX_ID=None):
        self.C_ID = C_ID,
        self.C_TAX_ID = C_TAX_ID,
        self.C_ST_ID = C_ST_ID,
        self.C_L_NAME = C_L_NAME,
        self.C_F_NAME = C_F_NAME,
        self.C_M_NAME = C_M_NAME,
        self.C_GNDR = C_GNDR,
        self.C_TIER = C_TIER,
        self.C_DOB = C_DOB,
        self.C_ADLINE1 = C_ADLINE1,
        self.C_ADLINE2 = C_ADLINE2,
        self.C_ZIPCODE = C_ZIPCODE,
        self.C_CITY = C_CITY,
        self.C_STATE_PROV = C_STATE_PROV,
        self.C_CTRY = C_CTRY,
        self.C_CTRY_1 = C_CTRY_1,
        self.C_AREA_1 = C_AREA_1,
        self.C_LOCAL_1 = C_LOCAL_1,
        self.C_EXT_1 = C_EXT_1,
        self.C_CTRY_2 = C_CTRY_2,
        self.C_AREA_2 = C_AREA_2,
        self.C_LOCAL_2 = C_LOCAL_2,
        self.C_EXT_2 = C_EXT_2,
        self.C_CTRY_3 = C_CTRY_3,
        self.C_AREA_3 = C_AREA_3,
        self.C_LOCAL_3 = C_LOCAL_3,
        self.C_EXT_3 = C_EXT_3,
        self.C_EMAIL_1 = C_EMAIL_1,
        self.C_EMAIL_3 = C_EMAIL_3,
        self.C_LCL_TX_ID = C_LCL_TX_ID,
        self.C_NAT_TX_ID = C_NAT_TX_ID


class Prospect(object):
    __slots__ = [
        "AGENCYID", "LASTNAME", "FIRSTNAME", "MIDDLEINITIAL", "GENDER",
        "ADDRESSLINE1", "ADDRESSLINE2", "POSTALCODE", "CITY", "STATE",
        "COUNTRY", "PHONE", "INCOME", "NUMBERCARS", "NUMBERCHILDREN",
        "MARITALSTATUS", "AGE", "CREDITRATING", "OWNORRENTFLAG", "EMPLOYER",
        "NUMBERCREDITCARDS", "NETWORTH"
    ]

    def __init__(self,
                 AGENCYID=None,
                 LASTNAME=None,
                 FIRSTNAME=None,
                 MIDDLEINITIAL=None,
                 GENDER=None,
                 ADDRESSLINE1=None,
                 ADDRESSLINE2=None,
                 POSTALCODE=None,
                 CITY=None,
                 STATE=None,
                 COUNTRY=None,
                 PHONE=None,
                 INCOME=None,
                 NUMBERCARS=None,
                 NUMBERCHILDREN=None,
                 MARITALSTATUS=None,
                 AGE=None,
                 CREDITRATING=None,
                 OWNORRENTFLAG=None,
                 EMPLOYER=None,
                 NUMBERCREDITCARDS=None,
                 NETWORTH=None):
        self.AGENCYID = AGENCYID
        self.LASTNAME = LASTNAME
        self.FIRSTNAME = FIRSTNAME
        self.MIDDLEINITIAL = MIDDLEINITIAL
        self.GENDER = GENDER
        self.ADDRESSLINE1 = ADDRESSLINE1
        self.ADDRESSLINE2 = ADDRESSLINE2
        self.POSTALCODE = POSTALCODE
        self.CITY = CITY
        self.STATE = STATE
        self.COUNTRY = COUNTRY
        self.PHONE = PHONE
        self.INCOME = INCOME
        self.NUMBERCARS = NUMBERCARS
        self.NUMBERCHILDREN = NUMBERCHILDREN
        self.MARITALSTATUS = MARITALSTATUS
        self.AGE = AGE
        self.CREDITRATING = CREDITRATING
        self.OWNORRENTFLAG = OWNORRENTFLAG
        self.EMPLOYER = EMPLOYER
        self.NUMBERCREDITCARDS = NUMBERCREDITCARDS
        self.NETWORTH = NETWORTH
