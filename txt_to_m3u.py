import re
from dataclasses import dataclass
from channel_data import get_channel_by_name, get_channel_by_tvg_name
from typing import Optional

source_files = ["iptv4.txt", "IPV6.txt"]
target_files = ["iptv4.m3u", "IPV6.m3u"]

m3u_title = '#EXTM3U x-tvg-url="http://epg.51zmt.top:8000/e.xml"'
# m3u_title = 'EXTM3U x-tvg-url="https://live.fanmingming.com/e.xml"'


@dataclass()
class Channel:
    name: str
    url: str
    group_title: Optional[str]
    tvg_logo: Optional[str]
    tvg_name: Optional[str]


# 循环处理每个文件
for i in range(len(source_files)):
    channels = []
    with open(file=source_files[i], mode='r', encoding="utf-8") as f:
        group_title = None
        for line in f.readlines():
            # 获取分组名称
            if "#genre#" in line:
                pattern = r'(.+?),#genre#'
                result = re.search(pattern, line)
                group_title = result.groups()[0]
                continue  # 跳过分组行
            line = line.strip()
            if line == "":
                continue  # 空行不处理
            name, url = line.split(",")
            # 从字典中获取频道信息
            c = get_channel_by_name(name)
            # 如果txt中的频道名称使用了tvg-name,注释掉上面一行，打开下面一行
            # c = get_channel_by_tvg_name(name)
            if c is not None:
                channel = Channel(name=name, url=url, group_title=group_title, tvg_logo=c.get("tvg-logo"),
                                  tvg_name=c.get("tvg-name"))
            else:
                channel = Channel(name=name, url=url, group_title=group_title, tvg_logo=None, tvg_name=None)
            channels.append(channel)

    # 写入目标文件
    with open(file=target_files[i], mode="w", encoding="utf-8") as f:
        f.write(m3u_title + "\n")
        for channel in channels:
            channel_title = "#EXTINF:-1"
            if channel.tvg_name is not None:
                channel_title += f' tvg-name="{channel.tvg_name}"'
            if channel.tvg_logo is not None:
                channel_title += f' tvg-logo="{channel.tvg_logo}"'
            if channel.group_title is not None:
                channel_title += f' group-title="{channel.group_title}"'
            channel_title += f",{channel.name}"
            f.write(channel_title + "\n")
            f.write(channel.url + "\n")
