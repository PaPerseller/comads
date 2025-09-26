import os

def process_httpdns_rules():
    output_dir = "/root"
    output_file = os.path.join(output_dir, "httpdns-cn.txt")
    
    # 原始文件的URL
    url = "https://raw.githubusercontent.com/v2fly/domain-list-community/refs/heads/master/data/category-httpdns-cn"
    
    try:
        # 读取远程文件内容
        import urllib.request
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
        
        # 处理内容
        processed_lines = []
        for line in content.splitlines():
            # 跳过注释行和空行
            if line.strip().startswith('#') or not line.strip():
                continue
            
            # 移除@ads后缀并提取域名
            domain = line.split('@ads')[0].strip()
            
            # 转换为AdGuard Home格式
            if domain:
                adguard_format = f"||{domain}^"
                processed_lines.append(adguard_format)
        
        # 写入文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(processed_lines))
            
    except Exception as e:
        print(f"处理过程中出现错误: {e}")

if __name__ == "__main__":
    process_httpdns_rules()
