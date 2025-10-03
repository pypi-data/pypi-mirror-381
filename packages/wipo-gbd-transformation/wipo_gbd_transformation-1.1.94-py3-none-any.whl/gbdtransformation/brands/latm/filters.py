import gbdtransformation.brands.ipas.filters as ipas

ignore_namespace = [
   'http://www.wipo.int/standards/XMLSchema/trademarks',
   'http://www.wipo.int/standards/XMLSchema/wo-trademarks']

def get_appdate(appdate, appnum):
    return ipas.get_appdate(appdate, appnum)

def translate_type(header):
    code = header.TransactionCode

    # extraction missing info.
    if not code:
        raise Exception('Incomplete Document Info')

    if code == 'Trademark': return 'TRADEMARK'
    if code == 'Trademark - Individual': return 'TRADEMARK'
    if code == 'Trademark - Madrid': return 'TRADEMARK'
    if code == 'Trademark - Collective': return 'TRADEMARK'

    raise Exception('Type "%s" is not mapped.' % code)

def translate_kind(trademark, header):
    code = header.TransactionCode
    subcode = header.TransactionSubCode

    if subcode == 'Trademark': return ['Individual']
    if subcode == 'TM Individual': return ['Individual']
    if subcode == 'TM Individual - Renewal': return ['Individual']
    if subcode == 'Trademark - Madrid': return ['Individual']

    if subcode == 'Collective Mark': return ['Collective']
    if subcode == 'TM Collective - Renewal': return ['Collective']
    if subcode == 'Certification Mark': return ['Certificate']

    raise Exception('Kind "%s" not mapped.' % subcode)

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

# TODO: language code in data is la (wrong X)
#       language code for Lao is lo (la is Latin)
# {'la': ['FAB POWER PLUS IN THAI']} <- en
# {'la': ['ທະວີໂຊກ ພ້ອມດ້ວຍຮູບ']} <- lo
def verbal_lang_map(markVerbalElements, applang=None):
    # print( ipas.verbal_lang_map(markVerbalElements, applang=applang))
    return ipas.verbal_lang_map(markVerbalElements, applang=applang)

def get_registration_nb(trademark, tmstatus):
    if trademark.RegistrationNumber:
        return trademark.RegistrationNumber

    if not tmstatus in ['Expired', 'Registered']:
        return None

    # no way to deduce registration number
    return None

def get_expiry_date(trademark, tmstatus):
    return ipas.get_expiry_date(trademark, tmstatus)

def get_registration_date(trademark, tmstatus):
    return ipas.get_registration_date(trademark, tmstatus)

def is_international(header):
    code = header.TransactionCode
    return code == 'Trademark - Madrid'

# M/1350065
def get_ir_refnum(appnum):
    return appnum.split('/')[-1]

def get_goods_services(goods_services):
    return ipas.get_goods_services(goods_services)
