attackTypes = {
        'normal': ['normal'],
        'Dos': ['neptune', 'satan', 'smurf', 'apache2', 'back', 'mailbomb',
            'teardrop', 'pod', 'land', 'worm', 'udpstorm'],
        'Probe': ['mscan', 'ipsweep', 'portsweep', 'nmap', 'snmpguess', 'saint'],
        'U2R': ['guess_passwd', 'processtable', 'buffer_overflow', 'multihop',
            'rootkit', 'named', 'ps', 'sendmail', 'xterm', 'xlock', 'phf',
            'loadmodule', 'perl', 'sqlattack', 'spy'],
        'R2L': ['warezmaster', 'snmpgetattack', 'httptunnel', 'warezclient', 'imap',
            'ftp_write', 'xsnoop']
        }

attackTypesMapping = {}

for type, subType in attackTypes.items():
    for i in subType:
        attackTypesMapping[i] = type   
    

def attack_types_mapping(set):            
    set['label'] = set.label.apply(lambda x: attackTypesMapping[x])
    return set                           
