import re
from dataclasses import dataclass
from channel_data import get_channel_by_name, get_channel_by_tvg_name  # 假设这个模块存在
from typing import Optional

source_files = ["iptv4.txt"]
target_files = ["iptv4.m3u"]

m3u_title = '#EXTM3U x-tvg-url="http://epg.zxyxndc.top/e.xml"'


@dataclass
class Channel:
    name: str
    url: str
    group_title: Optional[str] = None  # 使用默认值，简化后续代码
    tvg_logo: Optional[str] = None
    tvg_name: Optional[str] = None


for source_file, target_file in zip(source_files, target_files): # 直接用zip迭代
    channels = []
    with open(source_file, "r", encoding="utf-8") as f:
        group_title = None
        for line_num, line in enumerate(f, 1): # 添加行号，方便调试
            line = line.strip()
            if not line:
                continue

            if "#genre#" in line:
                match = re.search(r'(.+?),#genre#', line)
                if match:
                    group_title = match.group(1)
                else:
                    print(f"Warning: Invalid genre line in {source_file}:{line_num}: {line}")
                continue

            try:
                name, url, *_ = line.split(",")  # 使用 *_ 忽略额外的元素
            except ValueError:
                print(f"Error: Invalid line format in {source_file}:{line_num}: {line}")
                continue

            channel_data = get_channel_by_name(name) or get_channel_by_tvg_name(name) #尝试两个方法
            #  使用 or : 如果get_channel_by_name返回None，则使用get_channel_by_tvg_name的结果

            channels.append(Channel(name=name, url=url, group_title=group_title,
                                      tvg_logo=channel_data.get("tvg-logo") if channel_data else None,
                                      tvg_name=channel_data.get("tvg-name") if channel_data else None))



    with open(target_file, "w", encoding="utf-8") as f:
        f.write(m3u_title + "\n")
        for channel in channels:
            extinf = f'#EXTINF:-1 tvg-name="{channel.tvg_name or ""}" ' \
                     f'tvg-logo="{channel.tvg_logo or ""}" ' \
                     f'group-title="{channel.group_title or ""}",{channel.name}\n'
            f.write(extinf)
            f.write(channel.url + "\n")

