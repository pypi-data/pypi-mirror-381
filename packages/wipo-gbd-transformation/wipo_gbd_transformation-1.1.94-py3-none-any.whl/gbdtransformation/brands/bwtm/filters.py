import gbdtransformation.brands.ipas.filters as ipas
import gbdtransformation.common.filters as commons

ignore_namespace = [
   'http://www.wipo.int/standards/XMLSchema/trademarks',
   'http://www.wipo.int/standards/XMLSchema/wo-trademarks']

def get_appdate(appdate, appnum):
    return ipas.get_appdate(appdate, appnum)

# language code is not accurate for markVerbalElement
def guess_language(text, lang, default):
    if commons.is_latin(text):
        return 'en'
    else:
        return commons.guess_language(text, lang, default)

def translate_type(header):
    code = header.TransactionCode

    if code == 'National Marks': return 'TRADEMARK'
    if code == 'Madrid Marks': return 'TRADEMARK'
    if code == 'Banjul Protocol Marks': return 'TRADEMARK'

    raise Exception('Type "%s" is not mapped.' % code)

def translate_kind(trademark, header):
    code = header.TransactionCode

    if code == 'National Marks': return ['Individual']
    if code == 'Madrid Marks': return ['Individual']
    if code == 'Banjul Protocol Marks': return ['Individual']

    # it is set to Other for all
    # kind = trademark.KindMark

    raise Exception('Kind "%s" not mapped.' % code)

def translate_status(trademark):
    status = trademark.MarkCurrentStatusCode

    if status == 'Inactive':
        if trademark.ExpiryDate: return 'Expired'
        else: return 'Ended'

    return ipas.translate_status(status)

def translate_feature(trademark):
    feature = trademark.MarkFeature

    if not feature: return 'Undefined'

    return ipas.translate_feature(feature)

def translate_event(event):
    return ipas.translate_event(event)

# ---------------------------------------

def verbal_lang_map(markVerbalElements, applang=None):
    return ipas.verbal_lang_map(markVerbalElements, applang=applang)

def get_registration_nb(trademark, tmstatus):
    if trademark.RegistrationNumber:
        return trademark.RegistrationNumber

    if not tmstatus in ['Expired', 'Registered']:
        return None

    # BW/M/2011/815 -> 2011000815
    appnum_parts = trademark.ApplicationNumber.split('/')
    appyear = appnum_parts[-2]
    appnum  = appnum_parts[-1]
    regnum = '%s%s' %(appyear, appnum.zfill(6))
    return regnum

def get_expiry_date(trademark, tmstatus):
    return ipas.get_expiry_date(trademark, tmstatus)

def get_registration_date(trademark, tmstatus):
    return ipas.get_registration_date(trademark, tmstatus)

def is_international(content):
    return content.TransactionCode == 'Madrid Marks'

def get_ir_refnum(appnum):
    return appnum.split('/')[-1]

def get_goods_services(goods_services):
    return ipas.get_goods_services(goods_services)
