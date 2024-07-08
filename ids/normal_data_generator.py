import pandas as pd
import numpy as np

def generate_normal_synthetic_data(num_samples):
    normal_data = {}
    normal_data = pd.DataFrame(normal_data)

    for _ in range(num_samples):
        count = np.random.randint(1, 10)
        srv_count = np.random.choice([1, 2, 3])
        same_srv_rate = srv_count / count
        dst_host_count = np.random.choice([2, 255])
        dst_host_same_srv_rate = np.random.random()

        data = {
            'duration': 0,
            'protocol_type': 'icmp',
            'service': 'eco_i',
            'flag': 'SF',
            'src_bytes': np.random.randint(30, 180),
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
            'srv_count': srv_count,
            'serror_rate': 0,
            'srv_serror_rate': 0,
            'rerror_rate': 0,
            'srv_rerror_rate': 0,
            'same_srv_rate': same_srv_rate,
            'diff_srv_rate': 1 - same_srv_rate,
            'srv_diff_host_rate': 0,
            'dst_host_count': dst_host_count,
            'dst_host_srv_count': np.random.randint(1, dst_host_count),
            'dst_host_same_srv_rate': dst_host_same_srv_rate,
            'dst_host_diff_srv_rate': 1 - dst_host_same_srv_rate,
            'dst_host_same_src_port_rate': np.random.random(),
            'dst_host_srv_diff_host_rate': 0,
            'dst_host_serror_rate': 0,
            'dst_host_srv_serror_rate': 0,
            'dst_host_rerror_rate': 0,
            'dst_host_srv_rerror_rate': 0,
            'label': 'normal',
            'difficulty': 21
        }

        data_df = pd.DataFrame([data])
        normal_data = pd.concat([normal_data, data_df], ignore_index=True)

    normal_data['serror_rate'] = normal_data['serror_rate'].round(2)
    normal_data['srv_serror_rate'] = normal_data['srv_serror_rate'].round(2)
    normal_data['rerror_rate'] = normal_data['rerror_rate'].round(2)
    normal_data['srv_rerror_rate'] = normal_data['srv_rerror_rate'].round(2)
    normal_data['same_srv_rate'] = normal_data['same_srv_rate'].round(2)
    normal_data['diff_srv_rate'] = normal_data['diff_srv_rate'].round(2)
    normal_data['srv_diff_host_rate'] = normal_data['srv_diff_host_rate'].round(2)
    normal_data['dst_host_same_srv_rate'] = normal_data['dst_host_same_srv_rate'].round(2)
    normal_data['dst_host_diff_srv_rate'] = normal_data['dst_host_diff_srv_rate'].round(2)
    normal_data['dst_host_same_src_port_rate'] = normal_data['dst_host_same_src_port_rate'].round(2)
    normal_data['dst_host_srv_diff_host_rate'] = normal_data['dst_host_srv_diff_host_rate'].round(2)
    normal_data['dst_host_serror_rate'] = normal_data['dst_host_serror_rate'].round(2)
    normal_data['dst_host_srv_serror_rate'] = normal_data['dst_host_srv_serror_rate'].round(2)
    normal_data['dst_host_rerror_rate'] = normal_data['dst_host_rerror_rate'].round(2)
    normal_data['dst_host_srv_rerror_rate'] = normal_data['dst_host_srv_rerror_rate'].round(2)

    data_df = pd.DataFrame([data])
    normal_data = pd.concat([normal_data, data_df], ignore_index=True)

    set_name = 'synthetic_normal_nsl_kdd.csv'
    normal_data.to_csv(set_name, index=False)
    
    return normal_data
