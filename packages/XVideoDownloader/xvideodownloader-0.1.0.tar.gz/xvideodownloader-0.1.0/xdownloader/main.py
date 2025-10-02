import requests
import time
import os
from typing import Tuple, Dict, Any

class XDownloader:
    BASE_URL = "https://api.x-downloader.com"

    def __init__(self):
        self.session = requests.Session()

    def validate_url(self, tweet_url: str) -> int:
        try:
            resp = self.session.post(f"{self.BASE_URL}/validate", json={"url": tweet_url}, timeout=10)
            if resp.status_code == 200 and resp.json().get("status") == "ok":
                return 0
            return 1
        except Exception:
            return 1

    def request_download(self, tweet_url: str, filetype=".mp4") -> Tuple[int, str]:
        try:
            resp = self.session.post(f"{self.BASE_URL}/request", json={"url": tweet_url, "type": filetype}, timeout=10)
            if resp.status_code == 200 and "_id" in resp.json():
                return 0, resp.json()["_id"]
            return 1, ""
        except Exception:
            return 1, ""

    def check_status(self, file_id: str) -> Tuple[int, Dict[str, Any]]:
        try:
            resp = self.session.get(f"{self.BASE_URL}/download/{file_id}", timeout=10)
            if resp.status_code == 200:
                return 0, resp.json()
            return 1, {}
        except Exception:
            return 1, {}

    def download_file(self, host: str, filename: str, save_as: str) -> int:
        try:
            url = f"https://{host}/{filename}"
            with self.session.get(url, stream=True, timeout=30) as r:
                r.raise_for_status()
                with open(save_as, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
            return 0
        except Exception:
            return 1

    def download_tweet_video(self, tweet_url: str, resolution="720x1280") -> int:
        if self.validate_url(tweet_url) != 0:
            return 1
        status, file_id = self.request_download(tweet_url)
        if status != 0:
            return 2
        data = {}
        for _ in range(30):
            s, data = self.check_status(file_id)
            if s != 0:
                return 3
            if data.get("status") == "finished":
                break
            time.sleep(2)
        else:
            return 3
        formats = data.get("formats", [])
        if not formats:
            return 4
        target = next((f for f in formats if f["label"] == resolution), formats[-1])
        save_as = (data.get("titleFilename") or "output") + ".mp4"
        status = self.download_file(target["host"], target["filename"], save_as)
        if status != 0:
            return 5
        return 0