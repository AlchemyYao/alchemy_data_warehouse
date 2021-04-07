from django.db import models

# Create your models here.
class TushareStockBasic(models.Model):
    class Meta:
        #managed = False
        db_table = 'tushare_stock_basic'
    id      = models.CharField(max_length=100,primary_key=True)
    ts_code = models.CharField(max_length=100,null=True,blank=True)
    symbol	= models.CharField(max_length=100,null=True,blank=True)
    name	= models.CharField(max_length=100,null=True,blank=True)
    area	= models.CharField(max_length=100,null=True,blank=True)
    industry	= models.CharField(max_length=100,null=True,blank=True)
    fullname	= models.CharField(max_length=500,null=True,blank=True)
    enname	= models.CharField(max_length=500,null=True,blank=True)
    market	= models.CharField(max_length=100,null=True,blank=True)
    exchange	= models.CharField(max_length=100,null=True,blank=True)
    curr_type	= models.CharField(max_length=100,null=True,blank=True)
    list_status	= models.CharField(max_length=100,null=True,blank=True)
    list_date	= models.CharField(max_length=100,null=True,blank=True)
    delist_date	= models.CharField(max_length=100,null=True,blank=True)
    is_hs	= models.CharField(max_length=100,null=True,blank=True)

class TushareTradeCal(models.Model):
    class Meta:
        #managed = False
        db_table = 'tushare_trade_cal'
    id        = models.CharField(max_length=100,primary_key=True)
    exchange  = models.CharField(max_length=100,null=True,blank=True)
    cal_date  = models.CharField(max_length=100,null=True,blank=True)
    is_open	  = models.CharField(max_length=100,null=True,blank=True)
    pretrade_date	= models.CharField(max_length=100,null=True,blank=True)

class TushareNameChange(models.Model):
    class Meta:
        #managed = False
        db_table = 'tushare_name_change'
    id        = models.CharField(max_length=100,primary_key=True)
    ts_code   = models.CharField(max_length=100,null=True,blank=True)
    name      = models.CharField(max_length=100,null=True,blank=True)
    start_date	  = models.CharField(max_length=100,null=True,blank=True)
    end_date	  = models.CharField(max_length=100,null=True,blank=True)
    ann_date	  = models.CharField(max_length=100,null=True,blank=True)
    change_reason = models.CharField(max_length=500,null=True,blank=True)

class TushareDaily(models.Model):
    class Meta:
        #managed = False
        db_table = 'tushare_daily'
    id        = models.CharField(max_length=100,primary_key=True)
    ts_code	  = models.CharField(max_length=100,null=True,blank=True)
    trade_date	= models.CharField(max_length=100,null=True,blank=True)
    open	= models.CharField(max_length=100,null=True,blank=True)
    high	= models.CharField(max_length=100,null=True,blank=True)
    low	    = models.CharField(max_length=100,null=True,blank=True)
    close	= models.CharField(max_length=100,null=True,blank=True)
    pre_close	= models.CharField(max_length=100,null=True,blank=True)
    change	= models.CharField(max_length=100,null=True,blank=True)
    pct_chg	= models.CharField(max_length=100,null=True,blank=True)
    vol	    = models.CharField(max_length=100,null=True,blank=True)
    amount	= models.CharField(max_length=100,null=True,blank=True)
    