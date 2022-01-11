# from vininfo import Vin
#
# vin = Vin('XTAGFK330JY144213')
#
# print(vin.annotate())
# code =vin.country_code
# valied = vin.verify_checksum()





from vininfo import Vin

vin = Vin('VF1LM1B0H36666155')

vin.country  # France
vin.manufacturer  # Renault
vin.region  # Europe
vin.wmi  # VF1
vin.vds  # LM1B0H
vin.vis  # 36666155

annotated = vin.annotate()
details = vin.details

vin.verify_checksum()  # False
Vin('1M8GDM9AXKP042788').verify_checksum()  # True

print(vin.annotate())
print(vin.vis)