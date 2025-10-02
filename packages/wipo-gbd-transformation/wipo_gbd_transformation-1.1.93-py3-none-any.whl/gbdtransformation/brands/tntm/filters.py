import gbdtransformation.brands.ipas.filters as ipas
import gbdtransformation.common.filters as commons

ignore_namespace = [
   'http://www.wipo.int/standards/XMLSchema/trademarks',
   'http://www.wipo.int/standards/XMLSchema/wo-trademarks']

def get_appdate(appdate, appnum):
    return appnum.split('/')[-2].zfill(4)


def translate_type(header):
    code = header.TransactionCode

    if code == 'Marque Madrid': return 'TRADEMARK'
    if code == 'Marque Nationale': return 'TRADEMARK'
    if code == 'Marque Nationale Online': return 'TRADEMARK'
    if code == 'Marque Etrangere': return 'TRADEMARK'
    if code == 'Marque Etrangere Online': return 'TRADEMARK'
    if code == 'Marque Divisionelle': return 'TRADEMARK'

    raise Exception('Type "%s" is not mapped.' % code)

def translate_kind(trademark, header):
    subcode = header.TransactionSubCode

    if subcode == 'Protocole Madrid': return ['Individual']
    if subcode == 'Nationale Prod & Services': return ['Individual']
    if subcode == 'Nationale Collective': return ['Collective']
    if subcode == 'Nationale Collective Online': return ['Collective']
    if subcode == 'Etrangere Prod & Services': return ['Individual']
    if subcode == 'Etrangere Collective': return ['Collective']
    if subcode == 'Divisionelle Produit/Service': return ['Other']

    if subcode == 'Etrang Prod/Serv Online': return ['Individual']
    if subcode == 'Etrang Collevtive Online': return ['Collective']

    raise Exception('Kind "%s" not mapped.' % subcode)

def translate_status(trademark):
    status = trademark.MarkCurrentStatusCode

    return ipas.translate_status(status)

def translate_feature(trademark):
    feature = trademark.MarkFeature

    # if not feature: return 'Undefined'

    return ipas.translate_feature(feature)

def translate_event(event):
    return ipas.translate_event(event)

# ---------------------------------------
# TODO: separate values like
# {'fr': ['PICO BELLO بيكوبالو']}
def verbal_lang_map(markVerbalElements, applang=None):
    # print( ipas.verbal_lang_map(markVerbalElements, applang=applang))
    return ipas.verbal_lang_map(markVerbalElements, applang=applang)

def get_registration_nb(trademark, tmstatus):
    if trademark.RegistrationNumber:
        return trademark.RegistrationNumber

    if not tmstatus in ['Expired', 'Registered']:
        return None

    # a way to deduce the registration number
    appnum_parts = trademark.ApplicationNumber.split('/')
    regnum = '%s/%s' % (appnum_parts[-2], appnum_parts[-1])
    return regnum

def get_expiry_date(trademark, tmstatus):
    return ipas.get_expiry_date(trademark, tmstatus)

def get_registration_date(trademark, tmstatus):
    return ipas.get_registration_date(trademark, tmstatus)

def is_international(header):
    code = header.TransactionCode
    return code == 'Marque Madrid'

# TN/M/100/673426
def get_ir_refnum(appnum):
    return appnum.split('/')[-1]

def get_goods_services(goods_services):
    return ipas.get_goods_services(goods_services)
