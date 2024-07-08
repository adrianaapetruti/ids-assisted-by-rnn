import pandas as pd
import numpy as np

def generate_u2r_synthetic_data(num_samples):
    u2r_data = {}
    u2r_data = pd.DataFrame(u2r_data)

    for _ in range(num_samples):
        count = np.random.randint(1, 3)
        dst_host_count = np.random.randint(1, 10)
        dst_host_rerror_rate = np.random.random()

        data = {
            'duration': np.random.randint(150, 300),
            'protocol_type': 'tcp',
            'service': 'telnet',
            'flag': 'SF',
            'src_bytes': np.random.randint(1000, 6000),
            'dst_bytes': np.random.randint(2000, 16000),
            'land': 0,
            'wrong_fragment': 0,
            'urgent': 0,
            'hot': np.random.randint(1, 5),
            'num_failed_logins': 0,
            'logged_in': 1,
            'num_compromised': np.random.randint(0, 4),
            'root_shell': np.random.choice([0, 1]),
            'su_attempted': 0,
            'num_root': np.random.choice([0, 1]),
            'num_file_creations': 1,
            'num_shells': 0,
            'num_access_files': 0,
            'num_outbound_cmds': 0,
            'is_host_login': 0,
            'is_guest_login': 0,
            'count': count,
            'srv_count': count,
            'serror_rate': 0,
            'srv_serror_rate': 0,
            'rerror_rate': 0,
            'srv_rerror_rate': 0,
            'same_srv_rate': 1,
            'diff_srv_rate': 0,
            'srv_diff_host_rate': 0,
            'dst_host_count': dst_host_count,
            'dst_host_srv_count': dst_host_count,
            'dst_host_same_srv_rate': 1,
            'dst_host_diff_srv_rate': 0,
            'dst_host_same_src_port_rate': dst_host_rerror_rate,
            'dst_host_srv_diff_host_rate': 0,
            'dst_host_serror_rate': 0,
            'dst_host_srv_serror_rate': 0,
            'dst_host_rerror_rate': dst_host_rerror_rate,
            'dst_host_srv_rerror_rate': dst_host_rerror_rate,
            'label': 'buffer_overflow',
            'difficulty': np.random.randint(1, 5)
        }

        data_df = pd.DataFrame([data])
        u2r_data = pd.concat([u2r_data, data_df], ignore_index=True)

    u2r_data['serror_rate'] = u2r_data['serror_rate'].round(2)
    u2r_data['srv_serror_rate'] = u2r_data['srv_serror_rate'].round(2)
    u2r_data['rerror_rate'] = u2r_data['rerror_rate'].round(2)
    u2r_data['srv_rerror_rate'] = u2r_data['srv_rerror_rate'].round(2)
    u2r_data['same_srv_rate'] = u2r_data['same_srv_rate'].round(2)
    u2r_data['diff_srv_rate'] = u2r_data['diff_srv_rate'].round(2)
    u2r_data['srv_diff_host_rate'] = u2r_data['srv_diff_host_rate'].round(2)
    u2r_data['dst_host_same_srv_rate'] = u2r_data['dst_host_same_srv_rate'].round(2)
    u2r_data['dst_host_diff_srv_rate'] = u2r_data['dst_host_diff_srv_rate'].round(2)
    u2r_data['dst_host_same_src_port_rate'] = u2r_data['dst_host_same_src_port_rate'].round(2)
    u2r_data['dst_host_srv_diff_host_rate'] = u2r_data['dst_host_srv_diff_host_rate'].round(2)
    u2r_data['dst_host_serror_rate'] = u2r_data['dst_host_serror_rate'].round(2)
    u2r_data['dst_host_srv_serror_rate'] = u2r_data['dst_host_srv_serror_rate'].round(2)
    u2r_data['dst_host_rerror_rate'] = u2r_data['dst_host_rerror_rate'].round(2)
    u2r_data['dst_host_srv_rerror_rate'] = u2r_data['dst_host_srv_rerror_rate'].round(2)

    data_df = pd.DataFrame([data])
    u2r_data = pd.concat([u2r_data, data_df], ignore_index=True)

    set_name = 'synthetic_u2r_nsl_kdd.csv'
    u2r_data.to_csv(set_name, index=False)
    
    return u2r_data
