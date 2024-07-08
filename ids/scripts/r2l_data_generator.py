import pandas as pd
import numpy as np

def generate_flag():
    return np.random.choice(['SF', 'SH'])

def generate_duration(flag):
    if flag == 'SF':
        duration = np.random.randint(30, 40)
    else:
        duration = 0
    return duration      

def generate_src_bytes(flag):
    if flag == 'SH':
        src_bytes = 0
    else:
        src_bytes = np.random.randint(1000, 1500)
    return src_bytes           

def generate_dst_bytes(flag):
    if flag == 'SH':
        dst_bytes = 0
    else:
        dst_bytes = np.random.randint(10000, 65000)
    return dst_bytes 

def generate_count(flag):
    if flag == 'SH':
        count = np.random.randint(1, 2)
    else:
        count = 1
    return count

def generate_srv_count(flag):
    if flag == 'SH':
        srv_count = np.random.randint(100, 500)
    else:
        srv_count = 1
    return srv_count

def generate_serror_rate(flag):
    if flag == 'SH':
        serror_rate = 1
    else:
        serror_rate = 0
    return serror_rate

def generate_srv_serror_rate(flag):
    if flag == 'SH':
        srv_serror_rate = np.random.choice([0.58, 0.78])
    else:
        srv_serror_rate = 0
    return srv_serror_rate

def generate_srv_rerror_rate(flag):
    if flag == 'SH':
        srv_rerror_rate = np.random.choice([0.03, 0.04])
    else:
        srv_rerror_rate = 0
    return srv_rerror_rate

def generate_srv_diff_host_rate(flag):
    if flag == 'SH':
        srv_diff_host_rate = np.random.choice([0.28, 0.37])
    else:
        srv_diff_host_rate = 0
    return srv_diff_host_rate

def generate_dst_host_same_src_port_rate(flag):
    if flag == 'SH':
        dst_host_same_src_port_rate = np.random.uniform(0.75, 1)
    else:
        dst_host_same_src_port_rate = 0
    return dst_host_same_src_port_rate

def generate_dst_host_serror_rate(flag):
    if flag == 'SH':
        dst_host_serror_rate = np.random.uniform(0.5, 1)
    else:
        dst_host_serror_rate = np.random.random()
    return dst_host_serror_rate

def generate_difficulty(flag):
    if flag == 'SH':
        difficulty = 18
    else:
        difficulty = 12
    return difficulty                     

def generate_r2l_synthetic_data(num_samples):
    r2l_data = {}
    r2l_data = pd.DataFrame(r2l_data)

    for _ in range(num_samples):
        flag = generate_flag()
        dst_host_count = np.random.randint(1, 10)
        dst_host_serror_rate = generate_dst_host_serror_rate(flag)

        data = {
            'duration': generate_duration(flag),
            'protocol_type': 'tcp',
            'service': 'imap4',
            'flag': flag,
            'src_bytes': generate_src_bytes(flag),
            'dst_bytes': generate_dst_bytes(flag),
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
            'count': generate_count(flag),
            'srv_count': generate_srv_count(flag),
            'serror_rate': generate_serror_rate(flag),
            'srv_serror_rate': generate_srv_serror_rate(flag),
            'rerror_rate': 0,
            'srv_rerror_rate': generate_srv_rerror_rate(flag),
            'same_srv_rate': 1,
            'diff_srv_rate': 0,
            'srv_diff_host_rate': generate_srv_diff_host_rate(flag),
            'dst_host_count': dst_host_count,
            'dst_host_srv_count': dst_host_count,
            'dst_host_same_srv_rate': 1,
            'dst_host_diff_srv_rate': 0,
            'dst_host_same_src_port_rate': generate_dst_host_same_src_port_rate(flag),
            'dst_host_srv_diff_host_rate': 0,
            'dst_host_serror_rate': dst_host_serror_rate,
            'dst_host_srv_serror_rate': dst_host_serror_rate,
            'dst_host_rerror_rate': 0,
            'dst_host_srv_rerror_rate': 0,
            'label': 'imap',
            'difficulty': generate_difficulty(flag)
        }

        data_df = pd.DataFrame([data])
        r2l_data = pd.concat([r2l_data, data_df], ignore_index=True)

    r2l_data['serror_rate'] = r2l_data['serror_rate'].round(2)
    r2l_data['srv_serror_rate'] = r2l_data['srv_serror_rate'].round(2)
    r2l_data['rerror_rate'] = r2l_data['rerror_rate'].round(2)
    r2l_data['srv_rerror_rate'] = r2l_data['srv_rerror_rate'].round(2)
    r2l_data['same_srv_rate'] = r2l_data['same_srv_rate'].round(2)
    r2l_data['diff_srv_rate'] = r2l_data['diff_srv_rate'].round(2)
    r2l_data['srv_diff_host_rate'] = r2l_data['srv_diff_host_rate'].round(2)
    r2l_data['dst_host_same_srv_rate'] = r2l_data['dst_host_same_srv_rate'].round(2)
    r2l_data['dst_host_diff_srv_rate'] = r2l_data['dst_host_diff_srv_rate'].round(2)
    r2l_data['dst_host_same_src_port_rate'] = r2l_data['dst_host_same_src_port_rate'].round(2)
    r2l_data['dst_host_srv_diff_host_rate'] = r2l_data['dst_host_srv_diff_host_rate'].round(2)
    r2l_data['dst_host_serror_rate'] = r2l_data['dst_host_serror_rate'].round(2)
    r2l_data['dst_host_srv_serror_rate'] = r2l_data['dst_host_srv_serror_rate'].round(2)
    r2l_data['dst_host_rerror_rate'] = r2l_data['dst_host_rerror_rate'].round(2)
    r2l_data['dst_host_srv_rerror_rate'] = r2l_data['dst_host_srv_rerror_rate'].round(2)

    data_df = pd.DataFrame([data])
    r2l_data = pd.concat([r2l_data, data_df], ignore_index=True)

    set_name = 'synthetic_r2l_nsl_kdd.csv'
    r2l_data.to_csv(set_name, index=False)
    
    return r2l_data
