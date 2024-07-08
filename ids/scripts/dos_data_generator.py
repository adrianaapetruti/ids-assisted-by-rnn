import pandas as pd
import numpy as np

protocol_types = ['tcp', 'icmp']

def generate_protocol():
    protocol = np.random.choice(protocol_types)
    return protocol

def generate_service(protocol):
    if protocol == 'tcp':
        service = 'private'
    if protocol == 'icmp':
        service = 'eco_i' 
    return service

def generate_flag(protocol):
    if protocol == 'icmp':
        flag = 'SF'
    if protocol == 'tcp':
        flag = 'REJ'
    return flag

def generate_src_bytes(protocol):
    if protocol == 'icmp':
        src_bytes = 20
    else:
        src_bytes = 0    
    return src_bytes   

def generate_count(protocol):
    if protocol == 'tcp':
        count = np.random.choice([1, 81])
    else:
        count = np.random.choice([1, 2])
    return count

def generate_serror_rate(protocol):
    if protocol == 'tcp':
        serror_rate = np.random.uniform(0, 0.25)
    else:
        serror_rate = 0
    return serror_rate

def generate_rerror_rate(serror_rate):
    if not serror_rate:
        rerror_rate = 1 - serror_rate
    else:
        rerror_rate = 0
    return rerror_rate

def generate_srv_rerror_rate(protocol):
    if protocol == 'tcp':
        srv_rerror_rate = 1
    else:
        srv_rerror_rate = 0
    return srv_rerror_rate    

def generate_same_srv_rate(protocol):
    if protocol == 'tcp':
        same_srv_rate = np.random.choice([0, 1])
    else:
        same_srv_rate = 1
    return same_srv_rate                          

def generate_dst_host_srv_count(protocol):
    if protocol == 'tcp':
        dst_host_srv_count = 1
    else:
        dst_host_srv_count = np.random.choice(1, 4)
    return dst_host_srv_count

def generate_dst_host_same_srv_rate(dst_host_srv_count):
    return dst_host_srv_count / 255

def generate_dst_host_diff_srv_rate(dst_host_same_srv):
    return 1 - dst_host_same_srv

def generate_dst_host_serror_rate(protocol):
    if protocol == 'tcp':
        dst_host_serror_rate = np.random.uniform(0, 0.1)
    else:
        dst_host_serror_rate = 0
    return dst_host_serror_rate

def generate_dst_host_rerror_rate(protocol):
    if protocol == 'tcp':
        dst_host_rerror_rate = np.random.uniform(0, 1)
    else:
        dst_host_rerror_rate = 0
    return dst_host_rerror_rate  

def generate_dst_host_srv_rerror_rate(dst_host_rerror_rate):
    if dst_host_rerror_rate != 0:
        dst_host_srv_rerror_rate = 1
    else:
        dst_host_srv_rerror_rate = 0
    return dst_host_srv_rerror_rate          

def generate_dos_synthetic_data(num_samples):
    dos_data = {}
    dos_data = pd.DataFrame(dos_data)

    for _ in range(num_samples):
        protocol = generate_protocol()
        src_bytes = generate_src_bytes(protocol)
        count = generate_count(protocol)
        serror_rate = generate_serror_rate(protocol)
        dst_host_srv_count = generate_dst_host_srv_count(protocol)
        dst_host_same_srv_rate = generate_dst_host_same_srv_rate(dst_host_srv_count)
        dst_host_rerror_rate = generate_dst_host_rerror_rate(protocol)
        same_srv_rate = generate_same_srv_rate(protocol)

        data = {
            'duration': 0,
            'protocol_type': protocol,
            'service': generate_service(protocol),
            'flag': generate_flag(protocol),
            'src_bytes': src_bytes,
            'dst_bytes': 0,
            'land': 0,
            'wrong_fragment': 0,
            'urgent': 0,
            'hot': 0,
            'num_failed_logins': 0,
            'logged_in': 0,
            'num_compromised': 0,
            'root_shell': 0,
            'su_attempted': 0,
            'num_root': 0,
            'num_file_creations': 0,
            'num_shells': 0,
            'num_access_files': 0,
            'num_outbound_cmds': 0,
            'is_host_login': 0,
            'is_guest_login': 0,
            'count': count,
            'srv_count': count,
            'serror_rate': serror_rate,
            'srv_serror_rate': 0,
            'rerror_rate': 1 - serror_rate,
            'srv_rerror_rate': generate_srv_rerror_rate(protocol),
            'same_srv_rate': same_srv_rate,
            'diff_srv_rate': 1 - same_srv_rate,
            'srv_diff_host_rate': 0,
            'dst_host_count': 255,
            'dst_host_srv_count': dst_host_srv_count,
            'dst_host_same_srv_rate': dst_host_same_srv_rate,
            'dst_host_diff_srv_rate': generate_dst_host_diff_srv_rate(dst_host_same_srv_rate),
            'dst_host_same_src_port_rate': dst_host_same_srv_rate,
            'dst_host_srv_diff_host_rate': 0,
            'dst_host_serror_rate': generate_dst_host_serror_rate(protocol),
            'dst_host_srv_serror_rate': 0,
            'dst_host_rerror_rate': dst_host_rerror_rate,
            'dst_host_srv_rerror_rate': generate_dst_host_srv_rerror_rate(dst_host_rerror_rate),
            'label': 'satan',
            'difficulty': 20
        }

        data_df = pd.DataFrame([data])
        dos_data = pd.concat([dos_data, data_df], ignore_index=True)

    dos_data['serror_rate'] = dos_data['serror_rate'].round(2)
    dos_data['srv_serror_rate'] = dos_data['srv_serror_rate'].round(2)
    dos_data['rerror_rate'] = dos_data['rerror_rate'].round(2)
    dos_data['srv_rerror_rate'] = dos_data['srv_rerror_rate'].round(2)
    dos_data['same_srv_rate'] = dos_data['same_srv_rate'].round(2)
    dos_data['diff_srv_rate'] = dos_data['diff_srv_rate'].round(2)
    dos_data['srv_diff_host_rate'] = dos_data['srv_diff_host_rate'].round(2)
    dos_data['dst_host_same_srv_rate'] = dos_data['dst_host_same_srv_rate'].round(2)
    dos_data['dst_host_diff_srv_rate'] = dos_data['dst_host_diff_srv_rate'].round(2)
    dos_data['dst_host_same_src_port_rate'] = dos_data['dst_host_same_src_port_rate'].round(2)
    dos_data['dst_host_srv_diff_host_rate'] = dos_data['dst_host_srv_diff_host_rate'].round(2)
    dos_data['dst_host_serror_rate'] = dos_data['dst_host_serror_rate'].round(2)
    dos_data['dst_host_srv_serror_rate'] = dos_data['dst_host_srv_serror_rate'].round(2)
    dos_data['dst_host_rerror_rate'] = dos_data['dst_host_rerror_rate'].round(2)
    dos_data['dst_host_srv_rerror_rate'] = dos_data['dst_host_srv_rerror_rate'].round(2)

    data_df = pd.DataFrame([data])
    dos_data = pd.concat([dos_data, data_df], ignore_index=True)

    set_name = 'synthetic_dos_nsl_kdd.csv'
    dos_data.to_csv(set_name, index=False)
    
    return dos_data
