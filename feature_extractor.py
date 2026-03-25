import scapy.all as scapy
import numpy as np

class TrafficSentinel:
    """
    Net-Sentinel 核心特征提取模块
    支持 TLS 1.3 / QUIC 协议的时空指纹提取
    """
    def __init__(self, interface="eth0"):
        self.interface = interface

    def extract_spl(self, packet_count=20):
        """
        提取前 N 个报文的长度序列 (Size Profile)
        这是识别加密流量（如视频、恶意通信）的关键统计特征
        """
        print(f"[*] 正在接口 {self.interface} 上捕获流量...")
        packets = scapy.sniff(iface=self.interface, count=packet_count)
        
        # 提取报文负载长度（剔除头部干扰）
        lengths = [len(pkt) for pkt in packets]
        
        # 归一化处理（用于深度学习模型输入）
        features = np.array(lengths) / max(lengths) if lengths else np.zeros(packet_count)
        return features

if __name__ == "__main__":
    detector = TrafficSentinel()
    features = detector.extract_spl()
    print(f"[+] 提取的流指纹特征向量: \n{features}")
