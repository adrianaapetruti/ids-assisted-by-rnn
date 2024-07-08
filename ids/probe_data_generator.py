import pandas as pd
import numpy as np

def generate_probe_synthetic_data(num_samples):
    probe_data = {}
    probe_data = pd.DataFrame(probe_data)

    for _ in range(num_samples):
        data = {
            'duration': 0,
            'protocol_type': 'icmp',
            'service': 'eco_i',
            'flag': 'SF',
            'src_bytes': np.random.choice([8, 18]),
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
            'count': 0,
            'srv_count': 0,
            'serror_rate': 0,
            'srv_serror_rate': 0,
            'rerror_rate': 0,
            'srv_rerror_rate': 0,
            'same_srv_rate': 0,
            'diff_srv_rate': 0,
            'srv_diff_host_rate': np.random.choice([0, 1]),
            'dst_host_count': np.random.choice([1, 2]),
            'dst_host_srv_count': np.random.randint(0, 140),
            'dst_host_same_srv_rate': 1,
            'dst_host_diff_srv_rate': 0,
            'dst_host_same_src_port_rate': 1,
            'dst_host_srv_diff_host_rate': np.random.random(),
            'dst_host_serror_rate': 0,
            'dst_host_srv_serror_rate': 0,
            'dst_host_rerror_rate': 0,
            'dst_host_srv_rerror_rate': 0,
            'label': 'ipsweep',
            'difficulty': np.random.randint(15, 18)
        }

        data_df = pd.DataFrame([data])
        probe_data = pd.concat([probe_data, data_df], ignore_index=True)

    probe_data['serror_rate'] = probe_data['serror_rate'].round(2)
    probe_data['srv_serror_rate'] = probe_data['srv_serror_rate'].round(2)
    probe_data['rerror_rate'] = probe_data['rerror_rate'].round(2)
    probe_data['srv_rerror_rate'] = probe_data['srv_rerror_rate'].round(2)
    probe_data['same_srv_rate'] = probe_data['same_srv_rate'].round(2)
    probe_data['diff_srv_rate'] = probe_data['diff_srv_rate'].round(2)
    probe_data['srv_diff_host_rate'] = probe_data['srv_diff_host_rate'].round(2)
    probe_data['dst_host_same_srv_rate'] = probe_data['dst_host_same_srv_rate'].round(2)
    probe_data['dst_host_diff_srv_rate'] = probe_data['dst_host_diff_srv_rate'].round(2)
    probe_data['dst_host_same_src_port_rate'] = probe_data['dst_host_same_src_port_rate'].round(2)
    probe_data['dst_host_srv_diff_host_rate'] = probe_data['dst_host_srv_diff_host_rate'].round(2)
    probe_data['dst_host_serror_rate'] = probe_data['dst_host_serror_rate'].round(2)
    probe_data['dst_host_srv_serror_rate'] = probe_data['dst_host_srv_serror_rate'].round(2)
    probe_data['dst_host_rerror_rate'] = probe_data['dst_host_rerror_rate'].round(2)
    probe_data['dst_host_srv_rerror_rate'] = probe_data['dst_host_srv_rerror_rate'].round(2)

    data_df = pd.DataFrame([data])
    probe_data = pd.concat([probe_data, data_df], ignore_index=True)

    set_name = 'synthetic_probe_nsl_kdd.csv'
    probe_data.to_csv(set_name, index=False)
    
    return probe_data
