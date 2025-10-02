import gbdtransformation.brands.ipas.filters as ipas
import gbdtransformation.common.filters as commons

ignore_namespace = [
   'http://www.wipo.int/standards/XMLSchema/trademarks',
   'http://www.wipo.int/standards/XMLSchema/wo-trademarks']

def get_appdate(appdate, appnum):
    return appnum.split('/')[-2]

def translate_type(header):
    code = header.TransactionCode

    if code == 'Marque Nationale': return 'TRADEMARK'
    if code == 'Marque Divisionelle': return 'TRADEMARK'

    # no way to deduce the IR (ask the office)
    if code == 'Marque Madrid': return 'TRADEMARK'

    raise Exception('Type "%s" is not mapped.' % code)

def translate_kind(trademark, header):
    code = header.TransactionCode
    subcode = header.TransactionSubCode

    if subcode == 'Nationale Prod & Services': return ['Individual']
    if subcode == 'Nationale Collective': return ['Collective']

    if code == 'Marque Divisionelle': return ['Other']
    if code == 'Marque Madrid': return ['Individual']

    raise Exception('Kind "%s" not mapped.' % subcode)

def translate_status(trademark):
    status = trademark.MarkCurrentStatusCode

    if status == '3860': return 'Unknown'

    return ipas.translate_status(status)

def translate_feature(trademark):
    feature = trademark.MarkFeature

    if not feature: return 'Undefined'

    return ipas.translate_feature(feature)

def translate_event(event):
    return ipas.translate_event(event)

# ---------------------------------------

# TODO: split on language cahnge {'fr': ['SABBAQLI سبقلي']}
def verbal_lang_map(markVerbalElements, applang=None):
    return ipas.verbal_lang_map(markVerbalElements, applang=applang)

def get_registration_nb(trademark, tmstatus):
    if trademark.RegistrationNumber:
        return trademark.RegistrationNumber

    if not tmstatus in ['Expired', 'Registered']:
        return None

    raise Exception('!!')

    return None

def get_expiry_date(trademark, tmstatus):
    return ipas.get_expiry_date(trademark, tmstatus)

def get_registration_date(trademark, tmstatus):
    return ipas.get_registration_date(trademark, tmstatus)

def is_international(content):
    return False

def get_ir_refnum(appnum):
    return

def get_goods_services(goods_services):
    return ipas.get_goods_services(goods_services)
