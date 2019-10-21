
class RawMSG(object):
    __slots__ = ["key", "value"]

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value


class CMP(object):

    __slots__ = ["pts", "rec_type", "company_name", "cik", "status", "industry_id",
                 "sp_rating", "founding_date", "addr_line1", "addr_line2", "postal_code",
                 "city", "state_province", "country", "ceo_name"]

    def __init__(self, pts=None, rec_type=None, company_name=None, cik=None, status=None, industry_id=None,
                 sp_rating=None, founding_date=None, addr_line1=None, addr_line2=None,  postal_code=None,
                 city=None, state_province=None, country=None, ceo_name=None):
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
    __slots__ = ["pts", "rec_type", "symbol", "issue_type", "status", "name", "ex_id", "shares_out",
                 "first_trade_date", "first_trade_exchange", "dividend", "company_name"]

    def __init__(self, pts=None, rec_type=None, symbol=None, issue_type=None, status=None, name=None, ex_id=None, shares_out=None,
                 first_trade_date=None, first_trade_exchange=None, dividend=None, company_name=None):
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
    __slots__ = ["pts", "rec_type", "year", "quarter", "qtr_start_date", "posting_date",
                 "revenue", "earnings", "eps", "diluted_eps", "margin", "inventory", "assets",
                 "liabilities", "sh_out", "diluted_sh_out", "co_name_or_cik"]

    def __init__(self, pts=None, rec_type=None, year=None, quarter=None, qtr_start_date=None, posting_date=None,
                 revenue=None, earnings=None, eps=None, diluted_eps=None, margin=None, inventory=None, assets=None,
                 liabilities=None, sh_out=None, diluted_sh_out=None, co_name_or_cik=None):
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
    __slots__ = ["cdc_flag", "cdc_dsn", "ca_id", "ca_b_id", "ca_c_id", "ca_name", "ca_tax_st", "ca_st_id"]

    def __init__(self, cdc_flag, cdc_dsn, ca_id, ca_b_id, ca_c_id, ca_name, ca_tax_st, ca_st_id):
        self.ca_b_id = ca_b_id
        self.ca_c_id = ca_c_id
        self.cdc_dsn = cdc_dsn
        self.ca_id = ca_id
        self.