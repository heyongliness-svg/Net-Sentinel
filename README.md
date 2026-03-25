# Net-Sentinel: 高性能加密流量恶意识别系统

## 1. 项目简介
Net-Sentinel 是一款针对 TLS 1.3 和 QUIC 等现代加密协议开发的恶意流量识别系统。本项目通过提取报文长度序列（SPL）、双向延迟（RTT）等时空指纹特征，结合深度学习模型实现对隐蔽传输和恶意攻击的实时检测。

## 2. 核心功能
* **多协议支持**：兼容 TLS 1.3、QUIC、HTTP/3 等复杂加密环境。
* **高精识别**：内置集成学习检测引擎，中期测试准确率达 98.5%。
- **轻量化设计**：单流检测时延控制在毫秒级，支持边缘侧部署。

## 3. 安装步骤
### 环境依赖
- Python 3.8+
- Scapy, Numpy, Scikit-learn
- Tcpdump (用于底层捕获)

### 快速安装
```bash
git clone [https://github.com/YourUsername/Net-Sentinel.git](https://github.com/YourUsername/Net-Sentinel.git)
cd Net-Sentinel
pip install -r requirements.txt
4. 使用方法
实时流量分析
Bash
sudo python main.py --iface eth0 --mode real-time
离线 PCAP 分析
Bash
python main.py --file data/sample_malicious.pcap
